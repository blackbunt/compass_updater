from pick import pick


def show_menu():
    title = 'Compass Update Helper: '
    options = ['Starte Update', 'Downloade Update', 'Starte Lizenzstecker Update', 'Beenden']

    option, index = pick(options, title, indicator='=>', default_index=0)

    return [option, index]

