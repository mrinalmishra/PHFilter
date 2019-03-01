#PHFilter v1.0

It removes private heterozygous genotype from VCF file

###Read Manual for detail instructions

##Requirements:

Python 2.7 and above

Usage:

python phf_local.py -i input_vcf_file -o output_file -cutoff 1.0

-cutoff is optional. Default is set to 1.

To import PHFilter in your python code, copy and paste PHFilter folder to you local directory and type following in your python code

from PHFilter import *

To execute the PHFilter module type

PHF().execute(inputfile, outputfile, heterozygous_cutoff)

You can choose any heterozygous_cutoff value. Default is 1 when heterozygous_cutoff not defined.
