from streamlit_init import *

init_states()
st.set_page_config(page_title='ÖMAS KONSEPT', layout = 'wide', initial_sidebar_state = 'auto')
import time
import os
import pandas as pd
from main import *
from ikas_entegrasyon import IKAS_SIPARIS_ENTEGRASYON
from tikli_dataframe import SIPARIS_DATAFRAME_DUZENLE
from veritabani import *
from veritabani import databaseden_butun_verileri_cek
from malzeme_istekleri import *
from turkiye_tatiller import RESMI_TATILLER


CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]

st.header("ÖMAS KONSEPT SİPARİŞ TAKİP SİSTEMİ", divider=True, anchor="www.omaskonsept.com", )

sidebarButton = st.sidebar.selectbox("Menü", ["ikas Bekleyen Siparişler",
                                              "Teslim Edilen Siparişler (ikas)",
                                              "Müşteriler",
                                              "Stok Yönetimi",
                                              "Tamamlanan Siparişler",
                                              "Veritabanı",
                                              "Dosya Gönder"])

if st.sidebar.button("Session state temizle"):
    st.session_state.clear()

entegrasyon = IKAS_SIPARIS_ENTEGRASYON(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
access_token = entegrasyon.get_access_token()
data = entegrasyon.post_request(access_token=access_token)
siparis_listesi = entegrasyon.siparis_dataframe_hazirla(data=data)
SIPARIS_DATAFRAME_DUZENLE = SIPARIS_DATAFRAME_DUZENLE()
supabase_nesnesi, result = get_connection()
st.session_state["databasedeki_degerler"] = tum_checkboxlari_cek(supabase_nesnesi)

if sidebarButton == "ikas Bekleyen Siparişler":
    st.header("Sipariş Tablosu")

    st.dataframe(siparis_listesi)


    siparis_listesi_copy = pd.DataFrame(siparis_listesi).copy()
    editable_siparis_listesi = st.data_editor(siparis_listesi_copy, num_rows="dynamic", disabled=["siparis_numarasi", "musteri_adi_soyadi","urun_barkodu", "toplam_urun_sayisi", "siparis_durumu" ])
    
    #SİLİNEN SATIRLAR
    silinenler = siparis_listesi_copy[~siparis_listesi_copy["siparis_numarasi"].isin(editable_siparis_listesi["siparis_numarasi"])]
    st.write(silinenler)
    
    
    #siparişleri 'siparisler' isimli veritabanına kaydeder.
    # for _, row in siparis_listesi_copy.iterrows():
    #     supabase_nesnesi.table("siparisler").upsert({
    #     "siparis_numarasi": row["siparis_numarasi"],
    #     "siparis_tarihi": row["siparis_tarihi"],
    #     "musteri_adi_soyadi": row["musteri_adi_soyadi"],
    #     "urun_barkodu": row["urun_barkodu"],
    #     "toplam_urun_sayisi": row["toplam_urun_sayisi"],
    #     "notlar": row.get("notlar"),
    #     "siparis_durumu": row.get("siparis_durumu", "Yeni"),
    #     }).execute()


    
    for _, row in silinenler.iterrows():
        supabase_nesnesi.table("siparisler") \
        .delete() \
        .eq("siparis_numarasi", row["siparis_numarasi"]) \
        .execute()



    # for i in zip(siparis_listesi, editable_siparis_listesi):

    #     st.write(i)
    #     st.write(i["siparis_tarihi"], j["siparis_tarihi"])
    #     if i["siparis_tarihi"] != j["siparis_tarihi"]:
    #         resmi_tatiller = RESMI_TATILLER()
    #         imalat_bitis_suresi_yeni = resmi_tatiller.is_gunu_ekle(j["siparis_tarihi"], is_gunu=12)
    #         st.write(imalat_bitis_suresi_yeni)


        

    checkbox_bilgiler = SIPARIS_DATAFRAME_DUZENLE.uretim_asamalari_tablosu(df=pd.DataFrame(siparis_listesi), supabase=supabase_nesnesi)





elif sidebarButton == "Stok Yönetimi":
    st.write(HAM_MADDE_STOKLARI())
    st.write(anlik_stoklar_init())
    st.write("---")

    if st.button("💾 Veritabanına Kaydet"):

        for stok_key in anlik_stoklar_init():
            if stok_key in st.session_state:
                supabase_nesnesi.table("stoklar").upsert({
                    "stok_ismi": stok_key,
                    "stok_degeri": st.session_state[stok_key]
                }).execute()

        st.success("Tüm stoklar veritabanına kaydedildi ✅")


elif sidebarButton == "Teslim Edilen Siparişler (ikas)":
    st.dataframe(st.session_state["deliveredRows"])


elif sidebarButton == "Veritabanı":
    if st.button("tıklaaa"):
        #st.write(tum_checkboxlari_cek(supabase_nesnesi))

        st.header("checkbox değeri")
        for i in st.session_state["databasedeki_degerler"].values():
            if i["tamamlananlara_gonder"] == True:
                st.write(i)
                #buradaki sıkıntı şu, daha önce tamamlananlara gönderde işaretlenen siparişler de gözüküyor. 


elif sidebarButton == "Dosya Gönder":
    with st.container(border=True):
        st.write("Dosya gönder")
        yuklenen_dosya = st.file_uploader("Yüklemek istediğiniz dosyayı buraya sürükleyin.")

    
    if yuklenen_dosya != None:
        with st.container(border=True):
            st.info(f"""
            **Dosya Adı:** {yuklenen_dosya.name}  
            **Boyut:** {round(yuklenen_dosya.size / 1024, 2)} KB  
            **Tür:** {yuklenen_dosya.type}
            """)
        owner_id = "admin"
        #ext = yuklenen_dosyalar.name.split(".")[-1]
        uzanti = os.path.splitext(yuklenen_dosya.name)[1].lower()
        unique_name = f"{datetime.now().strftime("%d%m%y_%H%M%S")}{uzanti}"
        storage_path = f"{owner_id}/{unique_name}"
     

    
        file_bytes = yuklenen_dosya.read()
        
        res = supabase_nesnesi.storage.from_("dosyalar").upload(
            storage_path,
            file_bytes,
            {"content-type": yuklenen_dosya.type}
        )

        if res:
            
            with st.container(border=True):
      
                st.success(f"Yüklendi: {yuklenen_dosya.name}")
                supabase_nesnesi.table("yuklenen_dosyalar").insert({
                "file_name": yuklenen_dosya.name,
                "storage_path": storage_path,
                "owner_id": owner_id
            }).execute()
    st.write("---")



    st.header("Yüklenen Dosyalar")
    
    geri_donen_datalar = databaseden_butun_verileri_cek(supabase=supabase_nesnesi, table_name="yuklenen_dosyalar")
    
    if not geri_donen_datalar:
        st.warning("Yüklenen Dosya Yok")
    else:
        for data in geri_donen_datalar.data:
            id = data["id"]
            file_name = data["file_name"]
            storage_path = data["storage_path"]
            owner_id = data["owner_id"]
            created_at = data["created_at"]
            url = supabase_nesnesi.storage.from_("dosyalar").get_public_url(storage_path)

            with st.container(border=True):
                st.write("📄", file_name)
                st.link_button("İndir", url)