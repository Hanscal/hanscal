# coding: utf-8

from .font_selector import FontSelector
from . import drawer
from . seal_base import SealBase
from PIL import Image, ImageDraw
from imgaug import augmenters as iaa
import random

class SealDoubleCircle(SealBase):
    """docstring for SealDoubleCircle"""
    def __init__(self, config_path):
        super(SealDoubleCircle, self).__init__(config_path)
        self.content_generator.max_content_length = self.config['seal_double_circle']['max_content_length']
        self.english_chars = 'abcdefghijklmnopqrstuvwxyz'

    def generate_english_words(self):
        word_num = random.randint(1, self.config['seal_double_circle']['max_english_word_num'])
        english_text = ''
        for _ in range(word_num):
            char_num = random.randint(3, self.config['seal_double_circle']['max_english_char_num'])
            word = ''
            for _ in range(char_num):
                word += self.english_chars[random.randint(0, 25)]
            if random.random() < 0.5:
                word = word[0].upper() + word[1:]
            if len(english_text) > 0:
                english_text += " "
            english_text += word
        return english_text

    def process(self):
        W = self.config['image_width']
        H = self.config['image_height']
        bg_img = drawer.get_empty_img(W, H, 0)

        color = self.get_color()
        center = (W // 2, H // 2)

        # draw circle1
        circle_area1 = self.get_circle_area(center, 'seal_double_circle')
        circle_width = random.randint(self.config['seal_double_circle']['min_circle_width'],
                                        self.config['seal_double_circle']['max_circle_width'])
        drawer.draw_circle(bg_img, circle_area1, color=color, width=circle_width)

        #draw circle2
        circle_area2 = self.get_circle_area(center, 'seal_double_circle', radius_suffix='2')
        drawer.draw_circle(bg_img, circle_area2, color=color, width=circle_width//2)

        # draw star
        if random.random() < self.config['seal_double_circle']['draw_star_ratio']:
            star_radius = random.randint(self.config['seal_double_circle']['min_star_radius'],
                                        self.config['seal_double_circle']['max_star_radius'])
            drawer.draw_five_pointed_star(bg_img, center, star_radius, color)
        
        bg_img = self.aug_background(bg_img)

        # draw word
        text = self.content_generator.process()
        font_size = random.randint(self.config['min_font_size'], self.config['seal_double_circle']['max_font_size'])
        font, _, _ = self.font_gen.get_font(text, font_size=font_size)
        max_r = (circle_area2[2] - circle_area2[0])/2 - circle_width / 2
        word_r = max_r - font_size / 2 - 5
        interval_angle = random.randint(self.config['seal_double_circle']['min_interval_angle'], 
                                        self.config['seal_double_circle']['max_interval_angle'])
        drawer.draw_circle_word(text, bg_img, center, word_r, font, color, interval_angle)

        # draw english word
        eng_text = self.generate_english_words()
        font_size = random.randint(14, self.config['seal_double_circle']['max_eng_font_size'])
        font, _, _ = self.font_gen.get_font(eng_text, font_size=font_size)
        max_r = (circle_area1[2] - circle_area1[0]) / 2 - circle_width / 2
        word_r = max_r - font_size / 2 - 4
        interval_angle = random.randint(self.config['seal_double_circle']['min_eng_interval_angle'], 
                                        self.config['seal_double_circle']['max_eng_interval_angle'])
        drawer.draw_circle_word(eng_text, bg_img, center, word_r, font, color, interval_angle)
        
        bg_img = self.aug_all(bg_img)
        return bg_img, text