# -*- coding:utf-8 -*-

'''
author: "caihua"
date: 2019/10/10
Email: hanscalcai@163.com
'''

import os, sys, random, math
from  decimal import Decimal
from .specific_utils import *
import json
import optparse
from tqdm import tqdm

fixe_word_lists = []

def format_1():
    numbers = '1234567890'
    engs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    sp = '<'
    words = [numbers, engs, sp]
    ratio = [0.3, 0.4, 0.3]
    result_str = ''
    text_n = random.randint(30, 44)
    for i in range(text_n):
        rand_value = random.random()
        select_p = 0
        pre_sum = 0
        for j in range(3):
            if rand_value < pre_sum + ratio[j]:
                select_p = j
                break
            pre_sum += ratio[j]
        result_str += words[select_p][random.randint(0, len(words[select_p]) - 1)]
    return result_str

def format_2():
    pre_fix_words = ['甲方', '用人单位', '聘用企业', '雇主']
    if random.random() < 0.5:
        return get_random_company()
    return '{}{}{}{}'.format(pre_fix_words[random.randint(0, len(pre_fix_words) - 1)], \
                            get_random_colon(), get_random_space(2), get_random_company())

def format_3():
    pre_fix_words = ['乙方', '雇员', '受聘人', '劳动者']
    if random.random() < 0.5:
        return get_random_person_name()
    return '{}{}{}{}'.format(pre_fix_words[random.randint(0, len(pre_fix_words) - 1)], \
                            get_random_colon(), get_random_space(2), get_random_person_name())

def format_4():
    pre_fix_words = ['地址']
    if random.random() < 0.5:
        return get_random_street()
    return '{}{}{}{}'.format(pre_fix_words[random.randint(0, len(pre_fix_words) - 1)], \
                            get_random_colon(), get_random_space(2), get_random_street())

def format_5():
    numbers = '1234567890'
    engs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res_txt = ''
    for i in range(8):
        if random.random() < 0.4:
            res_txt += engs[random.randint(0, len(engs) - 1)]
        else:
            res_txt += numbers[random.randint(0, len(numbers) - 1)]
    return '护照号码为{}{}{}'.format(get_random_colon(), get_random_space(2), res_txt)

def format_6():
    format_list = ['自[{}]年[{}]月[{}]日起', '至[{}]年[{}]月[{}]日止', '自{}年{}月{}日起', '至{}年{}月{}日止']
    format_str = format_list[random.randint(0, len(format_list) - 1)]
    return format_str.format(get_year(), get_month(), get_day()) + '卐'

def format_7():
    pre_fix_words = ['国籍']
    if random.random() < 0.5:
        return get_random_country()
    return '{}{}{}{}'.format(pre_fix_words[random.randint(0, len(pre_fix_words) - 1)], \
                            get_random_colon(), get_random_space(2), get_random_country())

def format_8():
    # if random.random() < 0.5:
    #     return get_cn_amount()
    number_str = get_amount_number()
    number_str = number_str[::-1]
    result = ''
    dot_pos = number_str.find('.')
    if dot_pos >= 0:
        result += number_str[:dot_pos]
        number_str = number_str[dot_pos+1:]
    n = len(number_str)
    for i in range(n):
        if i > 0 and i % 3 == 0:
            result += ','
        result += number_str[i]
    return result[::-1]


xinchou_formats = None

def format_9():
    n = len(xinchou_formats)
    f_id = random.randint(0 , n - 1)
    xinchou_f = xinchou_formats[f_id]
    result_str = ''
    for item in xinchou_f:
        if item['type'] == 'fix_text':
            result_str += ''
        elif item['type'] == 'amount':
            result_str += format_8()
        elif item['type'] == 'cn_amount':
            result_str += get_cn_amount()
        elif item['type'] == 'percent':
            result_str += str(random.randint(0, 100))
    result_str += '卐'
    return result_str

def format():
    str_datas = [
        "受聘方的税前月薪为人民币 * 元。",
        "主本合同期内,乙方在甲方的劳动报酬为每月税前人民币 * 元。根据",
        "受聘方的税前月薪为人民币 * 元,其中 |%可按月兑换外汇。",
        "甲方每月月底向乙方支付当月工资人民币 *,并提供居住、伙食、交通等费用。",
        "乙方的月基本工资为人民币 * 元整,甲方每月以汇款的方式将工资汇入乙方的指定账",
        "工资待遇:乙方月薪为 * 人民币。",
        "按甲方现行工资制度确定乙方基本工资 * 元。岗位奖金为 * 元",
        "转正后月工资为税前人民币 】 元,其中基本工资为人民币 ,】 元/月",
        "乙方的月工资为税前: * 元,每月工资由甲方在甲方规定的日期支付",
        "乙方每月基本工资为税前人民币 * 元",
        "乙方目前税前年收入为人民币 * 元",
        "乙方的报酬为税前 *",
        "工资福利:聘用期间每年基本报酬为人民币 * 万元(含社会保险、福利等),按月平",
        "乙方月工资为人民币*元(税前)",
        "甲方将于每月月底支付乙方薪资。税前*(人民币)。",
        "甲方确定乙方每月的税前工资为:税后 * 元(人民币)",
        "劳动报酬:月薪: * 圆整。",
        "按甲方现行工资制度确定乙方基本工资 * 元。岗位奖金为 / 元",
        "乙方每月工资为人民币 * 元(税前)",
        "雇员每个月的工资总额为人民币*元(】)。",
        "甲方支付给乙方的每月薪酬为(税前)人民币 * 元(大写:人民币)",
        "受聘方的税前月薪为人民币 * 元。",
        "乙方的月基木工资为人民币 * 元整,甲方每月以汇款的方式将工资汇入乙方的指定账",
        "乙方入职时的月工资为人民币*元,按照甲方正常工资支付周期支付给乙方。",
        "基本工资为 * 元",
        "每个月的收入(税前)将为人民币 * 元。",
        "受聘方的税前月薪为人民币 * 元,其中|%可按月兑换外汇。",
        "您的税前月基本工资为人民币 * 元",
        "薪酬福利。乙方的标准固定工资为税前人民币*元/月,每年按12个月发放",
        "甲方按公司制度支付乙方薪水,基本月薪*元人民币",
    ]

    result = []

    for s in str_datas:
        item = []
        pre_str = ""

        def add_pre_str():
            global pre_str
            if len(pre_str) > 0:
                item.append({'content': pre_str, 'type': 'fix_text'})
            pre_str = ""

        for c in s:
            if c == '*':
                add_pre_str()
                item.append({'content': '', 'type': 'amount'})
            elif c == '】':
                add_pre_str()
                item.append({'content': '', 'type': 'cn_amount'})
            elif c == '|':
                add_pre_str()
                item.append({'content': '', 'type': 'percent'})
            else:
                pre_str += c
        add_pre_str()
        result.append(item)

    with open('xinchou.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(result, ensure_ascii=False, indent=4))

format_func_list = [format_2, format_3, format_4,format_4, format_5,format_5, format_6,format_6, format_7, format_9]

def run(options):
    n = len(fixe_word_lists)
    m = len(format_func_list)

    format()
    xinchou_json_path = os.path.join(options.base_data_dir, 'xinchou.json')
    with open(xinchou_json_path, 'r', encoding='utf-8') as f:
        global xinchou_formats
        xinchou_formats = json.loads(f.read())

    set_base_data_dir(options.base_data_dir)

    with open(options.output_path, 'w', encoding='utf-8') as f:
        for i in tqdm(range(options.gen_number)):
            res_str = ''
            if random.random() < 0:
                res_str = fixe_word_lists[random.randint(0, n - 1)]
            else:
                res_str = format_func_list[random.randint(0, m - 1)]()
            f.write(res_str + '\n')

def get_options(args=None):
    opt_parser = optparse.OptionParser()
    opt_parser.add_option('-b', '--base_data_dir', type=str, default='', help='')
    opt_parser.add_option('-o', '--output_path', type=str, default='', help='')
    opt_parser.add_option('-n', '--gen_number', type=int, default=100000, help='')

    (options, args) = opt_parser.parse_args(args=args)
    return options

if __name__ == '__main__':
    options = get_options()
    if not options:
        sys.exit(1)
    run(options)