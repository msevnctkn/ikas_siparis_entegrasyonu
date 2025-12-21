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




def kaydet(supabase, siparis_numarasi, checkbox_unique_isim):
    
    supabase.table("siparis_takip").upsert({"siparis_no":siparis_numarasi, 
                                                "mdf_kesildi":checkbox_unique_isim}).execute()





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