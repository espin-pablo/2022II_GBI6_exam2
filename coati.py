from Bio import Entrez 
from Bio import SeqIO
import re
import csv

def fasta_downloader():
        id_coati = open("data\coati.txt", "r")
        print(id_coati.readlines())

