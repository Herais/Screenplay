# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 05:45:38 2019

@author: VSurfacePro3
"""
dirpath = "C:\\Users\\VSurfacePro3\\Desktop\\Degree Classes\\Trade University\\CTAI\\R_looklook\\screenplay\\"
jiebadict_path = dirpath + "userdict_SpaceRacer.txt"

import xml.etree.ElementTree as ET
import jieba
import jieba.analyse
jieba.load_userdict(jiebadict_path)
import jieba.posseg as pseg
import nltk
import Screenplay
from Pixabay import Pixabay
#%%
dirpath = "C:\\Users\\VSurfacePro3\\Desktop\\Degree Classes\\Trade University\\CTAI\\R_looklook\\screenplay\\"
filename = "Space Racer MC 1-27-19.xml"
#filename = "SpaceRacer_CNfull_20190423_2038_VX.xml"
filepath = dirpath + filename
tree = ET.parse(filepath)
root = tree.getroot()

paragraphs = list(root.find("paragraphs"))
obj_paragraphs = root.find("paragraphs")


gen = Screenplay.Generate()
list_sceneheadings = gen.list_headings(root, lang="EN")
list_actions = gen.list_actions(root)
list_characters = gen.list_characters(root, rmextension=True, rmduplicates=True)
#additional_char = ['James', 'Grace', '莫德', '斯利格', '蕾蕾', '查理']
list_nonspeaking_characters = gen.list_nonspeaking_characters(root, list_additional_characters=[])

objScene = Screenplay.Scene()
dict_scenes = objScene.dict_scenes(root)
#actions_in_scenetwelve = objScene.list_actions(dict_scenes[12])
#characters_in_scenetwelve = objScene.list_characters(root, scene_number=18, include_nonspeaking=True)

#%%
pb = Pixabay()
#list_keywords = ['Vesta','Burning Planet']
#pb.search(list_keywords, dir_project='SR')
keywords_in_script_byscene = []
for key, scene in dict_scenes.items():
    actions_in_scene = objScene.list_actions(dict_scenes[key])
    characters_in_scene = objScene.list_characters(root, scene_number=key, include_nonspeaking=True)
    #print(actions_in_scene)
    flattened_string = ''
    for action in actions_in_scene:
        #print(action)
        flattened_string += action
        keywords_in_scene = jieba.analyse.extract_tags(flattened_string)
        index = 0
        while index < len(keywords_in_scene):
            for character in characters_in_scene:
                if keywords_in_scene[index] == character:
                    del keywords_in_scene[index]
                    index = index - 1
                    break
            index = index + 1
        keywords_in_script_byscene += keywords_in_scene
        #print(keywords_in_scene)
        
keywords_in_script_byscene = list(set(tuple(keywords_in_script)))
            
        #print(keywords_in_scene)



#%%
pb = Pixabay()
list_keywords = ['space','earth', 'human extinction', 'race ship', 
                 'satellite', 'surveillance camera', 'billboard',
                 'space ship', 'flight deck', 'space map', 'seatbelt']


all_kw += list_keywords
pb.search(list_keywords, dir_project='SR')

all_kw = []


#%%

seg_list = jieba.cut(flattened_string)
list_pseg = []
pseg_obj = pseg.cut(flattened_string)
for w in pseg_obj:
    list_pseg += [[w.word, w.flag]]
    
list_filtered = list(filter(lambda x:x[1] != 'x', list_pseg))
list_filtered = list(filter(lambda x:x[1] != 'c', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'd', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'f', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'i', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'k', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'l', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'm', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'nr', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'p', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'r', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 's', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'u', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'ud', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'uj', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'ul', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'uz', list_filtered))
list_filtered = list(filter(lambda x:x[1] != 'v', list_filtered))
print(list_filtered)

pixabay = Pixabay()






