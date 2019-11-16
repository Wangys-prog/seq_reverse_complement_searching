#!/usr/bin/python
#File created on 2019/11/11

__author__ = "Wang,Yansu"
__copyright__ = "Copyright 2019, JSNU"
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Wang,yansu"
__email__ = "Wangys_c@hotmail.com"

from Bio import SeqIO
from optparse import OptionParser

"""
输入序列文件（.fasta）得到互补序列文件（.fasta）
"""

def MakeOption():
    parser = OptionParser(usage="%prog [-h] [-v] -i[--input=] -o[--output=]",
                          version="%prog 1.0")
    parser.add_option("-i", "--input", action="store", dest="input",
                      help="输入fasta 文件",
                      default=False)
    parser.add_option("-o", "--output", action="store", dest="output",
                      help="输出互补fasta文件",
                      default=False)
    (options, args) = parser.parse_args()
    # extract option from command line
    input = options.input
    output = options.output
    return (input,output)

def reverse_seq(input,output):
    output = open(output,"w")
    for eachline in SeqIO.parse(input, "fasta"):
        reverse_id = eachline.description + "_reverse"
        seq = eachline.seq
        reverse_seq = eachline.reverse_complement(seq).seq
        reverse_seq_2 = reverse_seq[::-1]
        output.write(">%s\n%s\n" % (reverse_id,reverse_seq_2))
    output.close()

def main():
    input, output = MakeOption()
    reverse_seq(input,output)
if __name__ == '__main__':
     main()
