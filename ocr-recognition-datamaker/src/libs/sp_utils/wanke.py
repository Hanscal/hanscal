# coding:utf-8

from PIL import Image, ImageDraw, ImageFont
import os, sys, random, math

l_letters = u'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
l_numbers = u'1234567890'

def is_letter(c):
    return (c in l_letters)

def is_number(c):
    return (c in l_numbers)

def check_c(c):
    return is_letter(c) or is_number(c)

def split_number_and_letter(target_text):
    max_split = 2
    sp_list = []
    last_pos = 0
    n = len(target_text)
    now_pos = 0
    while now_pos < n:
        c = target_text[now_pos]
        if max_split <= 0:
            now_pos = n
            break
        if check_c(c):
            sp_list.append((last_pos, now_pos, False) )
            if now_pos + 1 < n and \
                check_c(target_text[now_pos + 1]) and \
                random.random() < 0.5:
                sp_list.append((now_pos, now_pos + 2, True))
                last_pos = now_pos + 2
                now_pos += 1
            else:
                sp_list.append((now_pos, now_pos + 1, True))
                last_pos = now_pos + 1
            max_split -= 1
        now_pos += 1
    if last_pos < n:
        sp_list.append((last_pos, n, False))
    result_list = []
    for item in sp_list:
        if item[0] != item[1]:
            result_list.append((target_text[item[0]:item[1]], item[2]))
    return result_list

def cal_radius(w, h):
    return int(math.ceil(math.sqrt(w*w/4.0 + h*h/4.0)))

def get_text_img_with_circle(text, font_path, font_size, font_color, sp_draw):
    img_t = Image.new("RGBA", (1,1))
    draw_t = ImageDraw.Draw(img_t)
    font = sp_draw.get_font(font_path, font_size)
    w, h = draw_t.textsize(text, font=font)
    r = cal_radius(w, h)
    R = 2*r + 2
    img = Image.new("RGBA", (R, R), (0,0,0,0))
    draw = ImageDraw.Draw(img)
    draw.text(( (R - w)//2, (R - h)//2 ), text, font=font, fill=font_color)
    draw.ellipse((0,0, R, R), outline=font_color, width=2)
    return img

def draw_target_text(text, is_draw_circle, font_gen, font_size, font_color, sp_draw):
    font_name = font_gen.get_font_name_by_text(text)
    if font_name is None:
        return None
    font_path = font_gen.get_font_path_by_name(font_name)
    font = sp_draw.get_font(font_path, font_size)
    if is_draw_circle:
        return get_text_img_with_circle(text, font_path, font_size, font_color, sp_draw)
    else:
        return sp_draw.get_text_img(text, font_path, font_size, font_color)

def get_text_img_list(target_text, W, H, font_gen, font_size, font_color, sp_draw):
    text_list = split_number_and_letter(target_text)
    if len(text_list) == 1:
        return None
    text_img_list = []
    sum_w, sum_h = 0, 0
    for item in text_list:
        text_img = draw_target_text(item[0], item[1], font_gen, font_size, font_color, sp_draw)
        if text_img is None:
            return None
        t_w, t_h = text_img.size
        sum_w += t_w
        sum_h += t_h
        text_img_list.append(text_img)
    if sum_w >= W or sum_h >= H:
        return None
    return text_img_list

def strip_gang(target_text):
    pre_space = u''
    pos = 0
    n = len(target_text)
    while pos < n and target_text[pos] == u' ':
        pre_space += u' '
        pos += 1
    while pos < n and (target_text[pos] == u'-' or target_text[pos] == u'-'):
        pos += 1
    result = pre_space + target_text[pos:]
    if random.random() < 0.5:
        result = result.replace(u'`', u'~')
    else:
        result = result.replace(u'`', u'～')
    if len(result) == 0:
        return u' '
    return result
