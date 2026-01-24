#bu sayfa ikastan hazır çekilen dataframe'e yeni kolonlar ekler.
import streamlit as st
from veritabani import *

class SIPARIS_DATAFRAME_DUZENLE():
    def __init__(self):
        pass
    
    def checkbox_degisti(key_name, supabase):
        deger = st.session_state.get(key_name, False)

        kolon, siparis_no = key_name.rsplit("_", 1)
        kolon = kolon.lower().replace(" ", "_")
        siparis_no = int(siparis_no)

        supabase.table("siparis_takip") \
            .upsert({
                "siparis_no": siparis_no,
                kolon: deger
            }) \
            .execute()




    def siparis_tik_tablosu(self, df, supabase):

        self.tik_kolonlari = [
            "mdf_kesildi", "pleksi_kesildi", "boyaya_teslim",
            "cerceve_boyandi", "montaja_teslim", "kargoya_hazir", "tamamlananlara_gonder"
        ]
        liste = []
        st.write("### Üretim Aşamaları Tablosu")

        # Tablo başlıkları
        cols = st.columns([1] + [1]*len(self.tik_kolonlari))
        cols[0].markdown("**Müşteri Adı Soyadı**")
        for idx, kolon in enumerate(self.tik_kolonlari):
            cols[idx+1].markdown(f"**{kolon}**")

        st.markdown("---")
        databaseden_checkboxlari_cek = st.session_state["databasedeki_degerler"]
        # Her satır (sipariş) için
        for i, row in df.iterrows():

            musteri_adi_soyadi = row["musteri_adi_soyadi"]  # ← senin kolon ismine göre
            siparisno = row["siparis_numarasi"]

            row_cols = st.columns([1] + [1]*len(self.tik_kolonlari))

            # 1. kolon sipariş numarası
            row_cols[0].write(musteri_adi_soyadi)
            row_cols[0].write(siparisno)

            # 10 adet checkbox (yan yana)
            for idx, kolon in enumerate(self.tik_kolonlari):

                key_name = f"{kolon}_{siparisno}"  # benzersiz anahtar
                #liste.append([key_name, siparisno, kolon])


                if key_name not in st.session_state:
                    st.session_state[key_name] = (
                        databaseden_checkboxlari_cek
                        .get(siparisno, {})
                        .get(kolon, False)
                    )
            
                try:
                # Checkbox’u oluştur
                    row_cols[idx+1].checkbox(
                                                "",
                                            key=key_name,
                                            on_change=SIPARIS_DATAFRAME_DUZENLE.checkbox_degisti,
                                            args=(key_name, supabase)
                                            )
                except Exception as e:
                    pass
            st.write("---")
        #return liste


    
        

