# coding:utf-8

from PIL import Image, ImageDraw
import yaml
import os, sys, random, math
import json

class FontSelector(object):
    """docstring for FontSelector, fonts set refer to fonts_json"""
    def __init__(self, font_dir, font_chars_path, config_path):
        super(FontSelector, self).__init__()
        # self.all_ch_font_dir = os.path.join(font_dir, 'all_ch')
        # self.sp_ch_font_dir = os.path.join(font_dir, 'sp_ch')
        # self.font_path_list = self.load_font_list()
        self.font_dir = font_dir
        # self.all_ch_font_name_list = self.load_font_list(self.all_ch_font_dir)
        # self.sp_ch_font_name_list = self.load_font_list(self.sp_ch_font_dir)
        self.config = self.load_config(config_path)
        # self.sp_word_maps = {}
        # self.init_hash_sp_word_maps()
        self.fonts_char_map = {}
        self.char_to_name_map = {}
        self.font_name_list = []
        self.load_font_chars(font_chars_path)

    def load_font_chars(self, font_chars_path):
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


    # def init_hash_sp_word_maps(self):
    #     for font_name, chs in self.special_fonts.items():
    #         for c in chs:
    #             if not self.sp_word_maps.has_key(c):
    #                 self.sp_word_maps[c] = []
    #             self.sp_word_maps[c].append(font_name)

    def load_font_list(self, font_dir):
        result = []
        font_name_list = os.listdir(font_dir)
        for font_name in font_name_list:
            if font_name[-3:] == 'ttf':
                result.append(font_name.decode('utf-8'))
        return result

    def load_config(self, config_path):
        result = None
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            result = yaml.load(content)

        return result

    # def get_font_path(self):
    #     n = len(self.font_path_list)
    #     return self.font_path_list[random.randint(0, n - 1)]

    def get_font_name_by_text(self, text):
        # for c in text:
        n = len(self.font_name_list)
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

    def get_font_size(self, is_sp=False):
        if is_sp:
            return random.randint(self.config['min_font_size'], int(self.config['min_font_size'] + 5))
        if random.random() < 0.7:
            random.randint(self.config['min_font_size'], int((self.config['min_font_size'] + self.config['max_font_size'])/2) )
        return random.randint(self.config['min_font_size'], self.config['max_font_size'])

    def get_font_color(self):
        mean_value = random.randint(0, 80)
        c_list = []
        for i in range(3):
            v = random.randint(mean_value - 10, mean_value + 10)
            v = min(255, max(v, 0))
            c_list.append(v)
        return tuple(c_list)

    def get_random_font_color(self):
        red = random.randint(0,240)
        green = random.randint(0,240)
        blue = random.randint(0,240)
        return tuple([red,green,blue])

    def get_font_red_color(self):
        mean_value = random.randint(0, 40)
        c_list = []
        c_list.append(random.randint(200,255))
        for i in range(2):
            v = random.randint(mean_value - 10, mean_value + 10)
            v = min(255, max(v, 0))
            c_list.append(v)
        return tuple(c_list)

    # def check_charcter_in_font(self, font_name, ch):
    #     if not self.special_fonts.has_key(font_name):
    #         return True
    #     for name in self.sp_word_maps[ch]:
    #         if name == font_name:
    #             return True
    #     return False

    # def get_new_special_font(self, ch):
    #     if not self.sp_word_maps.has_key(ch):
    #         return None
    #     n = len(self.sp_word_maps[ch])
    #     return self.sp_word_maps[ch][random.randint(0, n - 1)]

    # def is_special_ch(self, ch):
    #     return self.sp_word_maps.has_key(ch)
