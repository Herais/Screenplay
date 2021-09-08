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
#%%
scp = Screenplay.Screenplay()
#%%


fp = 'F:/Github/Screenplay/private_screenplays/合并剧本word.docx'
fp = 'F:/Github/Screenplay/private_screenplays/wanglai2.xml'

fp = 'input/A Nightmare on Elm Street 3_ Dream Warriors_script.txt'
fp = 'F:/Github/Screenplay/private_screenplays/愚人之家（2019稿）nowm.docx'

#%%
#%%
dfsc = scp.read.docx(fp, pat_sh=u'【】')
#%%
dfsc1 = scp.parse.D_Character_and_Dialogue(dfsc)

#%%
dfsc2 = scp.parse.D_Character_Parenthetical(dfsc1)

#%%
dfC = dfsc1.loc[dfsc1['Type'] == 'Character', 'Element']
#%%
pat_parenthetical='([(（].*[）)])'
dfC_expanded = dfC.str.split(pat_parenthetical, expand=True)
dfC_expanded = dfC_expanded.rename(columns={0: 'Character', 1:'Parenthetic'})
#%%
dfC_melted = dfC_expanded[['Character', 'Parenthetic']].melt(ignore_index=False)
#%%
dfsc_merged = dfsc1.merge(dfC_melted, left_index=True, right_index=True, how='left') 
#%%
dfsc_merged['Type'].update(dfsc_merged['variable'])
dfsc_merged['Element'].update(dfsc_merged['value'])
#%%
dfsc_merged.columns