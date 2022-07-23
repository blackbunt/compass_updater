# url = 'https://filestation.compass-software.de/FileManagement/DownloadLink?guid=b4082b52-778f-4be3-8710-6248f3b44f78'
# url = 'https://filestation.compass-software.de/FileManagement/DownloadLink?guid=b4082b52-778f-4be3-8710-6248f3b44f72'
# url = 'http://192.168.0.208:8096/web/index.html#!/item?id=25417&serverId=2f88a993e4414855a6b3ba4135101a79'
# url = 'https://filestation.compass-software.de/FileManagement/DownloadLink?guid=56018ed4-8e35-4a88-b4e1-f42f4ca8287a'
import os
import yaml
import errno
import sys
import download
import menu
import run_update


def read_config(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def create_folder_structure(dirname):
    if not os.path.exists(os.path.dirname(dirname)):
        try:
            os.makedirs(os.path.dirname(dirname))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def read_config(file_path):
    with open(file_path, "r") as f:
        return yaml.safe_load(f)


def clear_scr():
    clear = lambda: os.system('cls')
    clear()


# run the base initialisation
if not os.path.exists('config.yaml'):
    input("Konfigurationsdatei 'config.yaml' fehlt.\nWeiter mit Enter...")
    sys.exit()
config = read_config('config.yaml')

# create folders.
for folder in list(config['paths'].values()):
    create_folder_structure(folder)
# show menu
menu_valid = True
while menu_valid:
    clear_scr()
    menu_value = menu.show_main_menu()
    if menu_value[1] == 0:  # Starte Compass Update von Menü Auswahl
        clear_scr()
        run_update.compass_upd(config['paths']['CompassUpdatePath'])

    elif menu_value[1] == 1:  # Download Update von bereitgestellter URL
        clear_scr()
        input_valid = True
        while input_valid:
            url = input(f'Abbrechen mit \'q\'\n\nCompass Update URL eingeben/einfügen:\n\n')
            if download.url_verify(url):
                download.download_update(url, config['paths']['CompassUpdatePath'],
                                         config['paths']['CompassLicenseUpdatePath'],
                                         config['paths']['CompassPatchUpdatePath'])
                break
            elif url == 'q':
                break
            else:
                print(f'Keine korrekte Eingabe.')

    elif menu_value[1] == 2:  # Starte Lizenstecker Update von Menü Auswahl
        clear_scr()
        run_update.patch_update(config['paths']['CompassPatchUpdatePath'])
    elif menu_value[1] == 3:  # Starte Lizenstecker Update von Menü Auswahl
        clear_scr()
        run_update.liz_update(config['paths']['CompassLicenseUpdatePath'])
    elif menu_value[1] == 4:  # Beende Programm
        sys.exit()
