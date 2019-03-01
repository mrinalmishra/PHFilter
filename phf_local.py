try:
    import argparse
except ImportError, e:
    sys.exit('Requires python 2.7 and above to run ConCat-1.0. Program Terminated')

import textwrap

from PHFilter import *

parser = argparse.ArgumentParser(prog='PHFilter',
                                 version= 'PHFiltert-1.0',
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent('''\
    ----------------------------------------------------------------------------------------------------------
    \t\t\t\t Welcome to PHFilter-1.0
    \t\t\t AVCF file filtering program
    \t\t\tWritten by Mrinal Mishra, University of Florida
    ----------------------------------------------------------------------------------------------------------
    
    
    '''))

parser.add_argument('-i', type=str, required=True,
                    help='Enter input file name')
parser.add_argument('-o', type=str, required=True,
                    help='Enter output file name')
parser.add_argument('-cutoff', type=int, default=1,
                    help='Enter the heterozygous cutoff value. Default is 1.')


args = parser.parse_args()

def main():
    PHF().execute(args.i, args.o, args.cutoff)


if __name__ == "__main__":
    main()
