url = 'https://filestation.compass-software.de/FileManagement/DownloadLink?guid=b4082b52-778f-4be3-8710-6248f3b44f78'
# url = 'https://filestation.compass-software.de/FileManagement/DownloadLink?guid=b4082b52-778f-4be3-8710-6248f3b44f72'
# url = 'http://192.168.0.208:8096/web/index.html#!/item?id=25417&serverId=2f88a993e4414855a6b3ba4135101a79'
#url = 'https://filestation.compass-software.de/FileManagement/DownloadLink?guid=56018ed4-8e35-4a88-b4e1-f42f4ca8287a'
import os
import yaml
import download
import base

def read_config(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)



# run the base initialisation
config = base.run()
download.download_update(url, config['paths']['CompassUpdatePath'])


