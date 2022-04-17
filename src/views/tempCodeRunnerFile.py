      # nominal penggalangan dana
      self.riwayatDonasiCard[i]["nominal"] = QLabel(self)
      self.riwayatDonasiCard[i]["nominal"].setText("Nominal")
      self.riwayatDonasiCard[i]["nominal"].setStyleSheet('color: rgba(37, 49, 60, 1)')
      self.riwayatDonasiCard[i]["nominal"].setStyleSheet('background-color: #F2F4F7')
      self.riwayatDonasiCard[i]["nominal"].move(425, 482 +i*185)
      self.riwayatDonasiCard[i]["nominal"].setFont(mulish24)
      # foto          
      url2 = 'https://yt3.ggpht.com/ytc/AKedOLQU2qqsQIYjE4SgWbHOYL4QkPO6dEXBcV8SnYEDig=s900-c-k-c0x00ffffff-no-rj'
      data2 = urllib.request.urlopen(url2).read()
      image2 = QImage()
      image2.loadFromData(data2)
      self.riwayatDonasiCard[i]["previewImg2"] = QLabel(self)
      self.riwayatDonasiCard[i]["previewImg2"].setFixedSize(117, 128)
      self.riwayatDonasiCard[i]["previewImg2"].move(269, 413 +i*185)
      self.riwayatDonasiCard[i]["previewImg2"].setScaledContents(True)
      pixmap2 = QPixmap(image2)
      self.riwayatDonasiCard[i]["previewImg2"].setPixmap(pixmap2)