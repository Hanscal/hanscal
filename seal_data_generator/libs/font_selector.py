# coding:utf-8

from PIL import Image, ImageDraw, ImageFont
import yaml
import os, sys, random, math
import json

class FontSelector(object):
    """docstring for FontSelector"""
    def __init__(self, font_dir, config_path, font_chars_path=None):
        super(FontSelector, self).__init__()
        self.font_dir = font_dir
        self.config = self.load_config(config_path)
        self.fonts_char_map = {}
        self.char_to_name_map = {}
        self.font_name_list = []
        self.load_font_chars(font_chars_path)
        self.font_chars_path = font_chars_path
        self.font_caches = {}

    def load_font_chars(self, font_chars_path):
        if font_chars_path is None:
            self.font_name_list = os.listdir(self.font_dir)
            self.font_name_list = [v for v in self.font_name_list if v[-4:] == '.ttf']
            return
        with open(font_chars_path, 'r', encoding='utf-8') as f:
            data_str = f.read()
            self.fonts_char_map = json.loads(data_str)
        self.font_name_list = []
        self.char_to_name_map = {}
        for name, chars in self.fonts_char_map.items():
            self.font_name_list.append(name)
            for c in chars:
                if c not in self.char_to_name_map:
                    self.char_to_name_map[c] = {}
                self.char_to_name_map[c][name] = True

    def load_config(self, config_path):
        result = None
        with open(config_path, 'r') as f:
            content = f.read()
            result = yaml.load(content)

        return result

    def get_font_name_by_text(self, text):
        n = len(self.font_name_list)
        if self.font_chars_path is None:
            return self.font_name_list[random.randint(0, n - 1)]
        # for c in text:
        is_all_ch_exists = False
        search_times = 10
        while not is_all_ch_exists:
            font_name = self.font_name_list[random.randint(0, n - 1)]
            is_all_ch_exists = True
            for c in text:
                if (c not in self.char_to_name_map) or \
                    (font_name not in self.char_to_name_map[c]):
                    is_all_ch_exists = False
                    break
            search_times -= 1
            if search_times == 0:
                return None
        return font_name

    def get_font_path_by_name(self, font_name):
        return os.path.join(self.font_dir, font_name)

    def get_font_size(self):
        return random.randint(self.config['min_font_size'], self.config['max_font_size'])

    def get_font_color(self):
        rgb_range = [(200, 255), (0, 10), (0, 10)]
        c_list = []
        for i in range(3):
            v = random.randint(rgb_range[0], rgb_range[1])
            c_list.append(v)
        return tuple(c_list)

    def get_font(self, text=None, font_path=None, font_size=None):
        if text is None:
            text = ''
        if font_path is None:
            font_name = self.get_font_name_by_text(text)
            font_path = self.get_font_path_by_name(font_name)
        if font_size is None:
            font_size = self.get_font_size()
        hash_str = "{}_{}".format(font_path, font_size)
        if hash_str in self.font_caches:
            return self.font_caches[hash_str], font_path, font_size
        self.font_caches[hash_str] = ImageFont.truetype(font_path, font_size)
        return self.font_caches[hash_str], font_path, font_size

if __name__ == '__main__':
    from content_generator import ContentGenerator
    content_gen = ContentGenerator('../configs/seal_config.yaml')
    font_gen = FontSelector('../fonts','../configs/seal_config.yaml')
    for i in range(10):
        text = content_gen.process()
        font, font_path, font_size = font_gen.get_font(text)
        print(font_path, font_size)
