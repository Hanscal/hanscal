# -*- coding:utf-8 -*-

'''
author: "caihua"
date: 2019/11/6
Email: caihua@datagrand.com
'''

from .content_generator import ContentGenerator
from .font_selector import FontSelector
from .sp_utils import seal_util as drawer
from PIL import Image, ImageDraw
from imgaug import augmenters as iaa
import numpy as np
import random
import yaml

class SealBase(object):
    """docstring for SealBase"""
    def __init__(self, config_path):
        super(SealBase, self).__init__()
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

    def get_circle_area(self, center, seal_name='seal_base', radius_suffix=''):
        r = random.randint(self.config[seal_name]['min_radius' + radius_suffix],
                            self.config[seal_name]['max_radius' + radius_suffix])

        area = [center[0] - r, center[1] - r, center[0] + r, center[1] + r]
        return area

    def get_color(self):
        rgb_range = [(150, 255), (0, 70), (0, 70)]
        c_list = []
        for i in range(3):
            v = random.randint(rgb_range[i][0], rgb_range[i][1])
            c_list.append(v)
        return tuple(c_list)

    def aug_background(self, img):
        mask_img = np.array(img)
        # print(old_img.shape)
        mask_img[mask_img > 0] = 1
        np_img = np.array(img)
        seq = iaa.SomeOf((1,2), [
                iaa.Superpixels(p_replace=(0.05, 0.3), n_segments=(4, 16)),
                iaa.GaussianBlur(sigma=(0.0, 1.0)),
                iaa.AverageBlur(k=((5, 11), (1, 3))),
                iaa.CoarseDropout((0.0, 0.06), size_percent=(0.02, 0.25)),
                iaa.Noop(),
            ])
        img_aug = seq.augment_image(np_img)
        img = Image.fromarray(img_aug*mask_img)
        return img

    def aug_all(self, img):
        img = img.rotate(random.randint(0, 360))
        # mask_img = np.array(img)
        # print(old_img.shape)
        # mask_img[mask_img > 0] = 1
        # np_img = np.array(img)
        # seq = iaa.SomeOf((1,1), [
        #         iaa.PiecewiseAffine(scale=(0.01, 0.03)),
        #         iaa.Noop(),
        #     ])
        # img_aug = seq.augment_image(np_img)
        # img = Image.fromarray(img_aug)
        # *mask_img
        return img

    def process(self):
        W = self.config['image_width']
        H = self.config['image_height']
        bg_img = drawer.get_empty_img(W, H, 0)

        color = self.get_color()

        center = (W // 2, H // 2)
        # draw cicle
        circle_area = self.get_circle_area(center)
        circle_width = random.randint(self.config['seal_base']['min_circle_width'],
                                    self.config['seal_base']['max_circle_width'])
        drawer.draw_circle(bg_img, circle_area, color=color, width=circle_width)

        # draw star
        if random.random() < self.config['seal_base']['draw_star_ratio']:
            star_radius = random.randint(self.config['seal_base']['min_star_radius'],
                                        self.config['seal_base']['max_star_radius'])
            drawer.draw_five_pointed_star(bg_img, center, star_radius, color)

        bg_img = self.aug_background(bg_img)

        # draw word
        text = self.content_generator.process()
        font, font_path, font_size = self.font_gen.get_font(text)
        # min_r = star_radius + font_size / 2
        max_r = (circle_area[2] - circle_area[0])/2 - circle_width / 2
        word_r = max_r - font_size / 2 - 5
        interval_angle = random.randint(self.config['seal_base']['min_interval_angle'],
                                        self.config['seal_base']['max_interval_angle'])
        drawer.draw_circle_word(text, bg_img, center, word_r, font, color, interval_angle)

        bg_img = self.aug_all(bg_img)
        return bg_img, text
