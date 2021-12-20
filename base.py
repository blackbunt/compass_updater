# erstellt die ordnerstruktur, importiert die config.
import yaml
import os
import errno


def read_config(file_path):
    with open( file_path, "r" ) as f:
        return yaml.safe_load( f )


def create_folder_structure(dirname):
    if not os.path.exists( os.path.dirname( dirname ) ):
        try:
            os.makedirs( os.path.dirname( dirname ) )
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise


def run():
    config = read_config( 'config.yaml' )
    for folder in list(config['paths'].values()):
        create_folder_structure(folder)
    return config


if __name__ == '__main__':
    run()
