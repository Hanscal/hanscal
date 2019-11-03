# coding:utf-8

from PIL import Image, ImageDraw
import os, sys, random, math
from libs.content_generator import ContentGenerator
# from libs.draw_form import DrawForm
from libs.font_selector import FontSelector
# from libs.position_selector import PositionSelector
# from libs.text_paster import TextPaster
from libs.bg_generator import BgGenerator
from libs.special_draw import SpecialDraw
import imgaug as ia
from imgaug import augmenters as iaa
import numpy as np
from utils import data_utils
import optparse, time

def get_background_file_list(bg_dir):
    bg_path_list = []
    file_list = os.listdir(bg_dir)
    for file_name in file_list:
        if file_name[-3:] == 'jpg':
            bg_path_list.append(os.path.join(bg_dir, file_name))
    return bg_path_list

def random_min_form_size():
    w = random.randint(100, 250)
    h = random.randint(20, 40)
    return w, h

def reg_aug(img):
    if random.random() < 0.1:
        return img
    np_img = np.array(img)
    seq = iaa.SomeOf((1,3), [
            iaa.Noop(),
            # iaa.Noop(),
            # iaa.PiecewiseAffine(scale=(0.01, 0.02)),
            iaa.GaussianBlur(sigma=(0.3, 0.8)),
            iaa.Add((-40, 40)),
            iaa.AdditiveGaussianNoise(scale=(0, 0.1*255)),
            iaa.Dropout(p=(0, 0.05)),
            # iaa.Affine(rotate=(-2, 2), cval=0, mode='constant')
        ])
    img_aug = seq.augment_image(np_img)
    img = Image.fromarray(img_aug)
    return img

def reg_aug_strong(img):
    if random.random() < 0.1:
        return img
    np_img = np.array(img)
    sometimes = lambda aug: iaa.Sometimes(0.1,aug)
    seq = iaa.Sequential([
        iaa.SomeOf((1,3), [
            iaa.Noop(),
            # iaa.Noop(),
            # iaa.PiecewiseAffine(scale=(0.01, 0.02)),
            iaa.GaussianBlur(sigma=(0.3, 0.8)),
            iaa.Add((-40, 40)),
            iaa.AdditiveGaussianNoise(scale=(0, 0.1*255)),
            # iaa.Affine(rotate=(-2, 2), cval=0, mode='constant')
        ]),
        # 第一个是crop上面像素，第三个是crop下面像素,if tuple then 0-5 random
        sometimes(iaa.Crop(px=(0,5))),
        sometimes(iaa.PiecewiseAffine(scale=(0, 0.005))),
        sometimes(iaa.Invert(0.5))   # 黑白通道反向
        ])
    img_aug = seq.augment_image(np_img)
    img = Image.fromarray(img_aug)

    return img

def run(options):
    if not os.path.exists(options.output_dir):
        os.makedirs(options.output_dir)
    bg_path_list = get_background_file_list(options.bg_dir)

    bg_gen = BgGenerator(options.bg_dir, options.config)
    ct_gen = ContentGenerator(options.config)
    font_gen = FontSelector(options.font_dir, options.font_chars, options.config)
    sp_draw = SpecialDraw(options.config)
    count = 0
    start_time = time.time()
    reg_writer = open(os.path.join(options.output_dir, 'label.txt'), 'w', encoding='utf-8')
    while count < options.gen_number:
        bg_img = bg_gen.get_background_img()
        text_list = ct_gen.process()
        # font_name = font_gen.get_all_ch_font_name()
        # font_size = font_gen.get_font_size()
        # font_color = font_gen.get_font_color()
        crop_img, text = sp_draw.process(text_list, bg_img, font_gen)
        if crop_img is None:
            continue
            # + font_path.decode('utf-8')
        data_utils.save_reg_data(options.output_dir, options.pre_fix + str(count), crop_img, text , reg_aug_strong, reg_writer)
        count += 1

        if count % 10 == 0:
            print ('{}/{}'.format(count, options.gen_number))
            cost_time = time.time() - start_time
            print ('cost time:{:.2f}, mean time: {:.2f}, exp time:{:.2f}'.format(cost_time, cost_time/count, (cost_time/count)*(options.gen_number - count)))
            sys.stdout.flush()

    reg_writer.close()


def get_options(args=None):
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('--config', type=str, default='/Volumes/work/build-tools/ocr-recognition-datamaker/src/config/config_local.yaml', help='define the content config file')
    opt_parser.add_option('--bg_dir', type=str, default='/Volumes/work/build-tools/text_renderer/data/bg', help='define the background dir')
    opt_parser.add_option('--font_dir', type=str, default='/Volumes/work/build-tools/text_renderer/data/fonts', help='define the fonts dir')
    opt_parser.add_option('--font_chars', type=str, default='/Volumes/work/build-tools/text_renderer/data/fonts_char.json', help='define the fonts have chars')
    opt_parser.add_option('--gen_number', type=int, default=100, help='define the generate number')
    opt_parser.add_option('--output_dir', type=str, default='/Volumes/work/build-tools/ocr-recognition-datamaker/run_shs/output', help='define the output dir')
    opt_parser.add_option('--pre_fix', type=str, default='p', help='define the output file prefix str')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)
