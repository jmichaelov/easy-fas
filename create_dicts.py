#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 11:34:11 2022

@author: james
"""

# Opens files from http://rali.iro.umontreal.ca/rali/?q=en/Textual%20Resources and saves as dicts

from io import BytesIO
from zipfile import ZipFile
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import json

usffan_link = urlopen("http://rali.iro.umontreal.ca/rali/sites/default/files/resources/usf-fan/cue-target.xml.zip")
zipfile = ZipFile(BytesIO(usffan_link.read()))
with zipfile.open("cue-target.xml") as f:
    usffan_tree = ET.parse(f)
usffan_root = usffan_tree.getroot()


usffan_dict = dict()

for i in range(len(usffan_root)):
    cue_element = usffan_root[i]
    cue_word = cue_element.attrib["word"]
    total_responses = cue_element[0].attrib["g"]
    usffan_dict[cue_word] = {"_count":int(total_responses)}
    for j in range(len(cue_element)):
        response_element = cue_element[j]
        response_word = response_element.attrib["word"]
        response_count = response_element.attrib["p"]
        usffan_dict[cue_word][response_word] = {"_count":int(response_count)}
        
with open("usffan_dict.json","w") as f:
    json.dump(usffan_dict,f)

eat_link = urlopen("http://rali.iro.umontreal.ca/rali/sites/default/files/resources/eat/eat-stimulus-response.xml.zip")
zipfile = ZipFile(BytesIO(eat_link.read()))
with zipfile.open("eat-stimulus-response.xml") as f:
    eat_tree = ET.parse(f)

eat_root = eat_tree.getroot()


eat_dict = dict()

for i in range(len(eat_root)):
    cue_element = eat_root[i]
    cue_word = cue_element.attrib["word"]
    total_responses = cue_element.attrib["all"]
    eat_dict[cue_word] = {"_count":int(total_responses)}
    for j in range(len(cue_element)):
        response_element = cue_element[j]
        response_word = response_element.attrib["word"]
        response_count = response_element.attrib["n"]
        eat_dict[cue_word][response_word] = {"_count":int(response_count)}

with open("eat_dict.json","w") as f:
    json.dump(eat_dict,f)

