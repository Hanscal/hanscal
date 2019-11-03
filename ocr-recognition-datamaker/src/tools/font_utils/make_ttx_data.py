# -*- coding:utf-8 -*-

'''
author: "caihua"
date: 2019/10/11
Email: hanscalcai@163.com
'''

import sys
import os
import optparse

def run(options):
    suffixs = ['otf','ttf']
    print('make ttx data only for .otf and .ttf format input fonts')
    if not os.path.exists(options.output_ttx_dir):
        os.makedirs(options.output_ttx_dir)
    for suffix in suffixs:
        for file in os.listdir(options.input_font_dir):
            if not file.endswith(suffix):
                continue
            ttf_file_name = os.path.join(options.input_font_dir,file)
            ttx_file_name = os.path.join(options.output_ttx_dir,file[:-3]+'ttx')
            #对于已经生成的ttx文件跳过
            if os.path.exists(ttx_file_name):
                print('{} ttx file exists'.format(ttx_file_name))
                continue
            os.system('ttx -o %s %s'%(ttx_file_name,ttf_file_name))

def get_options(args=None):
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('-i', '--input_font_dir', type=str, default='', help='')
    opt_parser.add_option('-o', '--output_ttx_dir', type=str, default='', help='')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)