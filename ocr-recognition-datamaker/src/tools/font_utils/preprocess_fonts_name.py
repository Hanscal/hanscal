# coding: utf-8

import os
import shutil
import optparse
import sys

def get_file_name_list(root_dir, suffixs):
    result = []
    file_list = os.listdir(root_dir)
    for file_name in file_list:
        if file_name[-3:] in suffixs:
            result.append(file_name)
    return result

def run(options):
    suffix_list = ['ttf', 'otf', 'TTF', 'OTF']
    file_name_list = get_file_name_list(options.fonts_dir, suffix_list)

    replaced_chars = [' ', '\r', '\0', "'", "【","】","(",")"]
    for file_name in file_name_list:
        aft_file_name = file_name
        for c in replaced_chars:
            aft_file_name = aft_file_name.replace(c, '')
        src_path = os.path.join(options.fonts_dir, file_name)
        tgt_path = os.path.join(options.fonts_dir, aft_file_name[:-3] + 'ttf')
        if file_name != aft_file_name:
            shutil.move(src_path, tgt_path)
            print('move {}   to   {}'.format(file_name, aft_file_name))

def get_options(args=None):
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('-i', '--fonts_dir', type=str, default='', help='define the input dir of fonts files')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)