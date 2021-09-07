# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:01:10 2021

@author: VXhpUS
"""
import os
from pathlib import Path
import re
from screenplay import Screenplay
import pandas as pd
import math
from docx import Document

scp = Screenplay.Screenplay()
#%%


fp = 'F:/Github/Screenplay/private_screenplays/合并剧本word.docx'
fp = 'F:/Github/Screenplay/private_screenplays/wanglai2.xml'

fp = 'input/A Nightmare on Elm Street 3_ Dream Warriors_script.txt'
fp = 'F:/Github/Screenplay/private_screenplays/愚人之家（2019稿）nowm.docx'
#%%
'F:/Github/Screenplay/private_screenplays/合并剧本word.docx'.split('.')[-1]
#%%
dfsc = scp.read.auto(fp)
#%%
dfsc_psh = scp.parse.scene_heading(dfsc)
#%%
dfsc = scp.read.docx(fp, pat_sh=u'【】')

#%%
dfD = scp.parse.Dialogue(dfsc)
#%%

dfD['dialogue'].str.split('([(（].*[）)])', expand=True)
