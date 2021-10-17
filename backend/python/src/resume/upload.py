import os
import yaml
from azure.storage.blob import ContainerClient

def load_config():
    dir_root = os.path.dirname(os.path.abspath(__file__))
    with open(dir_root + "/config.yaml", "r") as yamlFile:
        return yaml.load(yamlFile, Loader=yaml.FullLoader)

def get_file(dir):
    with os.scandir(dir) as entries:
        for entry in entries:
            if entry.is_file() and not entry.name.startswith('.'):
                yield entry

def upload(files):
    connection_string = config['azure_storage_connectionstring']
    container_name=config['pictures_container_name']
    container_client = ContainerClient.from_connection_string(connection_string, container_name)
    print('Uploading files to blob storage...')
    for file in files:
        blob_client = container_client.get_blob_client(file.name)
        with open(file.path, "rb") as data:
            blob_client.upload_blob(data)
            print(f'{file.name} uploaded to blob storage')
            os.remove(file)
            print(f'{file.name} removed from folder')

config = load_config()
# pictures = get_file(config["source_folder"] + "/pictures")
# print(*pictures)