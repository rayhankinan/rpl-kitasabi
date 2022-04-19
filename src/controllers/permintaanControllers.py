from flask import jsonify, request
import bcrypt

from models.permintaanModels import PermintaanKesehatan, PermintaanLainnya
from application import userAuth, auditorAuth
from config.auditorConfig import AUDITOR_USERNAME, AUDITOR_HASHED_PASSWORD

class PermintaanController:
  @staticmethod
  @auditorAuth.verify_password
  def authenticate(username, password):
    if username == AUDITOR_USERNAME and bcrypt.checkpw(password.encode("utf-8"), AUDITOR_HASHED_PASSWORD):
      return True
    else:
      return False

  @staticmethod
  @userAuth.login_required
  def createPermintaanKesehatan():
    try:
      judul = request.form.get("judul")
      deskripsi = request.form.get("deskripsi")
      target = int(request.form.get("target"))
      fotoKTP = request.files.get("foto-ktp")
      fotoKK = request.files.get("foto-kk")
      fotoKetMedis = request.files.get("foto-ket-medis")
      fotoPemeriksaan = request.files.get("foto-pemeriksaan")
      tujuan = request.form.get("tujuan")
      namaPasien = request.form.get("nama-pasien")

      dataAkun = userAuth.current_user()
      idPengguna = dataAkun.getIDPengguna()

      # TODO : get IDPengguna
      PermintaanKesehatan(idPengguna, judul, deskripsi, target, fotoKTP, fotoKK, fotoKetMedis, fotoPemeriksaan, tujuan, namaPasien)
      return "Created", 201

    except Exception as e:
      return str(e), 400

  @staticmethod
  @userAuth.login_required
  def createPermintaanLainnya():
    try:
      judul = request.form.get("judul")
      deskripsi = request.form.get("deskripsi")
      target = int(request.form.get("target"))
      instansi = request.form.get("instansi")
      ig = request.form.get("akun-instagram")
      twt = request.form.get("akun-twitter")
      fb = request.form.get("akun-facebook")
      penerima = request.form.get("nama-penerima")

      dataAkun = userAuth.current_user()
      idPengguna = dataAkun.getIDPengguna()

      # TODO : get IDPengguna
      PermintaanLainnya(idPengguna, judul, deskripsi, target, instansi, ig, twt, fb, penerima)
      return "Created", 201

    except Exception as e:
      return str(e), 400

  @staticmethod
  @auditorAuth.login_required
  def editStatusPermintaanKesehatan():
    try:
      idPermintaanKesehatan = request.form.get("id-permintaan-kesehatan")
      statusAutentikasi = bool(request.form.get("status-autentikasi"))

      permintaanKesehatan = PermintaanKesehatan.getByIDPermintaanKesehatan(idPermintaanKesehatan)
      permintaanKesehatan.setStatusAutentikasi(statusAutentikasi)

      return "OK", 200

    except Exception as e:
      return str(e), 400

  @staticmethod
  @auditorAuth.login_required
  def editStatusPermintaanLainnya():
    try:
      idPermintaanLainnya = request.form.get("id-permintaan-lainnya")
      statusAutentikasi = bool(request.form.get("status-autentikasi"))

      permintaanLainnya = PermintaanLainnya.getByIDPermintaanLainnya(idPermintaanLainnya)
      permintaanLainnya.setStatusAutentikasi(statusAutentikasi)

      return "OK", 200

    except Exception as e:
      return str(e), 400

  @staticmethod
  @userAuth.login_required
  def riwayatPermintaan():
    try:
      dataAkun = userAuth.current_user()
      idPengguna = dataAkun.getIDPengguna()

      result = []
      riwayatKesehatan = PermintaanKesehatan.getByIDPengguna(idPengguna)
      riwayatLainnya = PermintaanLainnya.getByIDPengguna(idPengguna)

      if riwayatKesehatan is not None:
        for kes in riwayatKesehatan:
          result.append({
            "id-permintaan" : kes.getIDPermintaan(), 
            "id-pengguna": kes.getIDPengguna(), 
            "judul": kes.getJudul(), 
            "deskripsi": kes.getDeskripsi(), 
            "target": kes.getTarget(), 
            "status-autentikasi": kes.getStatusAutentikasi(), 
            "foto-ktp": kes.getFotoKTP(), 
            "foto-kk": kes.getFotoKK(), 
            "foto-ket-medis": kes.getFotoKetMedis(), 
            "foto-pemeriksaan": kes.getFotoPemeriksaan(), 
            "tujuan": kes.getTujuan(), 
            "nama-pasien": kes.getNamaPasien()
          })

      if riwayatLainnya is not None:
        for lain in riwayatLainnya:
          result.append({
            "id-permintaan" : lain.getIDPermintaan(), 
            "id-pengguna": lain.getIDPengguna(), 
            "judul": lain.getJudul(), 
            "deskripsi": lain.getDeskripsi(), 
            "target": lain.getTarget(), 
            "status-autentikasi": lain.getStatusAutentikasi(), 
            "instansi" : lain.getInstansi(), 
            "akun-instagram": lain.getAkunInstagram(), 
            "akun-twitter": lain.getAkunTwitter(), 
            "akun-facebook": lain.getAkunFacebook(), 
            "nama-penerima": lain.getNamaPenerima()
          })

      if riwayatKesehatan is None and riwayatLainnya is None:
        return "Not Found", 404

      else:
        return jsonify(result), 200

    except Exception as e:
      return str(e), 400


  @staticmethod
  @userAuth.login_required
  def detailPermintaan():
    try:
      idPermintaan = request.form.get("id-permintaan")

      riwayatKesehatan = PermintaanKesehatan.getByIDPermintaanKesehatan(idPermintaan)
      riwayatLainnya = PermintaanLainnya.getByIDPermintaanLainnya(idPermintaan)

      if riwayatKesehatan is not None:
        result = ({
            "id-permintaan" : riwayatKesehatan.getIDPermintaan(), 
            "id-pengguna": riwayatKesehatan.getIDPengguna(), 
            "judul": riwayatKesehatan.getJudul(), 
            "deskripsi": riwayatKesehatan.getDeskripsi(), 
            "target": riwayatKesehatan.getTarget(), 
            "status-autentikasi": riwayatKesehatan.getStatusAutentikasi(), 
            "foto-ktp": riwayatKesehatan.getFotoKTP(), 
            "foto-kk": riwayatKesehatan.getFotoKK(), 
            "foto-ket-medis": riwayatKesehatan.getFotoKetMedis(), 
            "foto-pemeriksaan": riwayatKesehatan.getFotoPemeriksaan(), 
            "tujuan": riwayatKesehatan.getTujuan(), 
            "nama-pasien": riwayatKesehatan.getNamaPasien(),
            "kategori": "Kesehatan"
          })

      else:
        result = ({
            "id-permintaan" : riwayatLainnya.getIDPermintaan(), 
            "id-pengguna": riwayatLainnya.getIDPengguna(), 
            "judul": riwayatLainnya.getJudul(), 
            "deskripsi": riwayatLainnya.getDeskripsi(), 
            "target": riwayatLainnya.getTarget(), 
            "status-autentikasi": riwayatLainnya.getStatusAutentikasi(), 
            "instansi" : riwayatLainnya.getInstansi(), 
            "akun-instagram": riwayatLainnya.getAkunInstagram(), 
            "akun-twitter": riwayatLainnya.getAkunTwitter(), 
            "akun-facebook": riwayatLainnya.getAkunFacebook(), 
            "nama-penerima": riwayatLainnya.getNamaPenerima(),
            "kategori": "Lainnya"
          })

      if riwayatKesehatan is None and riwayatLainnya is None:
        return "Not Found", 404

      else:
        return jsonify(result), 200

    except Exception as e:
      return str(e), 400
      