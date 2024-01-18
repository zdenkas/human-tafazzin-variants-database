import ipynbname
import os
import datetime

def create_database_output_path_prefix(folder='../database_versions'):
    version_number = get_version_number()
    output_file_name_prefix = create_database_output_file_name_prefix(version_number)
    output_path_prefix = os.path.join(folder, output_file_name_prefix)
    print(f'database output path prefix: {output_path_prefix}')
    return output_path_prefix

def create_database_output_file_name_prefix(version_number):
    now = str(datetime.datetime.now()).replace(':', '-').replace('.', '-').replace(' ', '-')
    output_file_name_prefix = f'{version_number}_{now}_Human-TAFAZZIN-Variants-Database_'
    return output_file_name_prefix
    
def get_version_number(database_folder='../database_versions'):
    # get version number from current notebook name
    nb_fname = ipynbname.name()
    version_number = nb_fname.split('_')[0]
    assert len(version_number) == 5, f'version_number (= beginning of filename of this Python notebook before the underscore) must have length 5, now is {version_number}'
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

def save_output_as_csv(output_path_prefix, 
                       df_pathogenic, df_benign, df_vus, df_exon5):
    df_pathogenic.to_csv(output_path_prefix + 'pathogenic.csv', index=False)
    print(f'Dataframe of shape {df_pathogenic.shape} saved to {output_path_prefix}pathogenic.csv')
        
    df_benign.to_csv(output_path_prefix + 'benign.csv', index=False)
    print(f'Dataframe of shape {df_benign.shape} saved to {output_path_prefix}benign.csv')

    df_vus.to_csv(output_path_prefix + 'vus.csv', index=False)
    print(f'Dataframe of shape {df_vus.shape} saved to {output_path_prefix}vus.csv')

    df_exon5.to_csv(output_path_prefix + 'exon5.csv', index=False)
    print(f'Dataframe of shape {df_exon5.shape} saved to {output_path_prefix}exon5.csv')
    