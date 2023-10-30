import ipynbname
import os
import datetime

def create_database_output_path(folder='../database_versions'):
    version_number = get_version_number()
    output_file_name = create_database_output_file_name(version_number)
    output_path = os.path.join(folder, output_file_name)
    print(f'database output path: {output_path}')
    return output_path

def create_database_output_file_name(version_number):
    now = str(datetime.datetime.now()).replace(':', '-').replace('.', '-').replace(' ', '-')
    output_file_name = f'{version_number}_{now}_Human-TAFAZZIN-Variants-Database.xlsx'
    return output_file_name
    
def get_version_number(database_folder='../database_versions'):
    # get version number from current notebook name
    nb_fname = ipynbname.name()
    version_number = nb_fname.split('_')[0]
    assert len(version_number) == 4, f'version_number (= beginning of filename of this Python notebook before the underscore) must have length 4, now is {version_number}'
    assert version_number.isnumeric(), f'version_number (= beginning of filename of this Python notebook before the underscore) must be numeric, now is {version_number}'
    print('version number:', version_number)

    # check that version_number will be the highest in database_folder
    database_files = os.listdir(database_folder)
    data_suffix = '.xlsx'
    data_prefixes = [file.split('_')[0] for file in database_files if file.endswith(data_suffix)]
    if len(data_prefixes) >= 1:
        assert version_number >= sorted(data_prefixes)[-1], f'version_number (= beginning of filename of this Python notebook before the underscore) must be the highest number from all database file names {database_folder}, now the highest in that folder is {sorted(data_prefixes)[-1]} and version_number is {version_number}'
        if version_number == sorted(data_prefixes)[-1]:
            print(f'Dataset with prefix {version_number} already exists -- this notebook will create new dataset with same prefix but new timestamp.')

    # check that version_number is the highest in notebooks folder (= current folder)
    notebook_files = os.listdir('.')
    notebook_suffix = '.ipynb'
    notebook_prefixes = [file.split('_')[0] for file in notebook_files if file.endswith(notebook_suffix)]
    assert version_number == sorted(notebook_prefixes)[-1], f'Version_number (= beginning of filename of this Python notebook before the underscore) must be the highest number from all the notebooks in this folder, now the highest is {sorted(notebook_prefixes)[-1]} and version_number is {version_number}'

    return version_number