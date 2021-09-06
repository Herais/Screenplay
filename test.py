# -*- coding: utf-8 -*-
"""
Created on Wed Sep  1 15:01:10 2021

@author: VXhpUS
"""
import re
import Screenplay
import pandas as pd
import math
#%%

scp = Screenplay.Screenplay()
#%%
fp = 'F:/Github/Content/tools/screenplay/input/合并剧本word.docx'
fp = 'F:/Github/Content/tools/screenplay/output/wanglai.xml'
fp = filepath = 'input/A Nightmare on Elm Street 3_ Dream Warriors_script.txt'


#%%
dfsc = scp.read.text(fp)
#%%
dfsc['Time'] = dfsc.groupby('Scene')['Time'].fillna(method='ffill')
