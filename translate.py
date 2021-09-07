# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 17:48:11 2020

@author: VSurfacePro3
"""

#%% Function Baidu Translation
import hashlib
from random import randint
import http.client
import urllib
import json

#%%
class Translate(object):
    
    def __init__(self, sc: str = None):   
        super(Screenplay, self).__init__()
        
    def Baidu(str_to_trans='apple', lang_from='zh', lang_to='en'):
        time.sleep(2)
        #path_translink = 'http://api.fanyi.baidu.com/api/trans/vip/translate'
        path_translink = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
        httpClient = None
        
        appid = '20200218000385369'
        passcode = 'phecLsPI8EnkvjRHQ8HU'
        salt = randint(1e9, 9e9)
        q = str_to_trans
        for_sign = appid + q + str(salt) + passcode
        sign = hashlib.md5(for_sign.encode()).hexdigest()
        
        link_query = (path_translink + '?'
                      + 'appid=' + appid +'&'
                      + 'q=' + urllib.parse.quote(q) + '&'
                      + 'from=' + lang_from + '&'
                      + 'to=' + lang_to + '&'
                      + 'salt=' + str(salt) + '&'
                      + 'sign=' + sign)
        
        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', link_query)
    
            # response是HTTPResponse对象
            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)
            print(result['trans_result'][0]['dst'])
            return result['trans_result'][0]['dst']  # str
    
        except Exception as e:
            print(e)
        finally:
            if httpClient:
               httpClient.close() 

