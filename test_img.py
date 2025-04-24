import os
from cloud_storage import CloudStorage

# nombre del bucket
BUCKET_NAME = os.environ.get("BUCKET_NAME")

# ruta local
ASSETS_DIR = "assets"

test_cloud_storage = CloudStorage(BUCKET_NAME)

# #TODO: CREATE
# file_to_upload = os.path.join(ASSETS_DIR, "image.png")
# test_upload_file = test_cloud_storage.upload_file("image_cloud.png", file_to_upload)
# print(test_upload_file)

# #TODO: UPDATE
# new_file = os.path.join(ASSETS_DIR, "new_image.png")
# test_update_file = test_cloud_storage.update_file("image_cloud.png", new_file)
# print(test_update_file)

#TODO: LIST
test_list_files = test_cloud_storage.list_files()

# #TODO: DELETE
# test_delete_file = test_cloud_storage.delete_file("image_cloud.png")
# print(test_delete_file)



# 1. listar archivos
# print(f"\n Archivos en el bucket: {BUCKET_NAME}")
# blobs = bucket.list_blobs()
# for b in blobs:
#     print(f" - {b.name}")

# # ruta local
# ASSETS_DIR = "assets"

# # 2. subir un archivo
# file_to_upload = os.path.join(ASSETS_DIR, "image.png")
# blob = bucket.blob("image_cloud.png") # crear referencia del archivo dentro del bucket
# blob.upload_from_filename(file_to_upload) # subir archivo local y guardarlo en el bucket
# print("Archivo subido.")

# # 3. actualizar un archivo
# new_file = os.path.join(ASSETS_DIR, "new_image.png")
# blob = bucket.blob("image_cloud.png")
# blob.upload_from_filename(new_file)
# print("Archivo actualizado")

# # 4. eliminar un archivo
# blob = bucket.blob("image_cloud.png")
# blob.delete()
# print("Archivo eliminado.")