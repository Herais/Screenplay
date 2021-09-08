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
fp = 'F:/Github/Screenplay/private_screenplays/愚人之家（2019稿）nowm.docx'
fp = 'input/A Nightmare on Elm Street 3_ Dream Warriors_script.txt'

#%%
'F:/Github/Screenplay/private_screenplays/合并剧本word.docx'.split('.')[-1]
#%%
dfsc = scp.read.auto(fp)

#%%
dfsc = scp.read.docx(fp, pat_sh=u'【】')
#%%
dfDT = dfD.T

#%%
dfC = dfsc.loc[dfsc['Type'] == 'Character', ['Type', 'Element']].copy()
if dfC.shape[0] > 0:
    dfC_expanded = dfC['Element'].str.split('([(（].*[）)])', expand=True)
#%%
dfsc.index.insert(1.1, 'Element')
#%%

dfD['dialogue'].str.split('([(（].*[）)])', expand=True)
