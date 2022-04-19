from operator import itemgetter
from flask import jsonify, request

from models.lamanModels import Laman
from models.permintaanModels import Permintaan, PermintaanKesehatan
from models.transaksiModels import Transaksi
from application import auth

class LamanController:
  @staticmethod
  @auth.login_required
  def createLaman():
    try:
      idAutentikasi = request.form.get("id-autentikasi")

      dataPermintaan = Permintaan.getByIDPermintaan(idAutentikasi)
      dataAkun = auth.current_user()

      if dataPermintaan.getStatusAutentikasi() is None:
        return "Permintaan belum disetujui!", 400

      if dataPermintaan.getStatusAutentikasi() == 0:
        return "Permintaan tidak disetujui!", 400
      
      idPenggalang = dataAkun.getIDPengguna()
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

      Laman(idAutentikasi, idPenggalang, judul, deskripsi, target, kategori, deadline, foto)
      return "Created", 201

    except Exception as e:
      return str(e), 400

  @staticmethod
  @auth.login_required
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
  @auth.login_required
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
  @auth.login_required
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
  @auth.login_required
  def eksplorTotalDonasiLaman():
    # EKSPLOR BY TOTAL DONASI
    try:
      laman = Laman.getAll()

      if laman is None:
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

        return jsonify(sorted(result, key=itemgetter("total-donasi"), reverse=True)), 200

    except Exception as e:
      return str(e), 400

  @staticmethod
  @auth.login_required
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
  @auth.login_required
  def riwayatLaman():
    try:
      dataAkun = auth.current_user()
      idPenggalang = dataAkun.getIDPengguna()
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