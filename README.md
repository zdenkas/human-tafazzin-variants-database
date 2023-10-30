# human-tafazzin-variants-database
Human Tafazzin Variants Database modifications.

This repository contains Python notebooks, which fix inconsistencies in Human Tafazzin Variants Database and enhances the database with publicaly available data. 

(The official version of Human Tafazzin Variants Database is currently available at https://drive.google.com/drive/folders/1O2MKa5FHsvq3hyjOVSsOZf37xkwKYAJ8 .)

### Folders:
* notebooks:
    * Python notebooks, which were applied to the dataset in alphanumerical order (e.g. notebook 0000_xxx.ipynb was applied first, 0001_yyy.ipynb after that, ...).
    * Each notebook contains code, which generated a new version of the database
    * Notebooks serve also as versioning documentation: in the beginning of each notebook, you will find a description of what changes for that particular version. 
* database_versions: 
    * Versions of database. They contain timestamp in their name and can be matched to corresponding notebooks with the number before the underscore. (E.g. notebook 0000_xxx.ipynb generated database (excel file) 0000_some-timestamp_Human-TAFAZZIN-Variants-Database.xslx
    * Latest version is the one with the highest number