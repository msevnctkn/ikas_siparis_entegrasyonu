
from main import *
import requests 
import pandas as pd
from sorgular import *
import time
from streamlit_init import *
from turkiye_tatiller import RESMI_TATILLER


class IKAS_SIPARIS_ENTEGRASYON():
    def __init__(self, client_id : str, client_secret : str, ):
      self.client_id = client_id
      self.client_secret = client_secret
      self.GRAPHQL_URL = "https://api.myikas.com/api/v1/admin/graphql"
      self.TOKEN_URL = "https://omas.myikas.com/api/admin/oauth/token"
      self.resmi_tatil = RESMI_TATILLER()


    def get_token(self):
      self.token_res = requests.post(
                        self.TOKEN_URL,
                        data={
                          "grant_type": "client_credentials",
                          "client_id": self.client_id,
                          "client_secret": self.client_secret
                          },
                        headers={"Content-Type": "application/x-www-form-urlencoded"})

      if self.token_res.status_code == 200:
         #st.write("TOKEN BAŞARIYLA ALINDI.")
         #st.write(self.token_res.text)
         return self.token_res.text
      
      elif self.token_res.status_code != 200:
          st.warning("Token alma hatası:", self.token_res.status_code)
          #st.write(self.token_res.text)
          exit()
          raise Exception
            



      
    def get_access_token(self):
      self.get_token()
      self.access_token = self.token_res.json()["access_token"]
      #st.write(self.access_token)
      return (self.access_token)

    def siparis_durumu_tr(self):
      self.siparis_durumu_dict = {"DELIVERED":"Teslim Edildi",
                                  "FULFILLED":"Kısmi Teslim Edildi",
                                  "CANCELLED":"İptal Edildi",
                                  "UNFULFILLED":"Oluşturuldu",
                                  "REFUNDED":"İade Edildi"}
      return self.siparis_durumu_dict



    def post_request(self, access_token):
      VARIABLES = {
                  "pagination": {
                      "page": 13,
                      "limit": 200
                  }
                }

      self.respond = requests.post(
          self.GRAPHQL_URL,
          json={"query": ORDER_QUERY, "variables":VARIABLES},
          headers={
              "Authorization": f"Bearer {access_token}",
              "Content-Type": "application/json"
          }
      )

      if self.respond.status_code == 200:
        #st.write("Respond Durum Kodu: ", self.respond.status_code)
        #st.write(self.respond.text)
        pass
      else:
        st.warning("Respond Durum Kodu:", self.respond.status_code)
        st.write("---")

      self.data = self.respond.json()
      has_next = self.data["data"]["listOrder"]["hasNext"] 
      page = self.data["data"]["listOrder"]["page"]
      count = self.data["data"]["listOrder"]["count"] #bugüne kadar alınan toplam sipariş sayısını temsil eder.
      orders = self.data.get("data", {}).get("listOrder", {}).get("data", [])
      return self.data
    
    def siparis_dataframe_hazirla(self, data):
      
      self.siparis_bilgileri = data["data"]["listOrder"]["data"]
      #oluşturuldu statüsünde bekleyen sipariş sayısı -> lazım olan cam sayısını bulmak için

      
      for content in self.siparis_bilgileri:
        #st.write(content)
        urun_bilgileri = []
        try:
          
          siparis_tarihi = (datetime.fromtimestamp(int(content["createdAt"])/1000)).date().strftime("%d.%m.%Y")
          siparis_numarasi = content["orderNumber"]
          notlar = content["note"]
          try:
            musteri_adi_soyadi = content["customer"]["fullName"] 
          except TypeError as e:
            musteri_adi_soyadi = " "
          #urun_adi = content["orderLineItems"][0]["variant"]["name"]
          #barcode_list = content["orderLineItems"][0]["variant"]["barcodeList"]
          itemCount = content["itemCount"] # müşterinin toplam sipariş ettiği ürün sayısı
          siparis_kanali = content["salesChannel"]["name"] #siparişin manuel mi yoksa siteden mi verildiğini söyler
          # omas = siteden kk ile ödendi
          # ADMIN = manuel
          
          for i in content["orderLineItems"]:
            barcodeList = i["variant"]["barcodeList"] # ürün barkodu
            urun_adi = i["variant"]["name"] #ürün ismi
            urun_bilgileri.append({"Ürün Barkodu": barcodeList,
                                    "Ürün Adı": urun_adi})

          #st.session_state["urun_bilgileri"].extend(urun_bilgileri)
          st.session_state["urun_bilgileri"].extend(urun_bilgileri)

          urun_barkodlari = [i["Ürün Barkodu"] for i in st.session_state["urun_bilgileri"]]
           
    
       
          siparis_durumu = content["orderLineItems"][0]["status"]
   
          imalat_bitis_suresi = self.resmi_tatil.is_gunu_ekle(tarih_str=siparis_tarihi, is_gunu=12)
          siparis_durumu = self.siparis_durumu_tr()[siparis_durumu]
          #st.write(st.session_state["urun_adi"])
          if siparis_numarasi not in st.session_state.get("eklenen_siparisler", 0):
            st.session_state["eklenen_siparisler"].add(siparis_numarasi)

            #Satüsü 'oluşturuldu' olarak bekleyen sipariş sayısı:
            # if siparis_durumu == "Oluşturuldu":
              
            #   if "65 CM" in urun_adi:
            #     st.session_state["olusturuldu_cam_sayisi_65"] += 1
            #     st.session_state["olusturuldu_ham_cerceve_sayisi_65"] += 1
              
          
            #   elif "60 CM" in urun_adi:
            #     st.session_state["olusturuldu_cam_sayisi_60"] += 1
            #     st.session_state["olusturuldu_ham_cerceve_sayisi_60"] += 1
         

            #   elif "40 CM" in urun_adi:
            #     st.session_state["olusturuldu_cam_sayisi_40"] += 1
            #     st.session_state["olusturuldu_ham_cerceve_sayisi_40"] += 1

              
            #   else:
            #     pass
                  #st.session_state["olusturuldu_cam_sayisi"] += 1



            if siparis_durumu != "Teslim Edildi" and siparis_durumu != "İptal Edildi" and siparis_durumu != "İade Edildi":
              
              st.session_state["rows"].append({
                "siparis_tarihi":siparis_tarihi,
                "siparis_numarasi": siparis_numarasi,
                "musteri_adi_soyadi":musteri_adi_soyadi,
                "urun_barkodu":urun_barkodlari,
                "toplam_urun_sayisi":itemCount,
                "notlar":notlar,
                "imalat_bitis_suresi":imalat_bitis_suresi,
                "siparis_durumu":siparis_durumu,     
                })

            else:
              st.session_state["deliveredRows"].append({
                  "siparis_tarihi":siparis_tarihi,
                  "siparis_numarasi": siparis_numarasi,
                  "musteri_adi_soyadi":musteri_adi_soyadi,
                  "urun_barkodu":urun_barkodlari,
                  "toplam_urun_sayisi":itemCount,
                  "notlar":notlar,
                  "imalat_bitis_suresi":imalat_bitis_suresi,
                  "siparis_durumu":siparis_durumu,
              })
          
          else:
            pass
            

        except Exception as e:
            st.write("Hata ile karşılaşıldı: ", e)
 
        
      #st.write("oluşturuldu olarak bekleyen cam sayısı", st.session_state["olusturuldu_cam_sayisi"])
      return st.session_state["rows"]
      

    def get_image_properties(self):
      self._data = self.post_request()
      self.list_product = self._data["data"]["listProduct"]["data"]
      self.imageId_list = []
      self.isMain_list = []
      self.order_list = []
      self.fileName_list = []


      for image_content in self.list_product:
        st.write(image_content)
        self.imageId = image_content["variants"][0]["images"][0]["imageId"]
        self.isMain = image_content["variants"][0]["images"][0]["isMain"]
        self.order = image_content["variants"][0]["images"][0]["order"]
        self.fileName = image_content["variants"][0]["images"][0]["fileName"]

        self.imageId_list.append(self.imageId)
        self.isMain_list.append(self.isMain)
        self.order_list.append(self.order)
        self.fileName_list.append(self.fileName)

        st.session_state["imageId"].append(self.imageId)
        st.session_state["imageId"] = list(set(st.session_state["imageId"]))        
  
        st.session_state["isMain"].append(self.isMain)
        st.session_state["isMain"] = list(set(st.session_state["isMain"]))

        st.session_state["order"].append(self.order)
        st.session_state["order"] = list(set(st.session_state["order"]))
        
        st.session_state["fileName"].append(self.fileName)
        st.session_state["fileName"] = list(set(st.session_state["fileName"]))

      #st.write("image id", st.session_state["imageId"])
      st.write(st.session_state["fileName"])
      return 0


    def get_image_url(self, image_id_list):
      image_urls = []
      for image_id in image_id_list:
        response = requests.post(
                              self.GRAPHQL_URL,
                              json={"query": IMAGE_QUERY, "variables": {"imageId": str(image_id)}},
                              headers={"Authorization": f"Bearer {self.access_token}",
                                       "Content-Type": "application/json"}
    )
        time.sleep(0.2)
        data = response.json()

        # Hata kontrolü
        if "errors" in data:
          st.write(f"{image_id} için hata:", data["errors"])
          image_urls.append(None)
          continue

        #url = data["data"]["getImageUploadUrl"]
        #image_urls.append(url)

      return data
