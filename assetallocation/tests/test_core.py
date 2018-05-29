import sys
print(sys.path)

import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
gparent_dir = os.path.dirname(parent_dir)
print("cur:  ",current_dir)
print("par:  ",parent_dir)
print("gpar:  ",gparent_dir)
sys.path.insert(0, gparent_dir)