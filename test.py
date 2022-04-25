import os
# from cvmblaster.blaster import Blaster
from Bio.Blast.Applications import NcbimakeblastdbCommandline


db = '/Users/cuiqingpo/Downloads/blast_db/resfinder'

input = "/Users/cuiqingpo/Downloads/test_genome/nx19E1.fa"
output = "/Users/cuiqingpo/Downloads/test_genome/test"
# help(Blaster)
# output = "~/Downloads/test_genome/test"
# if not os.path.exists(output):
#     os.mkdir(output)
# # outpath = os.path.abspath(output)
# print(output)


# # print(os.path.abspath('~/Downloads/test_genome/test'))


# test = Blaster(input, db, output, 8, ).biopython_blast()

# print(test)


db_file = '/Users/cuiqingpo/Downloads/blast_db/all.fsa'
name = '/Users/cuiqingpo/Downloads/blast_db/resfinder'


def initialize_db():
    database_path = os.path.join(
        os.path.dirname(__file__), f'db')
    for file in os.listdir(database_path):
        if file.endswith('.fsa'):
            file_path = os.path.join(database_path, file)
            file_base = os.path.splitext(file)[0]
            out_path = os.path.join(database_path, file_base)
            Blaster.makeblastdb()


def makeblastdb(file, name):
    cline = NcbimakeblastdbCommandline(
        dbtype="nucl", out=name, input_file=file)
    stdout, stderr = cline()


print('Start')
makeblastdb(db_file, name)
