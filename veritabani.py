from supabase import create_client
import streamlit as st
#supabase db şifre: omaskonsept

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]

def get_connection():
    db_password = "omaskonsept"
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
    result = supabase.table("siparis_takip").select("*").execute()
    return supabase, result



def checkbox_kontrol(supabase, siparis_no, kolon_adi, deger):
    supabase.table("siparis_takip") \
        .update({kolon_adi: deger}) \
        .eq("siparis_no", siparis_no) \
        .execute()



def checkbox_databaseden_veri_cek(supabase, siparis_no):
    response = (supabase
                .table("siparis_takip")
                .select("*")
                .eq("siparis_no",siparis_no)
                .execute()
                )
    
    if response.data:
        return response.data[0]
    return {}


def tum_checkboxlari_cek(supabase):
    response = supabase.table("siparis_takip") \
        .select("*") \
        .execute()

    sonuc = {}
    for row in response.data:
        sonuc[row["siparis_no"]] = row  # siparis_no → tüm kolonlar
    
    return sonuc



def databaseden_butun_verileri_cek(supabase, table_name:str ):
    data = supabase.table(table_name).select("*").execute()
    return data.data


def database_tekli_veri_yaz(supabase, table_name:str, kolon_adi, deger, ):
    data = supabase.table(table_name).upsert({kolon_adi:deger})
    return data




