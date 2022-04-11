from google.cloud import storage

from config.gcloudConfig import BUCKET_NAME_IMAGE

storageClient = storage.Client()
imageBucket = storageClient.bucket(BUCKET_NAME_IMAGE)