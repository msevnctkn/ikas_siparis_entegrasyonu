#imalatın istediği 
from main import *

def HAM_MADDE_STOKLARI():
    olusturuldu_cam_sayisi_65 = st.session_state["olusturuldu_cam_sayisi_65"]
    olusturuldu_cam_sayisi_60 = st.session_state["olusturuldu_cam_sayisi_60"]
    olusturuldu_cam_sayisi_40 = st.session_state["olusturuldu_cam_sayisi_40"]

    olusturuldu_ham_cerceve_sayisi_65 = st.session_state["olusturuldu_ham_cerceve_sayisi_65"]
    olusturuldu_ham_cerceve_sayisi_60 = st.session_state["olusturuldu_ham_cerceve_sayisi_60"]
    olusturuldu_ham_cerceve_sayisi_40 = st.session_state["olusturuldu_ham_cerceve_sayisi_40"]
    

    with st.expander("CAM STOKLARI", False):
        col1, col2, col3, col4 = st.columns(4)

        with col1:
            with st.container(border=True):
                st.markdown("Kare Camlar")
            with st.container(border=True):

                stok_cam_kare_100 = st.number_input("100 CM KARE CAM SAYISI", value=0, step=1)
                stok_cam_kare_80 = st.number_input("80 CM KARE STOK CAM SAYISI", value=0, step=1) 
                stok_cam_kare_70 = st.number_input("70 CM KARE STOK CAM SAYISI", value=0, step=1)
                stok_cam_kare_60 = st.number_input("60 CM KARE STOK CAM SAYISI", value=0, step=1)
                stok_cam_kare_50 = st.number_input("50 CM KARE STOK CAM SAYISI", value=0, step=1)
                stok_cam_kare_40 = st.number_input("40 CM KARE STOK CAM SAYISI", value=0, step=1)
                stok_cam_kabe_tablosu = st.number_input("KABE TABLOSU STOK CAM SAAYISI", value=0, step=1)
            
            #
            # VERİTABANI SESSION STATE KAYITLARI
            st.session_state["stok_cam_kare_100"] = stok_cam_kare_100
            st.session_state["stok_cam_kare_80"] = stok_cam_kare_80
            st.session_state["stok_cam_kare_70"] = stok_cam_kare_70
            st.session_state["stok_cam_kare_60"] = stok_cam_kare_60
            st.session_state["stok_cam_kare_50"] = stok_cam_kare_50
            st.session_state["stok_cam_kare_40"] = stok_cam_kare_40
            st.session_state["stok_cam_kabe_tablosu"] = stok_cam_kabe_tablosu
        
        with col2:
            with st.container(border=True):
                st.markdown("Yuvarlak Camlar")
            with st.container(border=True):
                stok_cam_65 = st.number_input("65 CM STOK YUVARLAK CAM SAYISI", value=0, step=1)
                stok_cam_60 = st.number_input("60 CM STOK YUVARLAK CAM SAYISI", value=0, step=1)
                stok_cam_40 = st.number_input("40 CM STOK YUVARLAK CAM SAYISI", value=0, step=1)
                

                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_cam_65"] = stok_cam_65
                st.session_state["stok_cam_60"] = stok_cam_60
                st.session_state["stok_cam_40"] = stok_cam_40


    
    with st.expander("MDF, AHŞAP VE PLEKSİ STOKLARI", False):
        stok_mdf_pleksi_col1, stok_mdf_pleksi_col2, stok_mdf_pleksi_col3 = st.columns(3)
        with stok_mdf_pleksi_col1:
            with st.container(border=True):
                st.markdown("MDFLER")
            with st.container(border=True):
                stok_ham_mdf_6mm = st.number_input("6 MM HAM MDF SAYISI", value=0)
                stok_arkalik_3mm = st.number_input("3 MM ARKALIK SAYISI", value=0 )


                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_ham_mdf_6mm"] = stok_ham_mdf_6mm
                st.session_state["stok_arkalik_3mm"] = stok_arkalik_3mm


        with stok_mdf_pleksi_col2:
            with st.container(border=True):
                st.markdown("AHŞAPLAR")
            with st.container(border=True):

                stok_ahsap_100 = st.number_input("100 CM KARE SAAT İÇİN ARKA AHŞAP SAYISI", value=0)
                stok_ahsap_80 = st.number_input("80 CM KARE SAAT İÇİN ARKA AHŞAP SAYISI", value=0 )

                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_ahsap_100"] = stok_ahsap_100
                st.session_state["stok_ahsap_80"] = stok_ahsap_80


        with stok_mdf_pleksi_col3:
            with st.container(border=True):
                st.markdown("PLEKSİLER")
            with st.container(border=True):

                stok_pleksi_4_8mm = st.number_input("4.8 MM SİYAH PLEKSİ SAYISI")
                stok_pleksi_2_8mm = st.number_input("2.8 MM SİYAH PLEKSİ SAYISI")
                stok_seffaf_pleksi_2_8mm = st.number_input("2.8 MM ŞEFFAF PLEKSİ SAYISI")
                stok_altin_pleksi = st.number_input("0.8 MM ALTIN PLEKSİ SAYISI")
                stok_krom_pleksi = st.number_input("0.8 MM KROM PLEKSİ SAYISI")


                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_pleksi_4_8mm"] = stok_pleksi_4_8mm
                st.session_state["stok_pleksi_2_8mm"] = stok_pleksi_2_8mm
                st.session_state["stok_seffaf_pleksi_2_8mm"] = stok_seffaf_pleksi_2_8mm
                st.session_state["stok_altin_pleksi"] = stok_altin_pleksi
                st.session_state["stok_krom_pleksi"] = stok_krom_pleksi



    with st.expander("ÇERÇEVE STOKLARI", False):
        stok_cerceve_col1, stok_cerceve_col2, stok_cerceve_col3 = st.columns(3)
        with stok_cerceve_col1:
            with st.container(border=True):
                st.markdown("Ham Çerçeveler")
            with st.container(border=True):


                stok_ham_cerceve_65 = st.number_input("65 CM STOK HAM ÇERÇEVE SAYISI", value=0, step=1)
                stok_ham_cerceve_60 = st.number_input("60 CM STOK HAM ÇERÇEVE SAYISI", value=0, step=1)
                stok_ham_cerceve_40 = st.number_input("40 CM STOK HAM ÇERÇEVE SAYISI", value=0, step=1)


                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_ham_cerceve_65"] = stok_ham_cerceve_65
                st.session_state["stok_ham_cerceve_60"] = stok_ham_cerceve_60
                st.session_state["stok_ham_cerceve_40"] = stok_ham_cerceve_40

        
        with stok_cerceve_col2:
            with st.container(border=True):
                st.markdown("Krom Kaplama")
            with st.container(border=True):

                stok_krom_kaplama_cerceve_65 = st.number_input("65 CM STOK KROM KAPLAMA ÇERÇEVE SAYISI", value=0, step=1)
                stok_krom_kaplama_cerceve_60 = st.number_input("60 CM STOK KROM KAPLAMA ÇERÇEVE SAYISI", value=0, step=1)
                stok_krom_kaplama_cerceve_40 = st.number_input("40 CM STOK KROM KAPLAMA ÇERÇEVE SAYISI", value=0, step=1)
            
                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_krom_kaplama_cerceve_65"] = stok_krom_kaplama_cerceve_65
                st.session_state["stok_krom_kaplama_cerceve_60"] = stok_krom_kaplama_cerceve_60
                st.session_state["stok_krom_kaplama_cerceve_40"] = stok_krom_kaplama_cerceve_40        




    with st.expander("BOYANMIŞ ÇERÇEVE STOKLARI", False):
        stok_boyanmis_cerceve_col1, stok_boyanmis_cerceve_col2, stok_boyanmis_cerceve_col3 = st.columns(3)
        with stok_boyanmis_cerceve_col1:
            with st.container(border=True):
                st.markdown("65 CM Boyanmış Çerçeveler")
            with st.container(border=True):
                stok_eskitme_cerceve_65 = st.number_input("65 CM ESKİTME ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_siyah_cerceve_65 = st.number_input("65 CM SİYAH ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_haki_cerceve_65 = st.number_input("65 CM HAKİ ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_bej_cerceve_65 = st.number_input("65 CM BEJ ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_antrasit_cerceve_65 = st.number_input("65 CM ANTRASİT ÇERÇEVE STOK SAYISI", value=0, step=1)

                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_eskitme_cerceve_65"] = stok_eskitme_cerceve_65
                st.session_state["stok_siyah_cerceve_65"] = stok_siyah_cerceve_65
                st.session_state["stok_haki_cerceve_65"] = stok_haki_cerceve_65    
                st.session_state["stok_bej_cerceve_65"] = stok_bej_cerceve_65  
                st.session_state["stok_antrasit_cerceve_65"] = stok_antrasit_cerceve_65  



        with stok_boyanmis_cerceve_col2:
            with st.container(border=True):
                st.markdown("60 CM Boyanmış Çerçeveler")
            with st.container(border=True):
                stok_eskitme_cerceve_60 = st.number_input("60 CM ESKİTME ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_siyah_cerceve_60 = st.number_input("60 CM SİYAH ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_haki_cerceve_60 = st.number_input("60 CM HAKİ ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_bej_cerceve_60 = st.number_input("60 CM BEJ ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_antrasit_cerceve_60 = st.number_input("60 CM ANTRASİT ÇERÇEVE STOK SAYISI", value=0, step=1)

                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_eskitme_cerceve_60"] = stok_eskitme_cerceve_60
                st.session_state["stok_siyah_cerceve_60"] = stok_siyah_cerceve_60
                st.session_state["stok_haki_cerceve_60"] = stok_haki_cerceve_60    
                st.session_state["stok_bej_cerceve_60"] = stok_bej_cerceve_60  
                st.session_state["stok_antrasit_cerceve_60"] = stok_antrasit_cerceve_60  





        with stok_boyanmis_cerceve_col3:
            with st.container(border=True):
                st.markdown("40 CM Boyanmış Çerçeveler")
            with st.container(border=True):
                stok_eskitme_cerceve_40 = st.number_input("40 CM ESKİTME ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_siyah_cerceve_40 = st.number_input("40 CM SİYAH ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_haki_cerceve_40 = st.number_input("40 CM HAKİ ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_bej_cerceve_40 = st.number_input("40 CM BEJ ÇERÇEVE STOK SAYISI", value=0, step=1)
                stok_antrasit_cerceve_40 = st.number_input("40 CM ANTRASİT ÇERÇEVE STOK SAYISI", value=0, step=1)

                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_eskitme_cerceve_40"] = stok_eskitme_cerceve_40
                st.session_state["stok_siyah_cerceve_40"] = stok_siyah_cerceve_40
                st.session_state["stok_haki_cerceve_40"] = stok_haki_cerceve_40    
                st.session_state["stok_bej_cerceve_40"] = stok_bej_cerceve_40  
                st.session_state["stok_antrasit_cerceve_40"] = stok_antrasit_cerceve_40  


    with st.expander("BOYA STOKLARI", False):
        stok_boya_col1, stok_boya_col2, stok_boya_col3, stok_boya_col4 = st.columns(4)
        with stok_boya_col1:
            with st.container(border=True):
                st.markdown("MDF BOYALARI")
            with st.container(height=500, border=True):
                stok_beyaz_boya = st.number_input("BEYAZ BOYA STOKU (KG)")
                stok_siyah_boya = st.number_input("SİYAH BOYA STOKU (KG)")
                stok_antrasit_boya = st.number_input("ANTRASİT BOYA STOKU (KG)")       

                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_beyaz_boya"] = stok_beyaz_boya
                st.session_state["stok_siyah_boya"] = stok_siyah_boya
                st.session_state["stok_antrasit_boya"] = stok_antrasit_boya    


        with stok_boya_col2:
            with st.container(border=True):
                st.markdown("ÇERÇEVE BOYALARI")
            with st.container(border=True):
                stok_cerceve_siyah_boya = st.number_input("SİYAH ÇERÇEVE BOYASI STOKU (KG)")
                stok_cerceve_antrasit_boya = st.number_input("ANTRASİT ÇERÇEVE BOYASI STOKU (KG)")
                stok_cerceve_haki_boya = st.number_input("HAKİ ÇERÇEVE BOYASI STOKU (KG)")
                stok_cerceve_bej_boya = st.number_input("BEJ ÇERÇEVE BOYASI STOKU (KG)")

                #
                # VERİTABANI SESSION STATE KAYITLARI
                st.session_state["stok_cerceve_siyah_boya"] = stok_cerceve_siyah_boya
                st.session_state["stok_cerceve_antrasit_boya"] = stok_cerceve_antrasit_boya
                st.session_state["stok_cerceve_haki_boya"] = stok_cerceve_haki_boya    
                st.session_state["stok_cerceve_bej_boya"] = stok_cerceve_bej_boya  

            with st.container(border=True):
                stok_altın_vernik = st.number_input("ALTIN VERNİK ÇERÇEVE BOYASI STOKU (KG)")
                st.session_state["stok_altın_vernik"] = stok_altın_vernik
               
    with st.expander("ELEKTRONİK MALZEME STOKLARI", False):
        elektronik_col1, elektronik_col2, elektronik_col3 = st.columns(3)
        with elektronik_col1:
            #elektronik malzemeleri gir
            a = st.number_input("sayı gir")


            st.metric("Arduino adedi", 5, f"{a} adet ihtiyaç var.", delta_color="normal")
        with elektronik_col2:
            st.metric("Esp 32 adedi", 6, "q")
        with elektronik_col3:
            st.metric("Pil", 4, "q")

    
    gereken_malzemeler_expander = st.expander("SİPARİŞ LİSTESİNDEKİ BÜTÜN SİPARİŞLERİ ÇIKARMAK İÇİN GEREKLİ OLAN MALZEME SAYILARINI GÖSTERİR.", False)
    with gereken_malzemeler_expander:
        #ham_madde_stoklar_expander = st.expander("HAM MADDE STOKLARI", True)

        gereken_malzemeler_col1, gereken_malzemeler_col2, gereken_malzemeler_col3, gereken_malzemeler_col4= st.columns(4)
        with gereken_malzemeler_col1:
            with st.container(border=True):
                st.metric("65 CM YUVARLAK CAM", 0,"YETERLİ STOK")

            with st.container(border=True):
                st.metric("60 CM YUVARLAK CAM", 0,"YETERLİ STOK")

            with st.container(border=True):    
                st.metric("40 CM YUVARLAK CAM", 0,"YETERLİ STOK")

        with gereken_malzemeler_col2:
            with st.container(border=True):
                st.metric("GEREKEN HAM ÇERÇEVE 65 CM",0 ,"YETERLİ STOK")

            with st.container(border=True):
                st.metric("GEREKEN HAM ÇERÇEVE 60 CM", 0,"YETERLİ STOK")

            with st.container(border=True):
                st.metric("GEREKEN HAM ÇERÇEVE 40 CM", 0,"YETERLİ STOK")

        
        with gereken_malzemeler_col3:
            with st.container(border=True):
                st.metric("GEREKEN 6 MM HAM MDF SAYISI", "Boş","YETERLİ STOK")

            with st.container(border=True):
                st.metric("GEREKEN 3 MM SİYAH ARKALIK SAYISI", "Boş","YETERLİ STOK")

            with st.container(border=True):
                st.metric("GEREKEN 4.8 MM SİYAH PLEKSİ SAYISI", "Boş","YETERLİ STOK")

            with st.container(border=True):
                st.metric("GEREKEN 2.8 MM SİYAH PLEKSİ SAYISI", "Boş","YETERLİ STOK")

            with st.container(border=True):
                st.metric("GEREKEN 2.8 MM ŞEFFAF PLEKSİ SAYISI", "Boş","YETERLİ STOK")

            with st.container(border=True):
                st.metric("GEREKEN 0.8 MM ALTIN PLEKSİ SAYISI", "Boş", "YETERLİ STOK")

            with st.container(border=True):
                st.metric("GEREKEN 0.8 MM KROM PLEKSİ SAYISI", "Boş", "YETERLİ STOK")
            
        with gereken_malzemeler_col4:
            with st.container(border=True):
                st.metric("GEREKEN ARDUINO SAYISI", "Boş","YETERLİ STOK")

            with st.container(border=True):    
                st.metric("GEREKEN ESP32 SAYISI", "Boş","YETERLİ STOK")

            with st.container(border=True):
                st.metric("GEREKEN PİL SAYISI", "Boş","YETERLİ STOK")



    


    with st.expander("SİPARİŞ LİSTESİNDEKİ ÜRÜNLERİ HAZIRLAYABİLMEK İÇİN GEREKLİ OLAN MALZEME LİSTESİ", False):
        
        st.write("Ham Çerçeve Sayısı 60", olusturuldu_ham_cerceve_sayisi_60)
        st.write("Ham Çerçeve Sayısı 40", olusturuldu_ham_cerceve_sayisi_40)


