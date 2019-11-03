# -*- coding:utf-8 -*-

'''
author: "caihua"
date: 2019/10/11
Email: hanscalcai@163.com
'''


import os
import sys
import json
import shutil
import optparse
from fontTools.subset import main as ss


def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        result = json.loads(f.read())
        return result

def save_json_data(file_path, data):
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))

def get_file_name_list(root_dir, suffixs):
    result = []
    file_list = os.listdir(root_dir)
    for file_name in file_list:
        if file_name[-3:] in suffixs:
            result.append(file_name)
    return result

def run(options):
    if not os.path.exists(options.output_font_dir):
        os.makedirs(options.output_font_dir)

    # get font name list
    suffixs = ['otf','ttf']
    new_fonts = []
    if len(options.input_font_dir) > 0:
        new_fonts = get_file_name_list(options.input_font_dir, suffixs)
    else:
        print('please cheack the input fonts dir')
        os._exit(-1)
    new_fonts = list(set(new_fonts))

    # copy selected fonts to certain dir, can be deleted
    # tmp_font_folder = os.path.join(options.output_dir,'origin_font')
    # if not os.path.exists(tmp_font_folder):
    #     os.makedirs(tmp_font_folder)
    #
    # for file_name in new_fonts:
    #     src_file = os.path.join(options.input_dir, file_name)
    #     tgt_file = os.path.join(tmp_font_folder, file_name)
    #     shutil.copy(src_file, tgt_file)

    # make subsets fonts
    subset_save_dir = os.path.join(options.output_font_dir,'subset_fonts')
    if not os.path.exists(subset_save_dir):
        os.makedirs(subset_save_dir)
    select_font_name = os.path.join(subset_save_dir, 'font_name_selected.json')
    save_json_data(select_font_name, new_fonts)

    for file_name in new_fonts:
        # 'use this script like: \nbash make_subset_fonts.sh font_file.ttf --text-file=word_set.txt --output-file=new_font.ttf'
        new_file_name = os.path.join(subset_save_dir,file_name)
        file_path = os.path.join(options.input_font_dir,file_name)
        print('subset of {}'.format(new_file_name))
        # os.system('pyftsubset %s --text-file=%s --output-file=%s'%(file_path,options.subcharset_path,new_file_name))
        sys.argv = [None,file_path,'--text-file={}'.format(options.subcharset_path),'--output-file=%s'%(new_file_name)]
        if not os.path.exists(new_file_name):
            ss()

def get_options(args=None):
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('-i', '--input_font_dir', type=str, default='/data/caihua/data/fonts/printing/ttf', help='')
    opt_parser.add_option('-c', '--subcharset_path', type=str, default='/data/caihua/scripts/ocr-recognition-datamaker/datas/charsets/charset_v1.txt', help='')
    opt_parser.add_option('-o', '--output_font_dir', type=str, default='/data/caihua/data/fonts/printing/json', help='')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)