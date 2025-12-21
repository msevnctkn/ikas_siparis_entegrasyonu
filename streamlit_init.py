import streamlit as st




def init_states():
    session_state_list = ["siparis_tarihi",
                      "siparis_numarasi",
                      "notlar",
                      "musteri_adi_soyadi",
                      "urun_adi",
                      "siparis_durumu",
                      "imalat_bitis_suresi",
                      "",
                      "imageId",
                      "isMain",
                      "order",
                      "fileName"
                      ]
    
    eklenen_siparisler = ["eklenen_siparisler"]
    #sipariş listesinin duplicate olmamasını sağlar.


    for key in session_state_list:
        st.session_state.setdefault(key, [])

    for key in eklenen_siparisler:
        st.session_state.setdefault(key, set())

    session_state_rows_list = ["rows"]
    session_state_teslim_edilen_siparisler_list = ["deliveredRows"]
    session_state_tik_list = ["tikList"]


    for key in session_state_rows_list:
        st.session_state.setdefault(key, [])


    for key in session_state_teslim_edilen_siparisler_list:
        st.session_state.setdefault(key, [])

    
    for key in session_state_tik_list:
        st.session_state.setdefault(key, [])
        
    ###########################################
    #
    #       V   E   R   İ   T   A   B   A   N   I   
    #       Ç   E   K   İ   L   İ   Y   O   R   .
    #

    #VERİTABANINDA KAYITLI OLAN HER ŞEYİ ÇEKER.
    databasedeki_degerler = ["databasedeki_degerler"]

    for key in databasedeki_degerler:
        st.session_state.setdefault(key, {})
