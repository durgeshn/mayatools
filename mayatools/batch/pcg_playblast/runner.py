import sys
import os

sys.path.append(r'C:\Users\amol\PycharmProjects')
# os.path.join(__file__)
from mayatools.batch.pcg_playblast import playblast_bat

a = playblast_bat.batPlayblast('SH004_CAM:cameraHD', 'D:/temp/BDG105_004_layNew.ma', 101, 105)
print (a)
