# -*- coding:utf-8 -*-

'''
author: "caihua"
date: 2019/11/6
Email: caihua@datagrand.com
'''


import os
import math
import random
from PIL import Image, ImageDraw, ImageFont

def get_empty_img(w, h, alpha):
    return Image.new('RGBA', (w, h), (255, 255, 255, alpha))

def draw_circle(img, area, color=(255, 0, 0), width=7):
    draw = ImageDraw.Draw(img)
    draw.ellipse(area, fill=None, outline=color, width=width)

def draw_line(img, start_p, end_p, color=(255, 0, 0), width=2):
    draw = ImageDraw.Draw(img)
    draw.line(start_p + end_p, fill=color, width=width)

def draw_polygon(img, coors, color=(255, 0, 0)):
    draw = ImageDraw.Draw(img)
    draw.polygon(coors, fill=color)

def get_roated_point(center_p, end_p, angle):
    rad = math.radians(angle)
    x1, y1 = end_p[0], end_p[1]

    n_x = (x1 - center_p[0])*math.cos(rad) - (y1 - center_p[1])*math.sin(rad) + center_p[0]
    n_y = (x1 - center_p[0])*math.sin(rad) + (y1 - center_p[1])*math.cos(rad) + center_p[1]
    return (n_x, n_y)

def draw_five_pointed_star(img, center, radius, color):
    L1 = math.tan(math.radians(36)) * radius * math.sin(math.radians(36))
    L2 = math.tan(math.radians(54)) * radius * math.sin(math.radians(36))
    across_p_l = L2 - L1

    end_pos_list = [(center[0], center[1] - radius)]
    for i in range(5):
        angle = i*72
        angle2 = i*72 + 36
        if i > 0:
            end_pos_list.append(get_roated_point(center, end_pos_list[0], angle))
        end_pos_list.append(get_roated_point(center,[center[0], center[1] - across_p_l], angle2))
    draw_polygon(img, end_pos_list, color)

def decorate_word_img(img, color):
    f_w, f_h = img.size
    for i in range(f_w):
        for j in range(f_h):
            r, g, b, a = img.getpixel((i, j))
            r = min(int(r*8), color[0])
            a = min(int(a*5), 255)
            img.putpixel((i, j), (r, g, b, a))

def get_word_img(text, font, font_color, is_decorate=True):
    img = Image.new('RGBA', (1, 1))
    draw = ImageDraw.Draw(img)
    try:
        w, h = draw.textsize(text, font=font)
        img = Image.new('RGBA', (w, h), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        draw.text((0, 0), text, font=font, fill=font_color)
    except Exception as e:
        print('text, size, color', text, font, font_color)
        print('get text img error', e)
        os._exit(-1)
    if is_decorate:
        decorate_word_img(img, font_color)
    return img

def draw_circle_word(word_text, img, center, radius, font, color, interval_angle):
    word_img_list = [get_word_img(c , font, color) for c in word_text]
    total_angle = (len(word_img_list) - 1) * interval_angle
    start_angle = total_angle / 2

    word_end_p = (center[0], center[1] - radius)
    for i, word_img in enumerate(word_img_list):
        angle = start_angle - i*interval_angle
        r_img = word_img.rotate(angle)
        end_pos = get_roated_point(center, word_end_p, -angle)
        r_w, r_h = r_img.size
        img.paste(r_img, (int(end_pos[0] - r_w//2), int(end_pos[1] - r_h//2)), mask=r_img)

def random_paste(bg_img, target_img):
    W, H = bg_img.size
    w, h = target_img.size
    bg_img.paste(target_img, (random.randint(0, W - w), random.randint(0, H - h)), mask=target_img)
