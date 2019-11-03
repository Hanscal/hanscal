# coding: utf-8

import os
import sys
import optparse
from PIL import Image, ImageDraw, ImageFont

def load_charsets(charset_path):
    char_list = []
    with open(charset_path, 'r', encoding='utf-8') as f:
        result = f.read().strip('\n')
    for c in result:
        char_list.append(c)
    char_list.sort()
    return ''.join(char_list)

def get_text_size(text, font):
    img_t = Image.new("RGBA", (1,1))
    draw_t = ImageDraw.Draw(img_t)
    w, h = draw_t.textsize(text, font=font)
    return w, h

def run(options):
    if not os.path.exists(options.output_dir):
        os.makedirs(options.output_dir)

    file_name_list = os.listdir(options.input_fonts_dir)
    print (file_name_list)
    charsets = load_charsets(options.charset_path)
    one_line_char = 40
    font_size = 20
    font_color = (0, 0, 0)
    bg_w = one_line_char*font_size
    rows = int(len(charsets)/one_line_char) + 1
    bg_h = font_size*rows
    # print ('charsets:')
    # print (charsets)
    print ('one_line_char:{}, font_size:{}, rows: {}'.format(one_line_char, font_size, rows))
    for file_name in file_name_list:
        if file_name == '.ttf':
            continue
        print (file_name)
        bg_img = Image.new('RGB', (bg_w, bg_h), (255, 255, 255))
        font_path = os.path.join(options.input_fonts_dir, file_name)
        try:
            font = ImageFont.truetype(font_path, font_size)
        except Exception as e:
            print ("can't load font: {}, ignored.".format(font_path))
            continue
        draw = ImageDraw.Draw(bg_img)
        for i in range(rows):
            paste_text_row = ''
            for j in range(one_line_char):
                s = i*one_line_char
                # e = (i+1)*one_line_char
                if s + j > len(charsets):
                    break
                # e = min(e, len(charsets))
                paste_text = charsets[s+j:s+j+1]
                paste_text_row +=paste_text
                try:
                    draw.text((j*font_size, i*font_size), paste_text, font=font, fill=font_color)
                except IOError as error:
                    print(error,paste_text)
            # t_w, t_h = get_text_size(paste_text_row, font)
            # draw.line((t_w, i*font_size, t_w, i*font_size + t_h), fill=(255, 0, 0), width=1)
        bg_img.save(os.path.join(options.output_dir, file_name[:-4] + '.jpg'))

def get_options(args=None):
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('-i', '--input_fonts_dir', type=str, default='./subset_fonts', help='define the input dir of fonts')
    opt_parser.add_option('-o', '--output_dir', type=str, default='./draw_fonts', help='define the output dir')
    opt_parser.add_option('-c', '--charset_path', type=str, default='./word_sets/words.txt', help='define the charset_path')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)