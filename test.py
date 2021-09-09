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
import PyPDF2 
from PyPDF2  import PdfFileReader

scp = Screenplay.Screenplay()
#%%


fp = 'F:/Github/Screenplay/private_screenplays/合并剧本word.docx'
fp = 'input/A Nightmare on Elm Street 3_ Dream Warriors_script.txt'
fp = 'F:/Github/Screenplay/private_screenplays/愚人之家（2019稿）nowm.docx'
fp = 'F:/Github/Screenplay/private_screenplays/wanglai2.xml'
fp = 'F:/Github/Screenplay/private_screenplays/Friend_Request_2019.xml'

#%%
dfsc = scp.read.auto(fp)
dfsc = scp.parse.Scene_Heading(dfsc)
dfsc = scp.parse.D_Character_Parenthetical(dfsc)
#%%
dft0 = dfsc.loc[dfsc['Type'].isin(['Action', 'Dialogue']), 'Element'].to_frame()
#%%
dft0['zh'] = dft0['Element'].apply(scp.translate.Baidu, 
                                   lang_from='en', 
                                   lang_to='zh')
#%%
dfsc.loc[dfsc['Type'].isin(['Action', 'Dialogue']), 'zh'] = dft0['zh']
#%%
#dfsc.to_json('F:/Github/Screenplay/private_screenplays/df_friend_request.json')
dfsc = pd.read_json('F:/Github/Screenplay/private_screenplays/df_friend_request.json')
#%%

en2zh_IE = {'INT': '内', 'EXT': '外'}
en2zh_Time = {'NIGHT': '夜', 'DUSK': '傍晚',
              'LATER': '稍后', 'CONTINUOUS': '继上','RAINY NIGHT': '雨夜'
              }
dfsc.loc[dfsc.Type == 'Character', 'Element'].unique()

