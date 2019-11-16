#!/usr/bin/python
#File created on 2019/11/11

__author__ = "Wang,Yansu"
__copyright__ = "Copyright 2019, JSNU"
__license__ = "GPL"
__version__ = "2.0"
__maintainer__ = "Wang,yansu"
__email__ = "Wangys_c@hotmail.com"

"""
序列比对
"""
from optparse import OptionParser
from Bio import SeqIO


def MakeOption():
    parser = OptionParser(usage="%prog [-h] [-v] -i[--input=] -n [--number=] -f [--reference=] -o[--output=]",
                          version="%prog 1.0")
    parser.add_option("-i", "--input", action="store", dest="input",
                      help="输入目的序列文件，格式是txt",
                      default=False)
    parser.add_option("-n", "--number", action="store", dest="number",
                      help="需要切割的序列片段长度需要整数，例如13",
                      default=False)
    parser.add_option("-f", "--reference", action="store", dest="reference",
                      help="被比对序列文件，fasta格式",
                      default=False)
    parser.add_option("-o", "--output", action="store", dest="output",
                      help="输出查找到的序列fasta文件",
                      default=False)
    (options, args) = parser.parse_args()
    # extract option from command line
    input = options.input
    number = options.number
    ref = options.reference
    output = options.output
    return (input,number,ref,output)


def capture_seq(input,number):
##################
# 根据特定长度截取目的序列
    query_seq = open(input,"r")
    n = "".join(number)
    aa = []
    for line in query_seq:
        i = 0
        if int(n) > len(line):
            print("输入的长度应当小于目的序列长度")
        else:
            while int(n)+int(i) <= len(line):
                 aa.append(line[int(i):int(n)+int(i)])
                 i+=1
    return aa

def alignmnet_seq(aa,ref,output):
###########################
# 将截取到的片段进行搜索
    output_file = open(output, "w")
    for eachline in SeqIO.parse(ref, "fasta"):
        id = eachline.description
        seq_db = eachline.seq
        for i in range(len(aa)):
            if str(aa[i]) in str(seq_db):
                bb = str(seq_db).find(str(aa[i])) + 1
                output_file.write(">%s\t%s\t%s\n%s\n" % (id, bb, str(aa[i]), seq_db))
    output_file.close()

def main():
    input,number,ref,output = MakeOption()
    aa = capture_seq(input, number)
    alignmnet_seq(aa,ref,output)
if __name__ == '__main__':
    main()


