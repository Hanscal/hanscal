# coding:utf-8

import os, sys, random, math
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
import optparse
from tqdm import tqdm
from datas.charsets.charset_random import eng_nums, symbols, riyu, cn_words


str_list = [eng_nums, symbols, cn_words]

def random_text():
    lens = [len(eng_nums), len(symbols), len(cn_words)]
    ratios = [0.1, 0.01, 0.89]
    if random.random() < 0.5:
        n = random.randint(1, 10)
    else:
        n = random.randint(10, 20)
    result = ''
    for i in range(n):
        r_value = random.random()
        sum_value = 0
        tar_id = 0
        for i,r in enumerate(ratios):
            if r_value < r + sum_value:
                tar_id = i
                break
            sum_value += r
        target_s = str_list[tar_id]
        result += target_s[random.randint(0, lens[tar_id] - 1)]
    return result


def run(options):
    with open(options.output_path, 'w', encoding='utf-8') as f:
        for i in tqdm(range(options.gen_number)):
            text = random_text()
            f.write(text + '\n')

def get_options(args=None):
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('-n', '--gen_number', type=int, default=100000, help='')
    opt_parser.add_option('-o', '--output_path', type=str, default='/data/caihua/scripts/ocr-recognition-datamaker/datas/corpus_output/rand_chinese.txt', help='')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)