from Bio import Entrez 
from Bio import SeqIO
from Bio.Seq import Seq 
from Bio.SeqRecord import SeqRecord 
from Bio import SeqIO 

def fasta_downloader():
    """" 
    Permite obtener un archivo gb
    """   
    with open('data\coati.txt', 'r+') as a:
            id_coati = a.readlines()    
    Entrez.email = "gualapuro.moises@gmail.com"
    with Entrez.efetch( db="nucleotide", rettype="gb", retmode="text", id= "id_coati") as handle:
        seq_record = SeqIO.read(handle, "gb")
        SeqIO.write(seq_record, "data\coati.gb", "gb")