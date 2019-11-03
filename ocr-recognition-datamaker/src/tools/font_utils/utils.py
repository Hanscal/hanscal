# -*- coding:utf-8 -*-

'''
author: "caihua"
date: 2019/10/11
Email: hanscalcai@163.com
'''

# coding: utf-8

import os
import sys
import shutil
import json
import optparse

def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        result = json.loads(f.read())
        return result

def conbine_json_data(json_path1,json_path2,output_path):
    data1 = load_json_data(json_path1)
    data2 = load_json_data(json_path2)
    result = {}

    for font_name, chars in data1.items():
        result[font_name] = chars
    for font_name, chars in data2.items():
        result[font_name] = chars

    with open(output_path, 'w', encoding='utf-8') as f:
        json_str = json.dumps(result, ensure_ascii=False, indent=4)
        f.write(json_str)


def copy_selected_fonts(input_dir,file_name_config,output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    file_name_list = load_json_data(file_name_config)
    for file_name in file_name_list:
        src_file = os.path.join(input_dir, file_name)
        tgt_file = os.path.join(output_dir, file_name)
        shutil.copy(src_file, tgt_file)