# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 00:01:28 2020

@author: VSurfacePro3
"""
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 05:45:38 2019

@author: VSurfacePro3
"""


import xml.etree.ElementTree as ET
import jieba
import jieba.analyse
jieba.load_userdict(jiebadict_path)
import jieba.posseg as pseg
import nltk
import Screenplay
from Pixabay import Pixabay

#%% Import File
dirpath = "input"
fp = dirpath + '/' + '合并剧本word.docx'

jiebadict_path = dirpath + "userdict_SpaceRacer.txt"