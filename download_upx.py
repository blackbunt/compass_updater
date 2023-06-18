# this small program downloads the latest upx.exe from the official website for windows x64
# and places it in the same folder as the script
#

import os
import shutil
import zipfile

import requests
import re
import tqdm


def get_version():
    '''
    returns the latest upx version from the official website, without downloading the file
    :return: latest upx version from the official website (str) -> '3.96'
    :return: download link for the latest upx.exe (str) -> 'https://........'
    :return: filename of the latest upx.exe (str) -> 'upx-3.96-win64.zip'
    '''
    # get the latest upx.exe from the official website
    url = 'https://github.com/upx/upx/releases/latest/'
    r = requests.get(url)
    if r.status_code != 200:
        print('Error while getting latest upx.exe, please check your internet connection.')
        print('Script will be terminated.')
        os.system('pause')
        exit(1)
    # speichert den html code der website in der variable html
    html = r.content
    # extract the download link for the latest windows x64 version with regex
    regex_link = r'href="(.+?.win64.zip)"'
    regex_version = r'v(\d+\.\d+\.\d+)'
    regex_filename = r'\/([^\/]+)$'

    # speichert den link in der variable download_link
    download_link = re.findall(regex_link, html.decode('utf-8'))[0]
    upx_version = re.findall(regex_version, download_link)[0]
    upx_filename = re.findall(regex_filename, download_link)[0]

    return upx_version, download_link, upx_filename


def download_upx(dl_url: str, dl_filename: str):
    '''
    downloads upx.exe from the official website
    :param dl_url: download link for the latest upx release zip
    :param dl_filename: filename of the latest upx release zip
    :return: bool if download was successful -> True
    '''
    # check if upx_filename is already in the current directory and ask user if he wants to overwrite it
    if os.path.isfile(dl_filename):
        print(f'{dl_filename} already exists in current directory.')
        print('Do you want to overwrite it? (y/n)')
        user_input = input()
        if user_input == 'y':
            # print(f'Overwriting {upx_filename}...')
            pass
        else:
            return False
    # use tqdm to show a progress bar while downloading
    with tqdm.tqdm(unit='MB', unit_scale=True, unit_divisor=1024, miniters=1, desc=f'Downloading {dl_filename}') as t:
        r = requests.get(dl_url, stream=True)
        with open(dl_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)
                    t.update(len(chunk))
    return True


def check_for_upx_version(version: str):
    '''
    checks if upx.exe is up-to-date
    checks if upx.exe exists in the current directory
    if it exists, check the version
    if it does not exist, the script returns False
    :param version: latest upx version from the official website
    :return: bool if upx.exe is up-to-date -> True
    '''

    # search for a file called upx.exe in the current directory
    # if it exists, check the version
    # if it does not exist, the script returns False
    if os.path.isfile('upx.exe'):
        # Get the version of the current upx.exe
        current_upx_version = os.popen('upx.exe --version').read().strip()
        version_match = re.findall(r"upx (\d+\.\d+\.\d+)", current_upx_version)
        if version_match[0] == version:
            print(f'Current upx.exe version: {version}')
            print('upx.exe is up-to-date.')
            return True
        else:
            print("Error while reading version from UPX.exe")
            os.system('pause')
    else:
        return False


def extract_upx(filename_zip: str, version: str):
    '''
    extract upx.exe from the zip file
    :return: bool if extraction was successful -> True
    '''
    # Aktuelles Verzeichnis erhalten
    aktuelles_verzeichnis = os.path.dirname(os.path.abspath(__file__))

    # Name des Ordners, der entpackt werden soll
    foldername = os.path.splitext(filename_zip)[0]

    # ZIP-Datei öffnen
    zip_ref = zipfile.ZipFile(filename_zip, 'r')

    # Extrahiere die Datei "upx.exe" aus dem angegebenen Ordner
    zip_member = f"{foldername}/upx.exe"

    # Fortschrittsgröße erhalten
    zip_size = zip_ref.getinfo(zip_member).file_size

    # Extraktionsziel für die Datei "upx.exe"
    zielverzeichnis = aktuelles_verzeichnis

    # use tqdm to show a progress bar while extracting, with the size of the zip file in mb
    with tqdm.tqdm(unit='MB', unit_scale=True, unit_divisor=1024, miniters=1, desc=f'Extracting {filename_zip}', total=zip_size) as t:
        # Extrahiere die Datei "upx.exe" aus dem angegebenen Ordner
        zip_ref.extract(zip_member, zielverzeichnis)
        t.update(zip_size)

    # ZIP-Datei schließen
    zip_ref.close()

    # move upx.exe to the current directory
    os.rename(f'{foldername}/upx.exe', 'upx.exe')

    # get the version of the current upx.exe
    current_upx_version = os.popen('upx.exe --version').read().strip()
    version_match = re.findall(r"upx (\d+\.\d+\.\d+)", current_upx_version)
    if version_match[0] == version:
        print(f'Current upx.exe version: {version}')

    else:
        print("Error while reading version from UPX.exe")
        os.system('pause')
        return False

    # delete the folder from the current directory
    shutil.rmtree(foldername)
    # check if the folder still exists
    if os.path.isdir(foldername):
        print(f'Error while deleting {foldername}')
        os.system('pause')
        return False
    # delete the zip file
    os.remove(filename_zip)
    # check if the zip file still exists
    if os.path.isfile(filename_zip):
        print(f'Error while deleting {filename_zip}')
        os.system('pause')
        return False
    return True




if __name__ == '__main__':
    upx_version, download_link, upx_filename = get_version()
    if not check_for_upx_version(upx_version):
        download_upx(download_link, upx_filename)
        if extract_upx(upx_filename, upx_version):
            print('upx.exe successfully updated.')