from streamlit_init import *
init_states()
st.set_page_config(layout="wide")
import time

import pandas as pd
from main import *
from ikas_entegrasyon import IKAS_SIPARIS_ENTEGRASYON
from tikli_dataframe import SIPARIS_DATAFRAME_DUZENLE
from veritabani import *

CLIENT_ID = st.secrets["CLIENT_ID"]
CLIENT_SECRET = st.secrets["CLIENT_SECRET"]

st.header("ÖMAS KONSEPT SİPARİŞ TAKİP SİSTEMİ", divider=True, anchor="www.omaskonsept.com", )
sidebarButton = st.sidebar.selectbox("Menü", ["ikas Bekleyen Siparişler",
                                              "Teslim Edilen Siparişler (ikas)",
                                              "Malzeme/Ürün İstekleri",
                                              "Tamamlanan Siparişler",
                                              "Veritabanı"])


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

elif sidebarButton == "Malzeme/Ürün İstekleri":
    pass


elif sidebarButton == "Teslim Edilen Siparişler (ikas)":
    st.dataframe(st.session_state["deliveredRows"])


elif sidebarButton == "Veritabanı":
    pass
