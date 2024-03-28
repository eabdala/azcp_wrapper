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
    container="landing-temis",
    blob_or_file = 'blob',
    path="cdrs",
    sas_token="sp=racwdlme&st=2023-12-06T18:20:20Z&se=2100-01-01T02:20:20Z&spr=https&sv=2022-11-02&sr=c&sig=5POkIL6W3pVjslA26mbW%2BZYTr4SoPrs4VhCLIf9YKdM%3D",
)

transfer_options = AzCopyOptions(
    recursive=True,
    # exclude_path=f"test2.jpg;test_data_4;test_data_3/test3.jpg",
    put_md5=True, )


az_client = AzClient(process_name='EL QUE ESTE POR CORRER')

azcp = az_client.copy(src=local_location, dest=remote_location, transfer_options=transfer_options)
