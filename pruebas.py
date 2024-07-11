from azcp_wrapper.azcp_client import AzClient
from azcp_wrapper.azcp_utils import (
    AzRemoteSASLocation,
    AzLocalLocation,
    AzCopyOptions,
    AzSyncOptions,
)
import os

from dotenv import load_dotenv

load_dotenv()

local_location = AzLocalLocation(
    path="C:\\Users\\eabdala\\Desktop\\pruebasftp\\",
    use_wildcard=True,
)
remote_location = AzRemoteSASLocation(
    storage_account="sttemislowenv001",
    container="landing-temis",
    blob_or_file="blob",
    path="cfg_global",
    sas_token="sp=racwdlme&st=2024-04-24T03%3A00%3A01Z&se=2100-01-01T02%3A59%3A59Z&spr=https&sv=2022-11-02&sr=c&sig=O4%2FYD%2FGYaZA8rI3MKTxzS1YsV56HmZxY%2F5qIm8%2F71cA%3D",
)


transfer_options = AzCopyOptions(
    recursive=True,
    put_md5=None,
    overwrite=None,
)

print(str(transfer_options.get_options_list()))
az_client = AzClient(process_name="EL QUE ESTE POR CORRER")

# azcp = az_client.copy(src=local_location, dest=remote_location, transfer_options=transfer_options)
azcp = az_client.remove(src=remote_location, transfer_options=transfer_options)
print(str(azcp))


# import subprocess

# def install_package(package_name):
#     try:
#         # Ejecutar el comando de instalación de pip
#         subprocess.check_call(['C:\\Python3\\3.9.7\\python.exe','-m','pip', 'install', package_name])
#         print(f"El paquete '{package_name}' ha sido instalado correctamente.")
#     except subprocess.CalledProcessError as e:
#         print(f"Error al instalar el paquete '{package_name}': {e}")

# # Nombre del paquete que deseas instalar
# package_name = 'azcp-wrapper'
# install_package(package_name)
