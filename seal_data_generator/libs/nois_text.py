# coding: utf-8

from .content_generator import ContentGenerator
from .font_selector import FontSelector
from . import drawer
from PIL import Image, ImageDraw
from imgaug import augmenters as iaa
import numpy as np
import random
import yaml

class NoisTextGenerator(object):
    """docstring for NoisTextGenerator"""
    def __init__(self, config_path):
        super(NoisTextGenerator, self).__init__()
        self.config_path = config_path
        self.config = self.load_config(config_path)
        self.content_generator = ContentGenerator(config_path)
        self.font_gen = None

    def load_config(self, config_path):
        result = None
        with open(config_path, 'r') as f:
            content = f.read()
            result = yaml.load(content)

        return result

    def init_fonts(self, font_dir, font_chars_path=None):
        self.font_gen = FontSelector(font_dir, self.config_path, font_chars_path)

    def get_color(self):
        rgb_range = [(0, 80), (0, 80), (0, 80)]
        c_list = []
        for i in range(3):
            v = random.randint(rgb_range[i][0], rgb_range[i][1])
            c_list.append(v)
        return tuple(c_list)

    def aug_text_img(self, img):
        np_img = np.array(img)
        seq = iaa.SomeOf((1, 3), [
                iaa.GaussianBlur(sigma=(0.0, 2.0)),
                iaa.AverageBlur(k=((5, 11), (1, 3))),
                iaa.PiecewiseAffine(scale=(0.01, 0.03)),
                iaa.Noop(),
            ])
        img_aug = seq.augment_image(np_img)
        img = Image.fromarray(img_aug)
        return img

    def process(self):
        gen_num = random.randint(0, self.config['max_gen_number'])
        text_img_list = []
        for i in range(gen_num):
            text = self.content_generator.process()
            font, font_path, font_size = self.font_gen.get_font(text)
            font_color = self.get_color()
            word_img = drawer.get_word_img(text, font, font_color, is_decorate=False)
            text_img_list.append(word_img)
        return text_img_list