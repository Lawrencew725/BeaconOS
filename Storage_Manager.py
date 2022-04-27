import re
import os, Messages_Declear as Messages_Declear
from Text_edit import tager, __name__
file_manager_a = open("tpa.txt", 'w')
file_manager_b = open("tpb.txt", 'w')
file_manager_c = open("tpc.txt", 'w')
file_manager_el = open("Else.txt", 'w')
known_file = [ ]
tpa = [ ]
tpb = [ ]
tpc = [ ] 
script_file = [ ]
tag_a = ["tpa"]
tag_b = ["tpb"]
tag_c = ["tpc"]
n_tpa = str(tpa)
n_tpb = str(tpb)
n_tpc = str(tpc)
n_el = str(known_file)
def backup():
    file_manager_a.write('n_tpa')
    file_manager_a.write(n_tpa)
    file_manager_b.write('n_tpb')
    file_manager_b.write(n_tpb)
    file_manager_c.write('n_tpc')
    file_manager_c.write(n_tpc)
    file_manager_el.write('n_el')
    file_manager_el.write(n_el)
def tag():
    if tager in tag_a:
        file_manager_a.write(__name__)
    elif tager in tag_b:
        file_manager_b.write(__name__)
    elif tager in tag_c:
        file_manager_c.write(__name__)
    else:
        file_manager_el.write(__name__)