from Bio import SeqIO
import pandas as pd

TAZ_POSITIONS_PATH = '../data_external/ExonsSpreadsheet-Homo_sapiens_Transcript_Exons_ENST00000601016_whole_table.csv'
TAZ_SEQUENCES_PATH = '../data_external/Homo_sapiens_ENST00000601016_6_sequence.fa'


def find_unexpected_letters_on_38_position(taz_database_38_loc, 
                                           dna_modifications, 
                                           taz_positions, 
                                           taz_sequences_path=TAZ_SEQUENCES_PATH):
    """
    Find unexpected letter in TAZ database
    
    Parameters
    ----------
    taz_dabase_38_loc : int
        Location in Genome release  38 (hg38) from TAZ database, e.g. 154411894

    dna_modifications : str
        DNA modifications field from TAZ database, e.g. c.51G>A     

    taz_positions : pandas dataframe
        TAZ positions from ensembl.org in hg38, loaded by `load_taz_positions`. 
    
    taz_sequences_path : str
        Path to TAZ sequences from ensembl.org
        
    """
    weird_split = None
    unexpected = None
    
    row_from_taz_positions = get_row_from_taz_positions(taz_database_38_loc, taz_positions)
    exon_intron_from_taz_positions = row_from_taz_positions['Exon / Intron']
    start_from_taz_positions = row_from_taz_positions['Start']
    end_from_taz_positions = row_from_taz_positions['End']
    seq_from_taz_positions = row_from_taz_positions.Sequence.split('}')[-1].strip()

    seq_record = find_seq_record(exon_intron_from_taz_positions, taz_sequences_path)

    if seq_record:
        sequence = seq_record.seq
        pos_in_sequence = taz_database_38_loc - start_from_taz_positions
        expected_letter = sequence[pos_in_sequence]
        
        dna_modifications_split = dna_modifications.split('>')
        assert len(dna_modifications_split) >= 2, f'problem with split for {dna_modifications}; {dna_modifications_split}'

        if len(dna_modifications_split) > 2:
            weird_split = f'weird split for "{dna_modifications}"; {dna_modifications_split}; {taz_database_38_loc}'

        dna_modifications_letter = dna_modifications_split[0].strip()[-1]
        if dna_modifications_letter != expected_letter:
            unexpected = f'Expected from position {taz_database_38_loc}: {expected_letter} ; dna modifications: {dna_modifications}'
            print(unexpected)
    else:
        print("No matching record found.")
    return unexpected, weird_split

def get_row_from_taz_positions(taz_database_38_loc, taz_positions):
    """
    Get row for taz_database_38_loc with exon/intron info
    """
    matching_rows = taz_positions[(taz_positions['Start'] <= taz_database_38_loc) & (taz_positions['End'] >= taz_database_38_loc)]
    # We expect only one match and want to get a single value
    if len(matching_rows) == 1:
        return matching_rows.iloc[0]
    else:
        print(f"Multiple or no matching rows found! {taz_database_38_loc}")
        return None
    
def find_seq_record(exon_intron_info, taz_sequences_path):
    """
    Find sequence from exon / intron info
    """
    
    # Use a generator expression to find the first matching seq_record
    seq_record = next((record for record in SeqIO.parse(taz_sequences_path, "fasta") if exon_intron_info in record.description), None)
    return seq_record

def load_taz_positions(taz_positions_path=TAZ_POSITIONS_PATH):
    """
    Load TAZ positions from ensembl.org
    
    Returns
    -------
    pandas dataframe
    """
    taz_positions = pd.read_csv(taz_positions_path)
    
    taz_positions['Start'] = pd.to_numeric(taz_positions['Start'].str.replace(',', ''), errors='coerce')
    taz_positions['Start'] = taz_positions['Start'].fillna(0).astype(int)
    
    taz_positions['End'] = pd.to_numeric(taz_positions['End'].str.replace(',', ''), errors='coerce')
    taz_positions['End'] = taz_positions['End'].fillna(0).astype(int)
    
    return taz_positions