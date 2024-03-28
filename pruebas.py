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
    use_wildcard=False,
)
remote_location = AzRemoteSASLocation(
    storage_account='arlandingstoragedesa',
    container="solicitudes-temis",
    blob_or_file = 'file',
    path="reportes",
    sas_token="sv=2022-11-02&ss=f&srt=sco&sp=rwdlc&se=2100-01-01T02:59:59Z&st=2024-01-16T20:13:42Z&spr=https&sig=LxaXIgF8M1jruy5clPv2l%2BRLUWZ6%2Bx9iBAgI75UP0sU%3D",
)

transfer_options = AzCopyOptions(
    recursive=True,
    # exclude_path=f"test2.jpg;test_data_4;test_data_3/test3.jpg",
    put_md5=True, )


az_client = AzClient()

azcp = az_client.copy(src=local_location, dest=remote_location, transfer_options=transfer_options)