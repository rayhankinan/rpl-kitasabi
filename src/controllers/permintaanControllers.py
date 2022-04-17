from os import system
from flask import jsonify, request, session
import sys
import json

from models.permintaanModels import PermintaanKesehatan, PermintaanLainnya

class PermintaanController:
  @staticmethod
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

      dataAkun = json.loads(session["User"])
      idPengguna = int(dataAkun["ID"])

      # TODO : get IDPengguna
      permintaanKesehatan = PermintaanKesehatan(idPengguna, judul, deskripsi, target, fotoKTP, fotoKK, fotoKetMedis, fotoPemeriksaan, tujuan, namaPasien)
      return "Permintaan Kesehatan Created", 201

    except Exception as e:
      return str(e), 400

  @staticmethod
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

      dataAkun = json.loads(session["User"])
      idPengguna = int(dataAkun["ID"])

      # TODO : get IDPengguna
      permintaanLainnya = PermintaanLainnya(idPengguna, judul, deskripsi, target, instansi, ig, twt, fb, penerima)
      return "Permintaan Lainnya Created", 201

    except Exception as e:
      return str(e), 400

  @staticmethod
  def setujuiPermintaanKesehatan():
    try:
      idPermintaanKesehatan = request.form.get("id-permintaan-kesehatan")
      permintaanKesehatan = PermintaanKesehatan.getByIDPermintaanKesehatan(idPermintaanKesehatan)
      permintaanKesehatan.setStatusAutentikasi(True)

      return "Permintaan Kesehatan Approved", 201
    except Exception as e:
      return str(e), 400

  @staticmethod
  def setujuiPermintaanLainnya():
    try:
      idPermintaanLainnya = request.form.get("id-permintaan-lainnya")
      permintaanLainnya = PermintaanLainnya.getByIDPermintaanLainnya(idPermintaanLainnya)
      permintaanLainnya.setStatusAutentikasi(True)

      return "Permintaan Kesehatan Approved", 201
    except Exception as e:
      return str(e), 400

  @staticmethod
  def riwayatPermintaan():
    try:
      dataAkun = json.loads(session["User"])
      idPengguna = int(dataAkun["ID"])

      result = []
      riwayatKesehatan = PermintaanKesehatan.getByIDPengguna(idPengguna)
      riwayatLainnya = PermintaanLainnya.getByIDPengguna(idPengguna)

      if (riwayatKesehatan is not None):
        for kes in riwayatKesehatan:
          result.append({"id-permintaan" : kes.getIDPermintaan(), "id-pengguna": kes.getIDPengguna(), "judul": kes.getJudul(), "deskripsi": kes.getDeskripsi(), "target": kes.getTarget(), "status-autentikasi": kes.getStatusAutentikasi(), "foto-ktp": kes.getFotoKTP(), "foto-kk": kes.getFotoKK(), "foto-ket-medis": kes.getFotoKetMedis(), "foto-pemeriksaan": kes.getFotoPemeriksaan(), "tujuan": kes.getTujuan(), "nama-pasien": kes.getNamaPasien()})

      if (riwayatLainnya is not None):
        for lain in riwayatLainnya:
          result.append({"id-permintaan" : lain.getIDPermintaan(), "id-pengguna": lain.getIDPengguna(), "judul": lain.getJudul(), "deskripsi": lain.getDeskripsi(), "target": lain.getTarget(), "status-autentikasi": lain.getStatusAutentikasi(), "instansi" : lain.getInstansi(), "akun-instagram": lain.getAkunInstagram(), "akun-twitter": lain.getAkunTwitter(), "akun-facebook": lain.getAkunFacebook(), "nama-penerima": lain.getNamaPenerima()})

      if (riwayatKesehatan == None and riwayatLainnya == None):
        return jsonify({}), 200
      else:
        return jsonify(result), 200

    except Exception as e:
      return str(e), 400

