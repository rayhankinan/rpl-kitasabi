from flask import request, session
import json

from models.permintaanModels import Permintaan

class PermintaanController:
  @staticmethod
  def createPermintaanKesehatan():
    try:
      pass
    except Exception as e:
      return str(e), 400

  @staticmethod
  def createPermintaanLainnya():
    try:
      pass
    except Exception as e:
      return str(e), 400

  @staticmethod
  def setujuiPermintaan():
    pass

  @staticmethod
  def riwayat():
    pass

