import sys
from tree import Suffix_Trie

def main(filename):
    with open(filename, 'r') as fp:
        dna = ''.join(line for line in fp)
        tree = Suffix_Trie(dna)
        print('TODO')


if __name__=='__main__':
    main(sys.argv[1])