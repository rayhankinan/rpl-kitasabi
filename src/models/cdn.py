from google.cloud import storage

from config.gcloudConfig import BUCKET_NAME_IMAGE

storageClient = storage.Client()
bucket = storageClient.bucket(BUCKET_NAME_IMAGE)