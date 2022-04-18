from flask import jsonify, request, session

from models.lamanModels import Laman
from models.permintaanModels import Permintaan, PermintaanKesehatan, PermintaanLainnya
from models.transaksiModels import Transaksi
import json
import sys

class LamanController:
  @staticmethod
  def createLaman():
    try:
      idAutentikasi = request.form.get("id-autentikasi")

      dataPermintaan = Permintaan.getByIDPermintaan(idAutentikasi)
      dataAkun = json.loads(session["User"])

      if (dataPermintaan.getStatusAutentikasi() == 0):
        return "Permintaan belum disetujui!", 400
      
      idPenggalang = int(dataAkun["ID"])
      judul =  dataPermintaan.getJudul()
      deskripsi = dataPermintaan.getDeskripsi()
      target = dataPermintaan.getTarget()
      deadline = request.form.get("deadline")
      foto = request.files.getlist("foto-laman")

      kes = PermintaanKesehatan.getByIDPermintaanKesehatan(idAutentikasi)

      if kes is None:
        kategori = "Lainnya"

      else:
        kategori = "Kesehatan"

      laman = Laman(idAutentikasi, idPenggalang, judul, deskripsi, target, kategori, deadline, foto)
      return "Created", 201

    except Exception as e:
      return str(e), 400

  @staticmethod
  def editLaman():
    try:
      idLaman = request.form.get("id-laman")
      laman = Laman.getByIDLaman(idLaman)
      foto = request.files.getlist("foto-laman")

      laman.setFoto(foto)

      return "OK", 200

    except Exception as e:
      return str(e), 400

  @staticmethod
  def searchlaman():
    # SEARCH BY JUDUL
    try:
      judul = request.form.get("query-judul")
      laman = Laman.getByJudul(judul)

      if laman is None:
        return "Not Found", 404
      else:
        result = []
        for l in laman:
          totalDonasi = Transaksi.getTotalByLaman(l.getIDLaman())
          result.append({"id-laman": l.getIDLaman(),
                        "id-autentikasi": l.getIDAutentikasi(),
                        "id-penggalang": l.getIDPenggalang(),
                        "judul": l.getJudul(),
                        "deskripsi": l.getDeskripsi(),
                        "target": l.getTarget(),
                        "total-donasi": totalDonasi,
                        "kategori": l.getKategori(),
                        "deadline": l.getDeadline(),
                        "timestamp": l.getTimestamp(),
                        "foto-laman": l.getFoto()})

        return jsonify(result), 200

    except Exception as e:
      return str(e), 400

  @staticmethod
  def eksplorKategoriLaman():
    # EKSPLOR BY KATEGORI
    try:
      kategori = request.form.get("query-kategory")
      laman = Laman.getByKategori(kategori)

      if laman is None:
        return "Not Found", 404
      else:
        result = []
        for l in laman:
          totalDonasi = Transaksi.getTotalByLaman(l.getIDLaman())
          result.append({"id-laman": l.getIDLaman(),
                        "id-autentikasi": l.getIDAutentikasi(),
                        "id-penggalang": l.getIDPenggalang(),
                        "judul": l.getJudul(),
                        "deskripsi": l.getDeskripsi(),
                        "target": l.getTarget(),
                        "total-donasi": totalDonasi,
                        "kategori": l.getKategori(),
                        "deadline": l.getDeadline(),
                        "timestamp": l.getTimestamp(),
                        "foto-laman": l.getFoto()})

        return jsonify(result), 200

    except Exception as e:
      return str(e), 400

  @staticmethod
  def eksplorTotalDonasiLaman():
    # EKSPLOR BY TOTAL DONASI
    try:
      laman = Laman.getByTotalDonasi()

      if (laman is None):
        return "Laman Not Found", 404
      else:
        result = []
        for l in laman:
          totalDonasi = Transaksi.getTotalByLaman(l.getIDLaman())
          result.append({"id-laman": l.getIDLaman(),
                        "id-autentikasi": l.getIDAutentikasi(),
                        "id-penggalang": l.getIDPenggalang(),
                        "judul": l.getJudul(),
                        "deskripsi": l.getDeskripsi(),
                        "target": l.getTarget(),
                        "total-donasi": totalDonasi,
                        "kategori": l.getKategori(),
                        "deadline": l.getDeadline(),
                        "timestamp": l.getTimestamp(),
                        "foto-laman": l.getFoto()})

        return jsonify(result), 200

    except Exception as e:
      return str(e), 400

  @staticmethod
  def detailLaman():
    # FIND BY IDLaman
    try:
      idLaman = request.form.get("id-laman")
      l = Laman.getByIDLaman(idLaman)
      totalDonasi = Transaksi.getTotalByLaman(idLaman)

      data = {"id-laman": l.getIDLaman(),
              "id-autentikasi": l.getIDAutentikasi(),
              "id-penggalang": l.getIDPenggalang(),
              "judul": l.getJudul(),
              "deskripsi": l.getDeskripsi(),
              "target": l.getTarget(),
              "total-donasi": totalDonasi,
              "kategori": l.getKategori(),
              "deadline": l.getDeadline(),
              "timestamp": l.getTimestamp(),
              "foto-laman": l.getFoto()}

      return jsonify(data),200

    except Exception as e:
      return str(e), 400

  @staticmethod
  def riwayatLaman():
    try:
      dataAkun = json.loads(session["User"])
      idPenggalang = int(dataAkun["ID"])
      laman = Laman.riwayatLaman(idPenggalang)

      if laman is None:
        return "Not Found", 404

      else:
        result = []
        for l in laman:
          totalDonasi = Transaksi.getTotalByLaman(l.getIDLaman())
          result.append({"id-laman": l.getIDLaman(),
                        "id-autentikasi": l.getIDAutentikasi(),
                        "id-penggalang": l.getIDPenggalang(),
                        "judul": l.getJudul(),
                        "deskripsi": l.getDeskripsi(),
                        "target": l.getTarget(),
                        "total-donasi": totalDonasi,
                        "kategori": l.getKategori(),
                        "deadline": l.getDeadline(),
                        "timestamp": l.getTimestamp(),
                        "foto-laman": l.getFoto()})

        return jsonify(result), 200

    except Exception as e:
      return str(e), 400