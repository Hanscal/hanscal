# coding: utf-8

import os, sys, random
import yaml
from PIL import Image, ImageDraw

class BgGenerator(object):
    """docstring for BgGenerator"""
    def __init__(self, background_dir, config_path):
        super(BgGenerator, self).__init__()
        self.config = self.load_config(config_path)
        self.img_path_list = self.load_backgrounds(background_dir)
        self.now_img_path_id = 0
        self.max_img_cache = 320
        self.bg_list = []

    def load_config(self, config_path):
        result = None
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            result = yaml.load(content)

        return result

    def load_backgrounds(self, background_dir):
        result = []
        file_list = os.listdir(background_dir)
        target_suffix = ['jpg', 'png']
        for file_name in file_list:
            if file_name[-3:] in target_suffix:
                result.append(os.path.join(background_dir, file_name))
        return result

    def get_bg_img(self):
        n = len(self.bg_list)
        m = len(self.img_path_list)
        res_img = None
        if self.now_img_path_id < n:
            res_img = self.bg_list[self.now_img_path_id]
        else:
            img_path = self.img_path_list[self.now_img_path_id]
            res_img = Image.open(img_path)
            if n < self.max_img_cache:
                self.bg_list.append(res_img)
        self.now_img_path_id = (self.now_img_path_id + 1) % m
        return res_img

    def get_background_img(self):
        target_w = self.config['image_width']
        target_h = self.config['image_height']
        target_w = random.randint(target_w, int(target_w*1.5))
        target_h = random.randint(target_h, int(target_h*1.5))

        target_img = self.get_bg_img()
        W, H = target_img.size
        target_w = min(target_w, W)
        target_h = min(target_h, H)
        min_x = 0
        max_x = W - target_w
        min_y = 0
        max_y = H - target_h
        x1 = random.randint(min_x, max_x)
        y1 = random.randint(min_y, max_y)
        return target_img.crop((x1, y1, x1 + target_w, y1 + target_h))