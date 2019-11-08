# coding: utf-8
from libs import seal_base
from libs import seal_double_circle
from libs import bg_generator
from libs import drawer
from libs import nois_text
import os, sys
import random
import numpy as np
import optparse, time

def save_data(output_dir, save_name , img, text, writer):
    img.save(os.path.join(output_dir, save_name + '.png'), quality=95)
    writer.write('{}.png {}\n'.format(save_name, text))

def run(options):
    if not os.path.exists(options.output_dir):
        os.makedirs(options.output_dir)

    # seal_gen = seal_base.SealBase(options.config)
    seal_gens = [seal_base.SealBase(options.config),
                seal_double_circle.SealDoubleCircle(options.config)]
    seal_gens[0].init_fonts(options.font_dir)
    for i in range(1,len(seal_gens)):
        seal_gens[i].font_gen = seal_gens[0].font_gen
        seal_gens[i].content_generator = seal_gens[0].content_generator
    # seal_gen = seal_double_circle.SealDoubleCircle(options.config)
    # seal_gen.init_fonts(options.font_dir)
    bg_gen = bg_generator.BgGenerator(options.bg_dir, options.config)

    nois_gen = nois_text.NoisTextGenerator(options.nois_config)
    nois_gen.init_fonts(options.font_dir)

    count = 0
    start_time = time.time()
    label_writer = open(os.path.join(options.output_dir, 'label.txt'), 'w')

    while count < options.gen_number:
        bg_img = bg_gen.get_background_img().convert('RGBA')
        seal_gen = seal_gens[random.randint(0, len(seal_gens) - 1)]
        seal_img, text = seal_gen.process()
        text_img_list = nois_gen.process()
        # for text_img in text_img_list:
        #     drawer.random_paste(bg_img, text_img)
        drawer.random_paste(bg_img, seal_img)
        save_name = '{}_{}'.format(options.pre_fix, count)
        save_data(options.output_dir, save_name, bg_img, text, label_writer)
        count += 1

        if count % 1 == 0:
            print ('{}/{}'.format(count, options.gen_number))
            cost_time = time.time() - start_time
            print ('cost time:{:.2f}, mean time: {:.2f}, exp time:{:.2f}'.format(cost_time, cost_time/count, (cost_time/count)*(options.gen_number - count)))
            sys.stdout.flush()

    label_writer.close()




def get_options(args=None):

    opt_parser = optparse.OptionParser()
    opt_parser.add_option('--config', type=str,
                          default='/Volumes/work/personal/hanscal/ocr-recognition-datamaker/src/config/seal_config.yaml',
                          help='define the content config file')
    opt_parser.add_option('--nois_config', type=str, default='/Volumes/work/personal/hanscal/ocr-recognition-datamaker/src/config/seal_config.yaml',
                          help='define the content config file')
    opt_parser.add_option('--bg_dir', type=str, default='./testdata/bgs',
                          help='define the background dir')
    opt_parser.add_option('--font_dir', type=str, default='/Volumes/work/build-tools/all_fonts/',
                          help='define the fonts dir')
    opt_parser.add_option('--font_chars', type=str, default='/Volumes/work/build-tools/all_fonts/pt_fonts_char.json',
                          help='define the fonts have chars')
    opt_parser.add_option('--gen_number', type=int, default=100, help='define the generate number')
    opt_parser.add_option('--output_dir', type=str, default='./testdata/', help='define the output dir')
    opt_parser.add_option('--pre_fix', type=str, default='p', help='define the output file prefix str')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)