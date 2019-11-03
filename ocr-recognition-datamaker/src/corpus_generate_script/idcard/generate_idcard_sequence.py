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
import time

fixe_word_lists = []

def format_passport_visa():
    numbers = '1234567890'
    engs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res_txt = ''
    for i in range(8):
        if random.random() < 0.4:
            res_txt += engs[random.randint(0, len(engs) - 1)]
        else:
            res_txt += numbers[random.randint(0, len(numbers) - 1)]
    return '护照号码为{}{}{}'.format(get_random_colon(), get_random_space(2), res_txt)

def format_passport_visa1():
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

def format_name(filepath=os.path.join(os.path.dirname(__file__),'Chinese_Names_Corpus.txt')):
    return '{}{}'.format(get_random_space(2), get_random_person_name(filepath))

def format_idlocation():
    """words in list format"""
    c_length = random.randint(8,15)
    return '{}{}'.format(get_random_space(2), get_random_cn(max_n=c_length))

def gen_expire_date(key):
    format_str = '{}.{}.{}-{}.{}.{}'
    return format_str.format(get_year(), get_month(), get_day(),get_year(),get_month(),get_day())

def gen_idno():
    now_year = time.strftime('%Y')
    year = random.randint(1948, int(now_year)-18)
    month = random.randint(1,12)
    if month<10:
        month = '0'+month
    day = random.randint(0,31)
    if day < 10:
        day = '0'+day

    def getArr():
        from .addr import addr
        addrIndex = random.randint(0,len(addr)-1)
        return addr[addrIndex]

    def getCheckBit(num17):
        Wi = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
        checkCode = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
        zipWiNum17 = zip(list(num17), Wi)
        S = sum(int(i) * j for i, j in zipWiNum17)
        Y = S % 11
        return checkCode[Y]

    regno, addrname = getArr()
    idno = str(regno)+str(year)+str(month)+str(day)
    for i in range(2):
        idno += str(random.randint(0,9))
    sex = random.randint(1,2)
    idno += str(random.randrange(sex,9,2))
    idno += getCheckBit(idno)
    if sex == 1:
        sex_str = '男'
    else:
        sex_str = '女'
    return idno, addrname, sex_str


def format(format_key_list):
    format_datas = [
        format_key_list[0]+"?",
        format_key_list[1]+"!",
        format_key_list[2]+"*",
        format_key_list[3]+"】",
        format_key_list[4]+"#",
        format_key_list[5]+"|",
        format_key_list[6]+"@公安局",
        format_key_list[7]+"【",
    ]

    idno, addrname, sex_str = gen_idno()

    n = len(format_datas)
    f_id = random.randint(0, n - 1)
    specific_f = format_datas[f_id]
    result_str = ''

    for item in specific_f:
        if '?' in item:
            pos = item.find('?')
            result_str += item[:pos]+'\n'
            result_str += item[pos:]+'\n'
            result_str += '{}{}{}'.format(format_key_list[0],get_random_space(2), format_name())
        elif '!' in item:
            pos = item.find('!')
            result_str += item[:pos] + '\n'
            result_str += item[pos:] + '\n'
            result_str += format_key_list[1]+get_random_space(2)+sex_str
        elif '*' in item:
            pos = item.find('*')
            result_str += item[:pos] + '\n'
            result_str += item[pos:] + '\n'
            result_str += format_key_list[2]+get_random_space(2)+get_nation()
        elif '】' in item:
            pos = item.find('】')
            result_str += item[:pos] + '\n'
            result_str += item[pos:] + '\n'
            result_str += '{}{}年{}月{}日'.format(format_key_list[3],get_random_space(2),str(idno[6:10]),str(idno[10:12]),str(idno[12:14]))
        elif '#' in item:
            pos = item.find('#')
            result_str += item[:pos] + '\n'
            result_str += item[pos:] + '\n'
            result_str += format_key_list[4]+get_random_space(2)+format_idlocation
        elif '|' in item:
            pos = item.find('|')
            result_str += item[:pos] + '\n'
            result_str += item[pos:] + '\n'
            result_str += format_key_list[5]+get_random_space(2)+idno
        elif '@' in item:
            pos = item.find('@')
            result_str += item[:pos] + '\n'
            result_str += item[pos:] + '\n'
            result_str += format_key_list[6]+get_random_space(2)+addrname+'公安局'
        elif '【' in item:
            pos = item.find('【')
            result_str += item[:pos] + '\n'
            result_str += item[pos:] + '\n'
            result_str += format_key_list[7]+get_random_space(2)+gen_expire_date()


    result_str +='\n'

    return result_str

format_func_list =[format]

def run(options):
    pre_fixdata_list = ["有效期限", "签发机关", "中华人民共和国", "居民身份证", "姓 名",
                        "性 别", "民 族", "出 生", "住 址", "公民身份证号码"]
    format_key_list= ["姓 名", "性 别", "民 族", "出 生", "住 址", "公民身份证号码", "签发机关", "有效期限"]

    n = len(fixe_word_lists)

    with open(options.output_path, 'w', encoding='utf-8') as f:
        for i in tqdm(range(options.gen_number)):
            if random.random() < 0:
                res_str = pre_fixdata_list[random.randint(0, n - 1)]
            else:
                res_str = format(format_key_list=format_key_list)
            if len(res_str.strip()) > 0:
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