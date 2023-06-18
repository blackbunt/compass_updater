# ota update exe
import requests
import sys
import os
import re
import tqdm
import subprocess
from bs4 import BeautifulSoup

global version

def get_version(version: str):
    '''
    checks if a newer version is available on GitHub
    :return: bool if a newer version is available -> True
    :return: str download link for the latest release
    :return: str latest release version
    :return: str new release version
    '''
    # get the latest release version from GitHub
    url = 'https://github.com/blackbunt/compass_updater/releases/latest'
    r = requests.get(url)
    if r.status_code != 200:
        print('Error while getting latest release version, please check your internet connection.')
        os.system('pause')
    # speichert den html code der website in der variable html
    url = r.request.url
    # extract the download link for the latest version with regex
    regex_version = r'\d{4}-\d{2}-\d{2}'

    # Search for the date pattern in the URL
    match = re.search(regex_version, url)
    extracted_version = None
    if match:
        extracted_version = match.group()
        if extracted_version > version:
            #print('Newer version available')
            #print(f'Latest release version: {extracted_version}')
            #print(f'Current version:        {version}')
            return True, url, extracted_version

        else:
            print('You are using the latest version.')
            return False, url, extracted_version
    else:
        print('No version found in URL')
        return False, url, extracted_version


def download_update(dl_url: str, version: str):
    '''
    downloads the latest release from GitHub
    :param dl_url: download link for the latest release
    :param version: latest release version
    :return: bool if download was successful -> True
    '''
    asset_name = f'Compass_Update_Helper_{version}.exe'
    # get current directory
    current_dir = os.getcwd()


    # Eine GET-Anfrage an die Website senden
    response = requests.get(dl_url)

    # Den HTML-Inhalt der Website extrahieren
    html_content = response.text

    # BeautifulSoup verwenden, um den HTML-Inhalt zu analysieren
    soup = BeautifulSoup(html_content, "html.parser")

    # Jetzt kannst du auf die verschiedenen Elemente der Website zugreifen
    # Zum Beispiel kannst du den Titel der Website auslesen:
    title = soup.title
    #print("Titel: " + title.text)

    # Finde alle Elemente mit der CSS-Klasse "div"
    elements = soup.find_all("div", attrs={"data-view-component": "true"})

    # schreibe die elemente in eine liste und suche nach dem asset link
    asset_content = None
    for element in elements:
        sub_element = element.find("include-fragment", attrs={"loading": "lazy"})
        if sub_element is not None:
            # append the asset content to a list
            asset_content = sub_element['src']
            break
    #print(asset_content)

    # untersuche den asset content nach dem asset link
    # nutze beautiful soup um den asset link zu finden
    asset_link = None
    response = requests.get(asset_content)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
    elements = soup.find_all("div", attrs={"data-view-component": "true"})
    for element in elements:
        sub_element = element.find("a", attrs={"class": "Truncate"})
        if sub_element is not None:
            # append the asset content to a list
            asset_link = sub_element['href']
            break
    #print(asset_link)
    # asset link muss noch angepasst werden
    if asset_link.startswith('/'):
        asset_link = 'https://github.com' + asset_link
    #print(asset_link)
    # download the asset
    r = requests.get(asset_link, stream=True)
    if r.status_code != 200:
        print('Error while downloading update, please check your internet connection.')
        os.system('pause')
    # get the file size
    total_size = int(r.headers.get('content-length', 0))
    block_size = 1024
    t = tqdm.tqdm(total=total_size, unit='iB', unit_scale=True)
    with open(asset_name, 'wb') as f:
        for data in r.iter_content(block_size):
            t.update(len(data))
            f.write(data)
    t.close()
    if total_size != 0 and t.n != total_size:
        print("ERROR, something went wrong")
        os.system('pause')

    print('Download successful')


def open_explorer():
    '''
    opens the explorer in the current directory
    :return: None
    '''
    current_dir = os.getcwd()
    subprocess.Popen(f'explorer "{current_dir}"')


def print_message(old_version: str, new_version: str):
    '''
    prints a message if a newer version is available
    :param old_version: current version
    :param new_version: latest release version
    :return: bool if user wants to download the latest release -> True
    '''
    print('Eine neue Version ist verfügbar.')
    print()
    print(f'Aktuelle Version: {new_version}')
    print(f'genutze Version:  {old_version}')
    print()
    # user fragen ob er die neue version herunterladen möchte
    print('Möchtest du die neue Version herunterladen?')
    print( 'y/n')
    user_input = input()
    if user_input == 'y':
        return True
    elif user_input == 'n':
        return False
    else:
        print('Ungültige Eingabe')
        print('Bitte erneut versuchen')
        print()
        print_message(old_version, new_version)

def print_tutorial(new_version: str):
    '''
    prints a tutorial for the new version installation
    :param new_version:
    :return:
    '''
    # clear the console on windows
    clear = lambda: os.system('cls')
    clear()
    print('Anleitung um Programm zu aktualisieren:')
    print('')
    print('1. Schließe das Programm')
    print('2. Lösche die alte Version')
    print(f'3. Benenne "Compass_Update_Helper_{new_version}.exe" in "Compass_Update_Helper.exe" um')
    print('4. Starte das Programm')
    print('5. Fertig!')
    print('')

    os.system('pause')

def run_ota_module(current_version):
    newer_version_available, url, newer_version = get_version(current_version)
    if newer_version_available and newer_version is not None and url is not None:
        # ask the user if he wants to download the latest release version and store the answer in download
        download = print_message(current_version, newer_version)
        # when the user wants to download the latest release version, download it
        if download:
            download_update(url, newer_version)
            print_tutorial(newer_version)
            open_explorer()
            # programm beenden
            sys.exit()
        else:
            pass
    else:
        pass


if __name__ == '__main__':
    version = '2021-08-01'
    run_ota_module(version)


