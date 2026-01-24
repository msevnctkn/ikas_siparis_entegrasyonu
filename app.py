from streamlit_init import *
init_states()
st.set_page_config(layout="wide")
import time

import pandas as pd
from main import *
from ikas_entegrasyon import IKAS_SIPARIS_ENTEGRASYON
from tikli_dataframe import SIPARIS_DATAFRAME_DUZENLE
from veritabani import *
from veritabani import databaseden_butun_verileri_cek
from malzeme_istekleri import *


CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]

st.header("ÖMAS KONSEPT SİPARİŞ TAKİP SİSTEMİ", divider=True, anchor="www.omaskonsept.com", )
sidebarButton = st.sidebar.selectbox("Menü", ["ikas Bekleyen Siparişler",
                                              "Teslim Edilen Siparişler (ikas)",
                                              "Stok Yönetimi",
                                              "Tamamlanan Siparişler",
                                              "Veritabanı",
                                              "Dosya Gönder"])


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

    checkbox_bilgiler = SIPARIS_DATAFRAME_DUZENLE.siparis_tik_tablosu(pd.DataFrame(siparis_listesi), supabase=supabase_nesnesi)

elif sidebarButton == "Stok Yönetimi":
    st.write(HAM_MADDE_STOKLARI())
    st.write(anlik_stoklar_init())
    st.write("---")
    for i in anlik_stoklar_init():
        st.write(st.session_state[i])

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
    st.write("Dosya gönder")
    yuklenen_dosya = st.file_uploader("Yüklemek istediğiniz dosyayı buraya sürükleyin.")
    if yuklenen_dosya != None:
        owner_id = "admin"
        #ext = yuklenen_dosyalar.name.split(".")[-1]
        unique_name = f"{datetime.now().strftime("%d%m%y_%H%M%S")}.pdf"
        storage_path = f"{owner_id}/{unique_name}"
        st.write("storage_path", storage_path)    

    
        file_bytes = yuklenen_dosya.read()
        res = supabase_nesnesi.storage.from_("dosyalar").upload(
            storage_path,
            file_bytes,
            {"content-type": yuklenen_dosya.type}
        )

        if res:
            st.success(f"Yüklendi: {yuklenen_dosya.name}")
            supabase_nesnesi.table("yuklenen_dosyalar").insert({
                "file_name": yuklenen_dosya.name,
                "storage_path": storage_path,
                "owner_id": owner_id
            }).execute()


    st.markdown("Verileri çek")
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