# coding:utf-8

import os, sys, random, math
import yaml

class ContentGenerator(object):
    """docstring for ContentGenerator"""
    def __init__(self, config_path):
        super(ContentGenerator, self).__init__()
        self.config = self.load_config(config_path)
        self.corpus_datas = {}
        self.load_corpus_data()
        self.normalize_appear_weight()
        # print self.config

    def load_config(self, config_path):
        result = None
        print('config_path',config_path)
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            result = yaml.load(content)

        return result

    def load_file(self, file_path):
        result = []
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                result.append(line)
        return result

    def load_corpus_data(self):
        for item in self.config['contents']:
            name = item['id']
            corpus_path = item['corpus_path']
            if not item['is_absolute_path']:
                corpus_path = os.path.join(self.config['corpus_base_dir'], corpus_path)
            self.corpus_datas[name] = self.load_file(corpus_path)
        print ("load corpus data over.....")

    def normalize_appear_weight(self):
        '''
            每一项的生成概率权重归一化
        '''
        total = 0.0
        for item in self.config['contents']:
            if item['w'] >= 0:
                total += item['w']
            else:
                item['w'] = 0.0
        
        for item in self.config['contents']:
            item['w'] = item['w']/total

    def is_sp_text(self, text):
        chars = u'1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ<'
        for c in text:
            if c not in chars:
                return False
        return True

    def random_cut_text(self, text):
        if random.random() < self.config['cut_str_ratio']:
            min_l,max_l = self.config['cut_min_len'], self.config['cut_max_len']
            if len(text) <= max_l:
                return text
            n = len(text)
            m = random.randint(min_l, max_l)
            p = random.randint(0 , n - m)
            return text[p:p+m]
        return text

    def cut_text(self, text):
        n = len(text)
        if n > self.config['max_content_length']:
            if self.is_sp_text(text):
                return text
            m = self.config['max_content_length']
            p = random.randint(0, n - m)
            return text[p: p+m]
        return text

    def random_space(self, text):
        if u' ' in text:
            return text
        n = len(text)
        if random.random() < self.config['random_space'] and (n > 1 and n < 25):
            m = random.randint(0, n)
            return text[:m] + u" "*random.randint(2, self.config['max_space_len']) + text[m:]

        return text

    def process(self):
        r_value = random.random()
        target_id = None
        target_max_line = 1
        pre_sum = 0.0
        for item in self.config['contents']:
            if r_value <= pre_sum + item['w']:
                target_id = item['id']
                target_max_line = max(target_max_line, item['max_line'])
                break
            pre_sum += item['w']

        result_list = []
        generate_line = random.randint(1, target_max_line)
        n = len(self.corpus_datas[target_id])
        for i in range(generate_line):
            while True:
                content = self.corpus_datas[target_id][random.randint(0, n - 1)]
                # content = self.random_cut_text(content)
                content = self.cut_text(content)
                content = self.random_space(content)
                if len(content) > 0:
                    result_list.append(content)
                    break
        return result_list


