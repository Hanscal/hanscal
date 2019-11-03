# coding:utf-8

from PIL import Image, ImageDraw, ImageFont
import yaml
import os, sys, random, math
from .sp_utils import wanke

class SpecialDraw(object):
    """docstring for SpecialDraw"""
    def __init__(self, config_path):
        super(SpecialDraw, self).__init__()
        self.config = self.load_config(config_path)
        self.font_caches = {}
    
    def load_config(self, config_path):
        result = None
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            result = yaml.load(content)

        return result

    def get_font(self, font_path, font_size):
        hash_str = "{}_{}".format(font_path, font_size)
        if hash_str in self.font_caches:
            return self.font_caches[hash_str]
        print ('new font:', font_path)
        font_path = font_path
        print(font_path, hash_str)
        self.font_caches[hash_str] = ImageFont.truetype(font_path, font_size)
        return self.font_caches[hash_str]

    def get_text_img(self, text, font_path, font_size, font_color):
        img_t = Image.new("RGBA", (1,1))
        draw_t = ImageDraw.Draw(img_t)
        font = self.get_font(font_path, font_size)
        try:
            w, h = draw_t.textsize(text, font=font)
        except Exception as e:
            print('text',text)
            print('font path, size, color',font_path,font_size,font_color)
            print('get text img error', e)
            os._exit(-1)
        # font = ImageFont.truetype(font_path, font_size)
        img = Image.new("RGBA", (w, h), (0,0,0,0))
        draw = ImageDraw.Draw(img)
        draw.text((0,0), text, font=font, fill=font_color)
        return img

    def get_text_affine_img(self, text, font_path, font_size, font_color):
        img_t = Image.new("RGBA", (1,1))
        draw_t = ImageDraw.Draw(img_t)
        font = self.get_font(font_path, font_size)
        w, h = draw_t.textsize(text, font=font)
        # font = ImageFont.truetype(font_path, font_size)
        img = Image.new("RGBA", (w, h), (0,0,0,0))
        draw = ImageDraw.Draw(img)
        draw.text((0,0), text, font=font, fill=font_color)
        img = img.transform((w+h,h),Image.AFFINE,(1.1,0.4,-h,0,1,0))
        return img

    def guess_size(self, text, font_size):
        n = len(text)
        return n*font_size, font_size

    def draw_line(self, img, start_pos, end_pos, fill=(0, 0, 0), width=2):
        draw = ImageDraw.Draw(img)
        draw.line(start_pos + end_pos, fill=fill, width=width)

    def draw_rect(self, img, start_pos, end_pos, fill=None, outline=(0,0,0), width=2):
        draw = ImageDraw.Draw(img)
        draw.rectangle(start_pos + end_pos, fill=fill, width=width, outline=outline)

    def paste_text_to_center(self, bg_img, text_img):
        W, H = bg_img.size
        w, h = text_img.size
        x1 = int((W - w)/2)
        y1 = int((H - h)/2)
        bg_img.paste(text_img, (x1, y1), mask=text_img)
        return [x1, y1, x1 + w, y1 + h]

    def draw_form_lines(self, bg_img, text_area):
        if random.random() > self.config['draw_form_line_ratio']:
            return
        W,H = bg_img.size
        line_color = self.random_line_color()
        y1 = text_area[1]
        y2 = text_area[3]
        if random.random() < 0.5:
            up_y = random.randint(max(0, y1 - 10), max(0, y1 - 3))
        else:
            up_y = random.randint(0, max(0, y1 - 10))
        self.draw_line(bg_img, (0, up_y), (W, up_y), fill=line_color)
        down_y = random.randint(min(y2 + 2, H), min(y2 + 2 + int((text_area[3] - text_area[1])*1.5),H) )
        self.draw_line(bg_img, (0, up_y), (W, up_y), fill=line_color)

        x1 = text_area[0]
        x2 = text_area[2]
        if random.random() < 0.5:
            left_x = random.randint(max(0, x1 - 10), max(0, x1 - 3))
        else:
            left_x = random.randint(0, max(0, x1 - 10))
        self.draw_line(bg_img, (left_x, 0), (left_x, H), fill=line_color)
        right_x = random.randint(min(x2 + 5, W), W)
        self.draw_line(bg_img, (right_x, 0), (right_x, H), fill=line_color)

    def find_max_angle(self, W, H, w, h):
        r_square = w*w/4.0 + h*h/4.0
        r = math.sqrt(r_square)
        if r < W / 2.0 and r < H / 2.0:
            return 90
        min_degree = 90
        if r >= H / 2.0:
            y = H / 2.0
            sin_theta = y / r
            sin_theta_origin = h/2.0/r
            theta = math.asin(sin_theta)
            theta_origin = math.asin(sin_theta_origin)
            degree = math.degrees(theta)
            degree_origin = math.degrees(theta_origin)
            min_degree = min(min_degree, degree - degree_origin)
        if r >= W / 2.0:
            x = W / 2.0
            cos_theta = x / r
            cos_theta_origin = w / 2.0 / r
            theta = math.acos(cos_theta)
            theta_origin = math.acos(cos_theta_origin)
            degree = math.degrees(theta)
            degree_origin = math.degrees(theta_origin)
            min_degree = min(min_degree, degree_origin - degree)
        return int(min_degree)

    def paste_random_rotate_text_img(self, bg_img, text_img):
        W, H = bg_img.size
        w, h = text_img.size
        max_angle = self.find_max_angle(W, H, w, h)
        max_angle = max(0, max_angle - 1)
        max_angle = min(max_angle, 2)
        angle = random.randint(-max_angle, max_angle)

        rotate_img = text_img.rotate(angle, expand=True)
        n_w, n_h = rotate_img.size
        if n_w > W or n_h > H:
            return None
        return self.paste_text_to_center(bg_img, rotate_img)

    def random_line_color(self):
        mean_value = random.randint(0, 128)
        c_list = []
        for i in range(3):
            v = random.randint(mean_value - 10, mean_value + 10)
            v = min(255, max(v, 0))
            c_list.append(v)
        return tuple(c_list)

    def draw_under_line(self, bg_img, text_area):
        if random.random() > self.config['draw_underline_ratio']:
            return
        W,H = bg_img.size
        line_color = self.random_line_color()
        line_length = random.randint(1, text_area[2] - text_area[0])
        x_pos = random.randint(0, text_area[2] - text_area[0] - line_length)
        y_pos = random.randint(text_area[3], text_area[3] + 4)
        self.draw_line(bg_img, (text_area[0] + x_pos, y_pos), (text_area[0] + x_pos + line_length, y_pos), fill=line_color)

    def draw_block(self, bg_img, text_area, text):
        if random.random() > self.config['draw_block_ratio']:
            return text
        W, H = bg_img.size
        block_color = self.random_line_color()
        block_size = int((text_area[3] - text_area[1])*0.9)
        s_x = text_area[0] - block_size - 3
        s_y = text_area[1] + int((text_area[3] - text_area[1] - block_size)/2)
        if s_x - 1 <= 0:
            return text
        if random.random() < 0.5:
            self.draw_rect(bg_img, (s_x, s_y), (s_x + block_size, s_y + block_size), outline=block_color, fill=None, width=1)
        else:
            self.draw_rect(bg_img, (s_x, s_y), (s_x + block_size, s_y + block_size), outline=block_color, fill=block_color, width=1)
        text_area[0] = s_x - 1
        return " " + text


    def expand_text_area(self, bg_img, text_area, text):
        W, H = bg_img.size
        x1, y1, x2, y2 = text_area[0],text_area[1],text_area[2],text_area[3]
        t_w, t_h = (x2 - x1), (y2 - y1)
        if random.random() < 0.3:
            return [x1, y1, x2, y2], text
        if random.random() > self.config['more_expend_ratio']:
            # simple expand
            x_exp = random.randint(int(t_h/4), int(t_h) )
            x1 = max(0, x1 - x_exp)
            x2 = min(W, x2 + x_exp)
            y_exp = random.randint(2, 8)
            y1 = max(0, y1 - y_exp)
            y2 = min(H, y2 + y_exp)
            return [x1, y1, x2, y2], text
        else:
            x1_exp = random.randint(int(1.2*t_h), int(2*t_h))
            x2_exp = random.randint(int(1.2*t_h), int(2*t_h))
            x1 = max(0, x1 - x1_exp)
            x2 = min(W, x2 + x2_exp)
            y1_exp = random.randint(int(0.1*t_h), int(0.5*t_h))
            y2_exp = random.randint(int(0.1*t_h), int(0.5*t_h))
            y1 = max(0, y1 - y1_exp)
            y2 = min(H, y2 + y2_exp)
            if x1_exp >= t_h and text[0] != ' ':
                text = ' ' + text
            if x2_exp >= t_h and text[-1] != ' ':
                text = text + ' '
            return [x1, y1, x2, y2], text

    def remove_extra_spcae(self, text):
        result = u''
        for i, c in enumerate(text):
            if i > 0 and (c == u' ' and text[i - 1] == u' '):
                continue
            result += c
        return result

    def random_split_text(self, text, font_gen, font_size):
        default_font_name = font_gen.get_font_name_by_text(text)
        if default_font_name is None:
            return None
        default_font_path = font_gen.get_font_path_by_name(default_font_name)
        if random.random() > self.config['rand_small_font'] or len(text) < 8:
            return [(text , font_size, default_font_path)]
        small_size = random.randint(font_size - 7, font_size - 2)
        small_size = max(15, small_size)
        n = len(text)
        small_word_len = random.randint(int(n/4), int(n/2) )
        p = random.randint(0, n - small_word_len)
        # 0 -> p
        result = []
        if p > 0:
            font_name = font_gen.get_font_name_by_text(text[:p])
            result.append((text[:p], font_size, font_gen.get_font_path_by_name(font_name)))
        # p -> p + small_word_len
        font_name = font_gen.get_font_name_by_text(text[p:p+small_word_len])
        result.append((text[p:p+small_word_len], small_size, font_gen.get_font_path_by_name(font_name)))
        # p + small_word_len -> end
        if p + small_word_len < n:
            font_name = font_gen.get_font_name_by_text(text[p+small_word_len:])
            result.append((text[p+small_word_len:], font_size, font_gen.get_font_path_by_name(font_name)))
        return result

    def paste_text_list_to_center(self, bg_img, text_img_list):
        W, H = bg_img.size
        total_w = 0
        for text_img in text_img_list:
            t_w, t_h = text_img.size
            total_w += t_w
        start_p = int((W - total_w)/2)
        area = [start_p, H, start_p + total_w, 0]
        for text_img in text_img_list:
            t_w, t_h = text_img.size
            y_s = int((H - t_h)/2)
            bg_img.paste(text_img, (start_p, y_s), mask=text_img)
            area[1] = min(area[1], y_s)
            area[3] = max(area[3], y_s + t_h)
            start_p += t_w
        return area
        # x1 = int((W - w)/2)
        # y1 = int((H - h)/2)
        # bg_img.paste(text_img, (x1, y1), mask=text_img)
        # return [x1, y1, x1 + w, y1 + h]



    def process(self, text_list, bg_img, font_gen):
        # font_name = font_gen.get_all_ch_font_name()
        # font_path = font_gen.get_all_ch_font_path(font_name)
        target_text = text_list[0]
        font_size = font_gen.get_font_size(is_sp=(len(target_text) > self.config['max_content_length']) )
        font_name_list = font_gen.font_name_list

        color_ratio = random.random()
        if color_ratio>0.01:
            font_color = font_gen.get_font_color()
        else:
            font_color = font_gen.get_random_font_color()
        W,H = bg_img.size
        # 大概的image的宽度和长度
        g_w, g_h = self.guess_size(target_text, font_size)
        if g_w > W or g_h > H:
            return None, None


        # target_text = wanke.strip_gang(target_text)
        # if random.random() < self.config['draw_circle_ratio']:
        #     text_img_list = wanke.get_text_img_list(target_text, W, H, font_gen, font_size, font_color, self)

        if random.random() > 0.5:
            texts_with_font_size = self.random_split_text(target_text, font_gen, font_size)
            if texts_with_font_size is None:
                return None, None
            text_img_list = []
            # print '------------------------------------------------------------'
            for item in texts_with_font_size:
                # print item[1]
                text_img_list.append(self.get_text_img(item[0], item[2], item[1], font_color))
            text_area = self.paste_random_rotate_text_img(bg_img, text_img_list[0])
        else:
            default_font_name = font_gen.get_font_name_by_text(target_text)
            if default_font_name is None:
                return None, None
            font_path = font_gen.get_font_path_by_name(default_font_name)
            text_img = self.get_text_img(target_text, font_path, font_size, font_color)
            # t_w, t_h = text_img.size
            text_area = self.paste_text_to_center(bg_img, text_img)

        if text_area is None:
            return None, None
        # text_area = self.paste_text_list_to_center(bg_img, text_img_list)

        self.draw_form_lines(bg_img, text_area)
        self.draw_under_line(bg_img, text_area)
        target_text = self.draw_block(bg_img, text_area, target_text)
        new_area, new_text = self.expand_text_area(bg_img, text_area, target_text)
        croped_img = bg_img.crop(tuple(new_area))
        new_text = self.remove_extra_spcae(new_text)
        return croped_img, new_text

