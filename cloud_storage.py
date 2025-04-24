import os

from dotenv import load_dotenv
from google.cloud import storage

load_dotenv()

class CloudStorage:
    def __init__(self, bucket_name):
        self.bucket_name = bucket_name

        #inicializar cliente de Cloud Storage(para esto se debe setear la variable de entorno GOOGLE_APPLICATION_CREDENTIALS con la ruta del archivo JSON de las credenciales en windows se usa set GOOGLE_APPLICATION_CREDENTIALS=path\to\file.json en la terminal)
        #client = storage.Client()

        #cargar credenciales desde el archivo JSON
        self.client = storage.Client.from_service_account_json(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"))

        #obtener el bucket
        self.bucket = self.client.get_bucket(bucket_name)

    def list_files(self):
        blobs = list(self.bucket.list_blobs())
        # print("blobs: ", blobs)

        if not blobs:
            print("No hay archivos en el bucket.")
            return

        print(f"\n Archivos en el bucket {self.bucket_name}:")
        for b in blobs:
            print(f" - {b.name}")

        return
        # return [f" - {b.name}" for b in blobs]

    def upload_file(self, cloud_file_name, local_file_path):
        blob = self.bucket.blob(cloud_file_name) #crear referencia del archivo dentro del bucket
        blob.upload_from_filename(local_file_path) #subir archivo local y guardarlo en el bucket
        return "Archivo subido."

    def update_file(self, cloud_file_name, new_local_file_path ):
        blob = self.bucket.blob(cloud_file_name) #obtener referencia del archivo dentro del bucket
        blob.upload_from_filename(new_local_file_path) #actualizar con archivo local en el bucket
        return "Archivo actualizado."

    def delete_file(self, cloud_file_name):
        blob = self.bucket.blob(cloud_file_name)  #obtener referencia del archivo dentro del bucket
        blob.delete() #eliminar archivo del bucket
        return "Archivo eliminado."