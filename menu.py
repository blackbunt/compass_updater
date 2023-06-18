from pick import pick

global version
version = '2023-06-18'

heading = f"\n   ___                                    _   _           _        _           _  _       _\n  / __| ___  _ __   _ __  __ _  ___ ___  | | | | _ __  __| | __ _ | |_  ___   | || | ___ | | _ __  ___  _ _\n | (__ / _ \| '  \ | '_ \/ _` |(_-<(_-<  | |_| || '_ \/ _` |/ _` ||  _|/ -_)  | __ |/ -_)| || '_ \/ -_)| '_|\n  \___|\___/|_|_|_|| .__/\__,_|/__//__/   \___/ | .__/\__,_|\__,_| \__|\___|  |_||_|\___||_|| .__/\___||_|\n                   |_|                          |_|                                         |_|\n\n© Bernhard Kauffmann - Version: {version}\n\nNutzung dieser Software geschieht auf eigene Verantwortung!"


def show_main_menu():
    title = heading
    options = ['Installiere Update', 'Installiere Patch', 'Installiere Lizenzstecker Update', 'Downloade Update/Patch', 'Öffne Download-Ordner', 'Beenden']

    option, index = pick(options, title, indicator='•', default_index=0)

    return [option, index]


def menu_yes_no(message: str):
    """
    Renders a yes/no option menu, returns choice
    :param message: message printed for decision
    :return:
    """
    options = ['Ja', 'Nein']
    title = message

    option, index = pick(options, title, indicator='•', default_index=1)
    return option, index