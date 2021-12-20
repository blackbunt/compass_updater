from pick import pick


def show_menu():
    title = 'Compass Update Helper: '
    options = ['Starte Update', 'Update Download', 'Beenden']

    option, index = pick(options, title, indicator='=>', default_index=0)

    return [option, index]

