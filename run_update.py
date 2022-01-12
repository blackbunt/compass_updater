from pick import pick
import os
import glob
import yaml
import natsort
import subprocess


def read_config(file_path):
    with open( file_path, "r" ) as f:
        return yaml.safe_load( f )


def compass_upd(folder: str):
    liste = []
    files = []
    menu = 'Zurück zum Hauptmenü'
    os.chdir( folder )
    for file in glob.glob( "*.exe" ):
        liste.append( file )
        # liste.append(file.split(".")[-2].replace("_", "."))

    if len(liste) != 0:
        files = natsort.humansorted(liste, reverse=True)
        filename = files[0]
        filename_bella = filename.split(".")[-2].replace("_", ".")
        files.insert(0, menu)
        title = f'Wähle Update aus. Neustes Update: {filename_bella}'
    else:
        files.insert(0, menu)
        title = 'Kein Compass Update heruntergeladen.'
    # create auswahl menu
    option, index = pick( files, title, indicator='•', default_index=0 )
    if index == 0:
        return None
    else:
        subprocess.call( os.path.join( folder, option ) )


def liz_update(folder: str):
    liste = []
    files = []
    menu = 'Zurück zum Hauptmenü'
    os.chdir(folder)
    for file in glob.glob("*.exe"):
        liste.append(file)
        # liste.append(file.split(".")[-2].replace("_", "."))
    # wenn dateien vorhanden, sortiere sie absteigend wie ein mensch es tun würde
    if len(liste) != 0:
        files = natsort.humansorted(liste, reverse=True)
        filename = files[0]
        filename_bella = filename.split(".")[-2].replace("_", ".")
        files.insert(0, menu)
        title = f'Wähle Update aus. Neustes Update: {filename_bella}'
    else:
        files.insert(0, menu)
        title = 'Kein Lizenzstecker Update heruntergeladen.'
    # create auswahl menu
    option, index = pick(files, title, indicator='•', default_index=0)
    if index == 0:
        return None
    else:
        subprocess.call(os.path.join(folder, option))


if __name__ == '__main__':
    config = read_config( 'config.yaml' )
    comp_path = config['paths']['CompassUpdatePath']
    liz_path = config['paths']['CompassLicenseUpdatePath']

    compass_upd( comp_path )

    title = 'Compass Update Helper: '
    options = ['Starte Update', 'Update Download', 'Beenden']

    # option, index = pick(options, title, indicator='=>', default_index=0)
