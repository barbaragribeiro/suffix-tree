import sys
from tree import Suffix_Tree

def main(filename):
    with open(filename, 'r') as fp:
        next(fp)
        rna = ''.join(line.strip() for line in fp)
        tree = Suffix_Tree(rna)
        print(tree.longest_repeated_substr())


if __name__=='__main__':
    main(sys.argv[1])