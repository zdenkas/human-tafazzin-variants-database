# Modifications of Human Tafazzin Variants Database

This repository contains Python notebooks that fix inconsistencies in the [Human Tafazzin Variants Database](https://www.barthsyndrome.org/research/tafazzindatabase.html) and enhance the database with publicly available data.

The official version of the Human Tafazzin Variants Database is currated by the Barth Syndrome Foundation and is currently available at https://drive.google.com/drive/folders/1O2MKa5FHsvq3hyjOVSsOZf37xkwKYAJ8 

Folders:
* notebooks:
    * Python notebooks that were applied to the dataset in alphanumerical order (e.g., notebook 00000_xxx.ipynb was applied first, 00010_yyy.ipynb after that, …). (TODO add papermill pipeline)
    * Each notebook contains code that generated a new version of the database.
    * Notebooks also serve as database versioning documentation: at the beginning of each notebook, you will find a description of what changes for that particular version.
* database_versions:
    * Versions of the database. They contain a timestamp in their name and can be matched to corresponding notebooks with the number before the underscore. (E.g., notebook 00000_xxx.ipynb generated databases (csv files) `00000_some-timestamp_Human-TAFAZZIN-Variants-Database_pathogenic.csv`, `00000_some-timestamp_Human-TAFAZZIN-Variants-Database_benign.csv`, ...)
    * The latest version is the one with the highest number. 
        * currently only latest version is in Git. TODO this should be created by papermill pipeline & have semantic versioning
        
 * [TODOs](https://github.com/zdenkas/human-tafazzin-variants-database/blob/main/TODO.txt)

  If you have any questions, feel free to contact me at zdenka@sedenka.cz, or create an issue. 
