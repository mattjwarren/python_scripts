import os
import sys
import re
#
#
# Quick script to flatten a directory structure and replace 
# unfriendly characters in the filename with _
#
try:
    root_dirpath=sys.argv[1]
except IndexError:
    raise Exception("Need to specify a root directory")

if not os.path.exists(os.path.abspath(root_dirpath)):
    raise FileNotFoundError("%s does not appear to exist" % root_dirpath)

for root,dirs,files in os.walk(root_dirpath):
    for filename in files:
        current_filepath=os.path.join(root,filename)

        new_filename=re.sub('[^0-9a-zA-Z_-.]+','_',filename)
        flattened_rootname=re.sub('[^0-9a-zA-Z_-]+','_',root)
        flattened_filepath=flattened_rootname+"_"+new_filename

        flattened_filepath=flattened_filepath.lstrip('_')

        print("Renaming: %s to %s" % (current_filepath,flattened_filepath))

        os.rename(current_filepath,flattened_filepath)

