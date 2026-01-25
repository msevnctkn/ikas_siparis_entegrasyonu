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

    session_state_rows_list = ["rows", "urun_adi_list"]
    session_state_teslim_edilen_siparisler_list = ["deliveredRows"]
    session_state_tik_list = ["tikList"]


    for key in session_state_rows_list:
        st.session_state.setdefault(key, [])


    for key in session_state_teslim_edilen_siparisler_list:
        st.session_state.setdefault(key, [])

    
    for key in session_state_tik_list:
        st.session_state.setdefault(key, [])
        


    # Oluşturuldu statüsünde bekleyen cam sayısı
    if "olusturuldu_cam_sayisi_65" not in st.session_state:
        st.session_state["olusturuldu_cam_sayisi_65"] = 0  

    if "olusturuldu_ham_cerceve_sayisi_65" not in st.session_state:
        st.session_state["olusturuldu_ham_cerceve_sayisi_65"] = 0

    ##########################################################

    if "olusturuldu_cam_sayisi_60" not in st.session_state:
        st.session_state["olusturuldu_cam_sayisi_60"] = 0  

    if "olusturuldu_ham_cerceve_sayisi_60" not in st.session_state:
        st.session_state["olusturuldu_ham_cerceve_sayisi_60"] = 0

    ##########################################################

    if "olusturuldu_cam_sayisi_40" not in st.session_state:
        st.session_state["olusturuldu_cam_sayisi_40"] = 0  

    if "olusturuldu_ham_cerceve_sayisi_40" not in st.session_state:
        st.session_state["olusturuldu_ham_cerceve_sayisi_40"] = 0

    ##########################################################


    #
    #       V   E   R   İ   T   A   B   A   N   I   
    #       Ç   E   K   İ   L   İ   Y   O   R   .
    #

    #VERİTABANINDA KAYITLI OLAN HER ŞEYİ ÇEKER.
    databasedeki_degerler = ["databasedeki_degerler"]

    for key in databasedeki_degerler:
        st.session_state.setdefault(key, {})




def anlik_stoklar_init():
    stoklar_session_state_list = ["stok_cam_kare_100",
                                  "stok_cam_kare_80",
                                  "stok_cam_kare_70",
                                  "stok_cam_kare_60",
                                  "stok_cam_kare_50",
                                  "stok_cam_kare_40",
                                  "stok_cam_kabe_tablosu",
                                  "stok_cam_65",
                                  "stok_cam_60",
                                  "stok_cam_40",
                                  "stok_ham_mdf_6mm",
                                  "stok_arkalik_3mm",
                                  "stok_ahsap_100",
                                  "stok_ahsap_80",
                                  "stok_pleksi_4_8mm",
                                  "stok_pleksi_2_8mm",
                                  "stok_seffaf_pleksi_2_8mm",
                                  "stok_altin_pleksi",
                                  "stok_krom_pleksi",
                                  "stok_ham_cerceve_65",
                                  "stok_ham_cerceve_60",
                                  "stok_ham_cerceve_40",
                                  "stok_krom_kaplama_cerceve_65",
                                  "stok_krom_kaplama_cerceve_60",
                                  "stok_krom_kaplama_cerceve_40",
                                  "stok_eskitme_cerceve_65",
                                  "stok_siyah_cerceve_65",
                                  "stok_haki_cerceve_65",
                                  "stok_bej_cerceve_65",
                                  "stok_antrasit_cerceve_65",
                                  "stok_eskitme_cerceve_60",
                                  "stok_siyah_cerceve_60",
                                  "stok_haki_cerceve_60",
                                  "stok_bej_cerceve_60",
                                  "stok_antrasit_cerceve_60",
                                  "stok_eskitme_cerceve_40",
                                  "stok_siyah_cerceve_40",
                                  "stok_haki_cerceve_40",
                                  "stok_bej_cerceve_40",
                                  "stok_antrasit_cerceve_40",
                                  "stok_beyaz_boya",
                                  "stok_siyah_boya",
                                  "stok_antrasit_boya",
                                  "stok_cerceve_siyah_boya",
                                  "stok_cerceve_antrasit_boya",
                                  "stok_cerceve_haki_boya",
                                  "stok_cerceve_bej_boya",
                                  "stok_altın_vernik",
                                  ]
    

    for key in stoklar_session_state_list:
        st.session_state.setdefault(key, 0)
        
    return stoklar_session_state_list