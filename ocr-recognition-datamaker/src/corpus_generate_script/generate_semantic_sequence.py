# coding:utf-8

import os, sys, random, math
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from datas.charsets.charset_random import cn_words
import optparse
import random
from tqdm import tqdm
import multiprocessing

# 会加载cn_words之外的字符
alphabet = cn_words

def get_all_file_list(root_dir):
    result = []
    for dirpath, _, filenames in os.walk(root_dir):
        for filepath in filenames:
            if filepath[-4:] == '.txt':
                result.append(os.path.join(dirpath, filepath))
    return result

def load_line_data(file_path):
    result = []
    with open(file_path, 'r') as f:
        for i,line in enumerate(f.readlines()):
            try:
                line = line.strip()
                if i %100000 ==0:
                    print('lines {}'.format(i))
            except Exception:
                try:
                    line = line.decode('utf-8').strip()
                except Exception as e:
                    # print(line)
                    print(e)
                    continue
            if '\0' in line:
                continue
            res_str = ""
            for c in line:
                if c in alphabet:
                    res_str += c
            for i, c in enumerate(line):
                if c != '' or (i > 0 and c == ' ' and line[i - 1] != ' '):  # 一行文本加载两次，第二次是为了把不在字符集中的字符加载
                    res_str += c
            if len(res_str) > 0:
                result.append(line)
    return result

# 改写成multiprocessing
def split_line_data(line_data):
    result = []
    for line_text in line_data:
        while len(line_text) >= 100:
            p = random.randint(10, 100)
            # if random.random() < 0.5:
            #     while line_text[p-1] !=' ' and p > 0:
            #         p -= 1
            result.append(line_text[:p])
            line_text = line_text[p:]

        if len(line_text) > 0:
            result.append(line_text)

    return result


def run(options):
    file_list = get_all_file_list(options.input_corpus)

    max_lines = 10000000
    text_lengths = []
    text_list = []
    pool = multiprocessing.Pool(processes=4)
    for file_path in tqdm(list(file_list)):
        print(os.path.basename(file_path))
        line_data = load_line_data(file_path)

        sp_line_data = pool.apply_async(split_line_data, (line_data,))

        # sp_line_data = split_line_data(line_data)
        text_pool = sp_line_data.get()
        text_lengths.append(len(text_pool))
        text_label = []
        for j,text in enumerate(text_pool):
            if j > max_lines:
                break
            else:
                text_label.append(text)
        text_list.append(text_label)
    pool.close()
    pool.join()
    print('text lengths',text_lengths)
    ratio = min(max_lines,options.gen_number) / sum([len(i) for i in text_list])

    with open(options.output_path, 'w') as f:
        for select_text in text_list:
            sub_text_list = random.sample(select_text, int(ratio*len(select_text)))
            # write_str = "\n".join(sub_text)
            sub_text_length = len(sub_text_list)
            up_text_indices = random.sample(range(0,sub_text_length),int(0.01*sub_text_length))
            for i,sub_text in enumerate(sub_text_list):
                write_str = sub_text +'\n'
                if i in up_text_indices:
                    write_str = write_str.upper()
                f.write(write_str)

        # if i > 10:
        #     break

def get_options(args=None):
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('-i', '--input_corpus',type=str, default='', help='')
    opt_parser.add_option('-n', '--gen_number', type=int, default=1000000, help='')
    opt_parser.add_option('-o', '--output_path', type=str, default='', help='')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)