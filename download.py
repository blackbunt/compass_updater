import urllib.request
import os
import cgi
import errno
from tqdm import tqdm
import re


class DownloadProgressBar(tqdm):
    def update_to(self, b=1, bsize=1, tsize=None):
        if tsize is not None:
            self.total = tsize
        self.update(b * bsize - self.n)


def create_folder_structure(dirname, rootdir):
    try:
        os.makedirs(os.path.join(rootdir, dirname))
        print(f'{dirname} in {rootdir} created.')
    except OSError as e:
        # print(f'{dirname} in {rootdir} already exists.')
        if e.errno != errno.EEXIST:
            print(f'Could not create {dirname} in {rootdir}.')
            raise
def url_verify(url: str):
    '''
    funktion checkt ob der bereitgestellt string eine url ist (nicht ob diese tatsächlich online ist!
    :param url: input url
    :return: bool if valid -> True
    '''
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE )
    if re.match(regex, url) is not None:
        return True
    else:
        return False

def download_update(url: str, output_path_compass: str, output_path_license: str):
    '''
    Downloads Update File from given URL and decides depending of the received filename in which folder the File is saved:
    regular Compass Update Files goes into the output_path_compass folder
    usb license update files goes into the output_path_license folder
    :param url: download url (str)
    :param output_path_compass: output path für download compass upd datei
    :param output_path_license: output path für download lizenstecker upd datei
    :return: NIX!
    '''
    try:
        response = urllib.request.urlopen(url)
        urlcontent = response.info()['Content-Disposition']
        value, params = cgi.parse_header(urlcontent)
        filename = params["filename"]
        filename_formatted = filename.split(".")[-2].replace("_", ".")  # filename gecleaned für lesbarkeit des users
        # check um was es sich handelt (comp update oder liz update)
        if filename.startswith('USB') & filename.endswith('.exe'):
            print(f'Lizenzstecker Update {filename_formatted} gefunden.')
            output_path = output_path_license
        elif filename[0].isdigit() & filename.endswith('.exe'):
            print(f'Compass Update {filename_formatted} gefunden.')
            output_path = output_path_compass
        else:
            print('Konnte Update Datei nicht zuordnen.')
            return


        output_file = os.path.isfile( os.path.join( output_path, filename ) ) # checkt ob datei schon heruntergeladen wurde oder das noch getan werden muss
        input_valid = True
        if output_file:
            print( 'Datei exestiert schon!' )
        while input_valid:
            # wenn datei exestiert
            if output_file == True:

                input_raw = input('Erneut herunterladen? j/n ')
                if input_raw == 'j':
                    bar = DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=f'Downloading Update {filename_formatted}')
                    urllib.request.urlretrieve(url, filename=output_file, reporthook=bar.update_to)
                    break
                if input_raw == 'n':
                    print('Abbruch.')
                    break
                else:
                    print(f'{input_raw} ist keine korrekte Eingabe!')
                    pass
            else: # wenn datei noch nicht exestiert
                bar = DownloadProgressBar(unit='B', unit_scale=True, miniters=1, desc=f'Downloading Update {filename_formatted}')
                urllib.request.urlretrieve(url, filename=output_file, reporthook=bar.update_to)
                break
    except TypeError:
        print(f'Keine Datei gefunden unter {url}')
    except ConnectionError:
        print(f'Verbindung wurde unterbrochen.')

if __name__ == '__main__':
    # Lizenstecker Update
    url = 'https://filestation.compass-software.de/FileManagement/LicenceDownload?LicenceFileName=USB20033177C_211103_1041.exe'
    # reguläres Update
    #url = 'https://filestation.compass-software.de/FileManagement/DownloadLink?guid=b4082b52-778f-4be3-8710-6248f3b44f78'
    create_folder_structure('Updates', os.getcwd())
    create_folder_structure('Compass', os.path.join(os.getcwd(), 'Updates'))
    create_folder_structure('Lizenzstecker', os.path.join(os.getcwd(), 'Updates'))
    download_path_compass = os.path.join(os.getcwd(), 'Updates/Compass/')
    download_path_license = os.path.join(os.getcwd(), 'Updates/Lizenzstecker/')
    if url_verify(url):
        download_update(url, download_path_compass, download_path_license)
