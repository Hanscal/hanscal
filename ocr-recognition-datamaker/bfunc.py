# -*- coding:utf-8 -*-

'''
author: "caihua"
date: 2019/7/11
Email: hanscalcai@163.com
'''

import cv2
import os
import xml.etree.ElementTree as ET
import json

def resize_bgimg(input_dir):
    bg_list = os.listdir(input_dir)
    for bg in bg_list:
        if bg.endswith('.jpg'):
            bg_path = os.path.join(input_dir,bg)
            img = cv2.imread(bg_path)
            h,w = img.shape[:2]
            print('image:{} height:{} and width:{}'.format(bg,h,w))
            img_resize = cv2.resize(img,(800,100),cv2.INTER_CUBIC)
            img_save_name = bg_path[:-4]+'_re.jpg'
            cv2.imwrite(img_save_name,img_resize)

def load_charsets(charset_path):
    charset_dict = {}
    with open(charset_path, 'r', encoding='utf-8') as f:
        result = f.read().strip('\n')
    for i, c in enumerate(result):
        charset_dict[c] = i
    return charset_dict

def gen_ttx(input_fonts_dir):
    pass

def gen_font_charset(input_ttx_dir,charset_path,output_path):
    file_name_list = os.listdir(input_ttx_dir)
    charset_dict = load_charsets(charset_path)
    result = {}
    for file_name in file_name_list:
        # file_name = 'Bodoni.ttf'
        file_path = os.path.join(input_ttx_dir, file_name)
        print('analyz {}'.format(file_path))
        try:
            tree = ET.parse(file_path)
            root = tree.getroot()
        except Exception as e:
            print(e)
            continue
        cmap = root.find('cmap')
        map_list = cmap.find('cmap_format_4')
        exist_chars = ''
        if map_list is None:
            continue
        for map_item in map_list:
            ch_code = map_item.get('code')
            ch = chr(int(ch_code, 16))
            if ch in charset_dict:
                exist_chars += ch
        result[file_name[:-3] + 'ttf'] = exist_chars
    with open(output_path, 'w', encoding='utf-8') as f:
        json_str = json.dumps(result, ensure_ascii=False, indent=4)
        f.write(json_str)

if __name__=='__main__':
    input_bg_dir = '/Volumes/work/build-tools/ocr-recognition-datamaker/text_renderer/data/bg'
    # resize_bgimg(input_bg_dir)

    input_ttx_dir = '/Volumes/work/build-tools/ocr-recognition-datamaker/text_renderer/data/fonts_ttx'
    charset_path = '/Volumes/work/build-tools/ocr-recognition-datamaker/text_renderer/data/chars/table_charset.txt'
    output_path = '/Volumes/work/build-tools/ocr-recognition-datamaker/text_renderer/data/fonts_char1.json'
    gen_font_charset(input_ttx_dir, charset_path, output_path)