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
