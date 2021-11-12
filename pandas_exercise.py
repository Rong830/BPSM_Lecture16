import os, sys, re, numpy as np
import pandas as pd


### Down load data
# New version, called it tsv as its tab-separated values
os.system("wget -qO eukaryotes.tsv 'ftp://ftp.ncbi.nlm.nih.gov/genomes/GENOME_REPORTS/eukaryotes.txt'")

# Read the file into a dataframe
df = pd.read_csv('eukaryotes.tsv', sep="\t", na_values=['-'])

### Process data
# Count the number of fungi species hace genomes bigger than 100Mb
len(df[df.apply(lambda x : x['Group'] == 'Fungi' and x['Size (Mb)'] > 100, axis=1)])

# Print the name of each fungi species
df[df.apply(lambda x : x['Group'] == 'Fungi' and x['Size (Mb)'] > 100, axis=1)]['#Organism/Name']

# Count the number of each groups that have been sequenced.
for Group in ['Plants', 'Animals', 'Fungi', 'Protists']:
    count = len(df[df['Group'] == Group])
    count_unique = len(set(df[df['Group'] == Group]['#Organism/Name']))
    count_unique = len(df[df['Group'] == Group].drop_duplicates('#Organism/Name'))
    print("{} genomes for {} ({} unique)"i.format(count, Group, count_unique))

# Selet all species from Heliconius genome that have been sequenced.
hel = df.apply(lambda x : x['#Organism/Name'].startswith('Heliconius'),axis=1)

# Which center has sequenced the most plant genomes?
df[df['Group'] == 'Plants']['Center'].value_counts()

# Which center has sequenced the most insect genomes?
df[df['SubGroup'] == 'Insects']['Center'].value_counts().head()

# Add a column giving the number of proteins per gene
df['Proteins'] / df['Genes']
df['Proteins per gene'] = df['Proteins'] / df['Genes']
# Show the results
df[ ['#Organism/Name', 'Group', 'Proteins per gene'] ].head()

# Which genomes have at least 10% more proteins than genes?
df[df['Proteins per gene'] >= 1.1][ ['#Organism/Name', 'Genes','Proteins','Proteins per gene'] ].head()



