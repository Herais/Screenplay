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

fp = 'F:/Github/Screenplay/private_screenplays/wanglai2.xml'
fp = 'F:/Github/Screenplay/private_screenplays/愚人之家（2019稿）nowm.docx'
fp = 'F:/Github/Screenplay/private_screenplays/合并剧本word.docx'
fp = 'input/A Nightmare on Elm Street 3_ Dream Warriors_script.txt'


#%%
'F:/Github/Screenplay/private_screenplays/合并剧本word.docx'.split('.')[-1]
#%%
Read = Read()
dfsc = Read.auto(fp)
#%%
'docx' in ['doc', 'docx']
#%%
dfsc = scp.read.docx(fp, pat_sh=u'【】')

#%%
pat_d = '[:：]'
    
idx_d = dfsc.loc[dfsc['Element'].str.contains(pat_d)].index

dfsc.loc[idx_d, 'Element'].str.split(pat_d, n=1, expand=True)