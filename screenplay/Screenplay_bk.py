# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 01:55:06 2019

@author: VSurfacePro3
"""
from xml.dom import minidom
import xml.etree.ElementTree as ET
from pathlib import Path
import re
import jieba
import jieba.analyse

#%%
class Screenplay（object）：:
    pass

class Generate(object):
      
    def list_headings(self, root, 
                      rmduplicates=False, 
                      lang="EN", 
                      locationonly=False):
        paragraphs = list(root.find("paragraphs"))
        parser = Parse()
        list_headings = []
        for para in paragraphs:
            if para[0].get("basestylename") == "Scene Heading":  #style, check if heading
                heading = para[1].text
                heading = parser.scene_heading(heading, lang=lang)
                list_headings += [heading]
        if rmduplicates:
            list_headings = list(set(tuple(list_headings)))
        if locationonly:
            list_headings = list(set(tuple(map(lambda x:x[1], list_headings))))
        return list_headings
    
    def list_characters(self, root, 
                        rmduplicates=False, 
                        nonspeaking=False, 
                        rmextension=False):
        paragraphs = list(root.find("paragraphs"))
        list_characters = []
        for para in paragraphs:
            item_type = para.find("style").get("basestylename")
            if item_type == "Character":
                text_per_character = ''
                for item in para.iter('text'):
                    if item.text != None:
                        text_per_character += item.text
                if rmextension:
                    parser = Parse()
                    text_per_character = parser.character(text_per_character)
                    text_per_character = text_per_character[0]
                list_characters += [text_per_character]
        if rmduplicates:
            list_characters = list(set(tuple(list_characters)))
        return list_characters
    
    def list_actions(self, root, num_scenes = 0):
        paragraphs = list(root.find("paragraphs"))
        list_actions = []
        for para in paragraphs:
            item_type = para.find("style").get("basestylename")
            if item_type == "Action":
                text_per_action = ''
                for item in para.iter('text'):
                    if item.text != None:
                        text_per_action += item.text
                list_actions += [text_per_action]
        return list_actions
    
    def list_nonspeaking_characters(self, root, list_additional_characters=[]):
        scene = Scene()
        dict_scenes = scene.dict_scenes(root)
        speaking_characters = self.list_characters(root, rmextension=True, rmduplicates=True)
        if len(list_additional_characters) != 0:
            speaking_characters = speaking_characters + list_additional_characters
        list_nonspeaking_characters = []
        for character in speaking_characters:
            for scene, content in dict_scenes.items():               
                for item in content:
                    if item[0] == 'Action':
                        pattern = re.compile(character)
                        matched_character = pattern.search(item[1])
                        if matched_character != None:
                           list_nonspeaking_characters += [[scene, matched_character.group()]]
                           break
        list_nonspeaking_characters = sorted(list_nonspeaking_characters)
        index = 0
        while index < len(list_nonspeaking_characters):
            for scene, content in dict_scenes.items():
                for item in content:
                    if item[0] == 'Character':
                        if int(list_nonspeaking_characters[index][0]) == scene:
                            if item[1] == list_nonspeaking_characters[index][1]:
                                del list_nonspeaking_characters[index]
                                index = index - 1
                                break
            index = index + 1
        return list_nonspeaking_characters
############################################################################     
class Scene(object):
    
    def dict_scenes(self, root):
        paragraphs = list(root.find("paragraphs"))
        list_scenes = dict()
        content = []
        sn = 0
        for para in paragraphs:
            item_text = ''
            for item in para:
                if item.tag == "style":
                    item_type = item.get("basestylename")
                    if item_type == "Scene Heading":
                        sn += 1
                        content = []
                elif item.tag == 'text':
                    if item.text != None:
                        item_text += item.text
            content += [[item_type, item_text]]
            list_scenes.update({sn: content})  
        return list_scenes
    
    def list_actions(self, list_tuple_elements):
        actions_in_scene = list(filter(lambda x:x[0] == "Action", list_tuple_elements))
        actions_in_scene = list(map(lambda x:x[1], actions_in_scene))
        return actions_in_scene
    
    def list_characters(self, root, scene_number=0, include_nonspeaking=False):
        parser = Parse()
        gen = Generate()
        dict_scenes = self.dict_scenes(root)
        list_tuple_element = dict_scenes[scene_number]
        characters_in_scene = list(filter(lambda x:x[0] == "Character", list_tuple_element))
        characters_in_scene = list(map(lambda x:x[1], characters_in_scene))
        for index, character in enumerate(characters_in_scene):
            characters_in_scene[index] = parser.character(character)[0]
        characters_in_scene = list(set(tuple(characters_in_scene)))
        if include_nonspeaking:
            list_nonspeaking_characters = gen.list_nonspeaking_characters(root)
            nonspeaking_in_scene = list(filter(lambda x:int(x[0]) == scene_number, list_nonspeaking_characters))
            if nonspeaking_in_scene != 0:
                for each in nonspeaking_in_scene:
                    characters_in_scene += [each[1]] 
        return characters_in_scene
############################################################################        
class Parse(object):
        
    def scene_heading(self, str_heading, lang="EN"):
        if lang == "EN":
            part_intext = ['INT.', 'EXT.', r'INT/EXT.', r'INT./EXT.']
            part_timeofday = ['DAY', 'DAYS LATER', 
                              'EVENING', 'EARLY EVENING',
                              'MORNING', 'DAWN',
                              'NIGHT',
                              'CONTINUOUS', 'SAME TIME', 'MOMENTS LATER',
                              'DREAM']    
        if lang == "CN":
            part_intext = [u'内.', u'外.', u'内/外.', u'内./外.']
            part_timeofday = ['日', '早晨', '清晨',
                              '夜', '傍晚', 
                              '片刻后', '几天后',
                              '同上', '续上', '梦境']            
#        str_heading = list_headings[5]
        for text in part_intext:
            comp = re.compile(text)
            part1 = comp.match(str_heading)
            part2 = str_heading
            if part1 != None:
                part1 = text.rstrip('.')
                part2 = str_heading.lstrip(text).lstrip(' ')
                break
        for text in part_timeofday:
            comp = re.compile(text)
            part3 = comp.search(part2)
            if part3 != None:
                part3 = text
                part2 = part2.rstrip(' ').rstrip(text).rstrip(' ').rstrip('-').rstrip(' ')
                break
            else:
                part3 = ''
        list_heading_separated = []
        list_heading_separated = part1, part2, part3
        return list_heading_separated
    
    def character(self, str_character):
#        str_character = '新闻记者#4（画外）'
        str_character = re.sub('（', '(', str_character)
        str_character = re.sub('）', ')', str_character)
        str_to_match = '\(.*\)'
        str_character_matched = re.search(str_to_match, str_character)
        character = [str_character, '']
        if str_character_matched != None:
            character_extension = str_character_matched.group(0)
            str_character = str_character.rstrip(character_extension)
            character_extension = character_extension.lstrip('(').rstrip(')')
            character = [str_character, character_extension]
        return character
############################################################################         
