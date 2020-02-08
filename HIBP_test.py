#The Content has been made available for informational and educational purposes only
import argparse
from hibp_api import *
parser = argparse.ArgumentParser()
required = parser.add_argument_group('required arguments')
parser.add_argument('-e','--email',required=True)
args = parser.parse_args()
print(hibp.email(args.email))
