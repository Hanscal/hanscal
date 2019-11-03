# -*- coding:utf-8 -*-

'''
author: "caihua"
date: 2019/10/11
Email: hanscalcai@163.com
'''

import os
import sys
import json
import optparse
import xml.etree.ElementTree as ET
import multiprocessing

def load_charsets(charset_path):
    charset_dict = {}
    with open(charset_path, 'r', encoding='utf-8') as f:
        result = f.read().strip('\n')
    for i, c in enumerate(result):
        charset_dict[c] = i
    return charset_dict

def load_json_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        result = json.loads(f.read())
        return result

def analyz_file(input_dir, file_name, charset_dict):
    file_path = os.path.join(input_dir, file_name)
    print ('analyz {}'.format(file_path))
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
    except Exception as e:
        print ('ET parse error',e)
        return (None, None)
    cmap = root.find('cmap')
    map_list = cmap.find('cmap_format_4')
    exist_chars = ''
    if map_list is None:
        return (None, None)
    for map_item in map_list:
        ch_code = map_item.get('code')
        ch = chr(int(ch_code, 16))
        if ch in charset_dict:
            exist_chars += ch
    return (file_name[:-3] + 'ttf', exist_chars)

def run(options):
    file_name_list = os.listdir(options.input_ttx_dir)
    charset_dict = load_charsets(options.charset_path)
    if len(options.font_name_list_path) > 0 and os.path.exists(options.font_name_list_path):
        file_name_list = load_json_data(options.font_name_list_path)
    file_name_list = [file_name[:-3] + 'ttx' for file_name in file_name_list]
    result = {}
    pool = multiprocessing.Pool(processes=options.process)
    run_res = []
    for file_name in file_name_list:
        run_res.append(pool.apply_async(analyz_file, (options.input_ttx_dir, file_name, charset_dict) ))

    pool.close()
    pool.join()

    for res in run_res:
        key, value = res.get()
        if key is not None:
            result[key] = value

    with open(options.output_path, 'w', encoding='utf-8') as f:
        json_str = json.dumps(result, ensure_ascii=False, indent=4)
        f.write(json_str)


def get_options(args=None):
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('-i', '--input_ttx_dir', type=str, default='./ttx_datas', help='define the input dir of ttx files')
    opt_parser.add_option('-o', '--output_path', type=str, default='./result.json', help='define the output file path')
    opt_parser.add_option('-c', '--charset_path', type=str, default='./word_sets/word.txt', help='define the charset_path')
    opt_parser.add_option('-f', '--font_name_list_path', type=str, default='', help='')
    opt_parser.add_option('-p', '--process', type=int, default=4, help='define the multiprocessing number')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)
