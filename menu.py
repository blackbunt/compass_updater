from pick import pick


def show_main_menu():
    title = 'Compass Update Helper: '
    options = ['Starte Update', 'Downloade Update', 'Starte Lizenzstecker Update', 'Beenden']

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

