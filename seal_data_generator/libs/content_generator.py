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
        self.max_content_length = self.config['max_content_length']

    def load_config(self, config_path):
        result = None
        with open(config_path, 'r') as f:
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
            self.corpus_datas[name] = self.load_file(item['corpus_path'])
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

    def cut_text(self, text):
        n = len(text)
        if n > self.max_content_length:
            m = self.max_content_length
            p = random.randint(0, n - m)
            return text[p: p+m]
        return text

    def process(self):
        r_value = random.random()
        target_id = None
        pre_sum = 0.0
        for item in self.config['contents']:
            if r_value <= pre_sum + item['w']:
                target_id = item['id']
                break
            pre_sum += item['w']

        result_text = ''
        n = len(self.corpus_datas[target_id])
        while True:
            content = self.corpus_datas[target_id][random.randint(0, n - 1)]
            content = self.cut_text(content)
            if len(content) > 0:
                result_text = content
                break
        return result_text


if __name__ == '__main__':
    content_gen = ContentGenerator('../configs/seal_config.yaml')
    for i in range(20):
        print(content_gen.process())