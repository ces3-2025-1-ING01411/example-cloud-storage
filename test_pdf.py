import os
from cloud_storage import CloudStorage

# nombre del bucket
BUCKET_NAME = os.environ.get("BUCKET_NAME")

# ruta local
ASSETS_DIR = "assets"

test_cloud_storage = CloudStorage(BUCKET_NAME)

# #TODO: CREATE
# file_to_upload = os.path.join(ASSETS_DIR, "test_pdf.pdf")
# test_upload_file = test_cloud_storage.upload_file("test1/pdf_cloud.pdf", file_to_upload)
# print(test_upload_file)

# #TODO: UPDATE
# new_file = os.path.join(ASSETS_DIR, "new_pdf.pdf")
# test_update_file = test_cloud_storage.update_file("test1/pdf_cloud.pdf", new_file)
# print(test_update_file)

#TODO: LIST
test_list_files = test_cloud_storage.list_files()

# #TODO: DELETE
# test_delete_file = test_cloud_storage.delete_file("test1/pdf_cloud.pdf")
# print(test_delete_file)