# coding:utf-8

import os, sys, random, math
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
from  decimal import Decimal
from datas.charsets.charset_random import cn_words, cn_words_first, cn_words_second

alphabet = cn_words
base_data_dir = ''

def set_base_data_dir(target_dir):
    global base_data_dir
    base_data_dir = target_dir

def load_bank_line_data(file_path):
    result = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            is_pass = True
            for c in line:
                if not c in alphabet:
                    is_pass = False
                    break
            if not is_pass:
                continue
            line_list = line.split(' ')
            while len(line_list) < 4:
                line_list.insert(0, "")
            result.append(line_list)
    return result

def get_number_string(str_len):
    ret_str = ''
    for i in range(str_len):
        ret_str += str(random.randint(0, 9))
    return ret_str


def gen_random_code():
    result = '借字'
    result += get_number_string(random.randint(3, 6))
    result += '第'
    result += get_number_string(random.randint(3, 8))
    result += '号'
    if random.random() < 0.4:
        result += u'-'
    return result

# bank_line_data = load_bank_line_data('../temp/bank.txt')


def get_random_bank_code(bank_line_data):
    bank_appear_ratio = [0.4, 0.4, 0.4, 1]
    res_str = u''
    n = len(bank_line_data)
    for j, r in enumerate(bank_appear_ratio):
        if random.random() <= r:
            bank_id = random.randint(0, n - 1)
            try:
                res_str += bank_line_data[bank_id][j]
            except Exception as e:
                print (bank_id, j)
                print (bank_line_data[bank_id])
                raise
    if random.random() < 0.7:
        res_str += gen_random_code()
    return res_str

def get_random_bank(bank_line_data):
    bank_appear_ratio = [0.4, 0.4, 0.4, 1]
    res_str = u''
    n = len(bank_line_data)
    for j, r in enumerate(bank_appear_ratio):
        if random.random() <= r:
            bank_id = random.randint(0, n - 1)
            try:
                res_str += bank_line_data[bank_id][j]
            except Exception as e:
                print (bank_id, j)
                print (bank_line_data[bank_id])
                raise
    return res_str


def load_company_line_data(file_path):
    result = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            is_pass = True
            for c in line:
                if not c in alphabet:
                    is_pass = False
                    break
            if not is_pass:
                continue
            result.append(line)
    return result

def get_random_company(filepath):
    company_line_data = []
    n = len(company_line_data)
    if n == 0:
        company_line_data = load_company_line_data(filepath)
        n = len(company_line_data)
        print('load company over !')
    company_id = random.randint(0, n - 1)
    return company_line_data[company_id]

def get_random_person_name(filepath):
    chinese_name_line_data = []
    n = len(chinese_name_line_data)
    if n == 0:
        chinese_name_line_data = load_company_line_data(filepath)
        n = len(chinese_name_line_data)
        print('load chinexe name over !')
    name_id = random.randint(0, n - 1)
    return chinese_name_line_data[name_id]

def get_random_street(filepath):
    street_line_data = []
    n = len(street_line_data)
    if n == 0:
        street_line_data = load_company_line_data(filepath)
        n = len(street_line_data)
        print('load street over !')
    street_id = random.randint(0, n - 1)
    return street_line_data[street_id]


countrys = ['中国','蒙古','朝鲜','韩国','日本','菲律宾','越南','老挝','柬埔寨','缅甸','泰国','马来西亚','文莱','新加坡','印度尼西亚','东帝汶','尼泊尔','不丹','孟加拉国','印度','巴基斯坦','斯里兰卡','马尔代夫','哈萨克斯坦','吉尔吉斯斯坦','塔吉克斯坦','乌兹别克斯坦','土库曼斯坦','阿富汗','伊拉克','伊朗','叙利亚','约旦','黎巴嫩','以色列','巴勒斯坦','沙特阿拉伯','巴林','卡塔尔','科威特','阿拉伯联合酋长国','阿曼','也门','格鲁吉亚','亚美尼亚','阿塞拜疆','土耳其','塞浦路斯','芬兰','瑞典','挪威','冰岛','丹麦','爱沙尼亚','拉脱维亚','立陶宛','白俄罗斯','俄罗斯','乌克兰','摩尔多瓦','波兰','捷克','斯洛伐克','匈牙利','德国','奥地利','瑞士','列支敦士登','英国','爱尔兰','荷兰','比利时','卢森堡','法国','摩纳哥','罗马尼亚','保加利亚','塞尔维亚','马其顿','阿尔巴尼亚','希腊','斯洛文尼亚','克罗地亚','波斯尼亚和墨塞哥维那','意大利','梵蒂冈','圣马力诺','马耳他','西班牙','葡萄牙','安道尔','埃及','利比亚','苏丹','突尼斯','阿尔及利亚','摩洛哥','亚速尔群岛','马德拉群岛','埃塞俄比亚','厄立特里亚','索马里','吉布提','肯尼亚','坦桑尼亚','乌干达','卢旺达','布隆迪','塞舌尔','乍得','中非','喀麦隆','赤道几内亚','加蓬','刚果共和国','圣多美及普林西比','刚果民主共和国','毛里塔尼亚','西撒哈拉','塞内加尔','冈比亚','马里','布基纳法索','几内亚','几内亚比绍','佛得角','塞拉利昂','利比里亚','科特迪瓦','加纳','多哥','贝宁','尼日尔','加那利群岛','赞比亚','安哥拉','津巴布韦','马拉维','莫桑比克','博茨瓦纳','纳米比亚','南非','斯威士兰','莱索托','马达加斯加','科摩罗','毛里求斯','留尼旺','圣赫勒拿','澳大利亚','新西兰','巴布亚新几内亚','所罗门群岛','瓦努阿图','密克罗尼西亚','马绍尔群岛','帕劳','瑙鲁','基里巴斯','图瓦卢','萨摩亚','斐济群岛','汤加','库克群岛','关岛','新喀里多尼亚','法属波利尼西亚','皮特凯恩岛','瓦利斯与富图纳','纽埃','托克劳','美属萨摩亚','北马里亚纳','加拿大','美国','墨西哥','格陵兰','危地马拉','伯利兹','萨尔瓦多','洪都拉斯','尼加拉瓜','哥斯达黎加','巴拿马','巴哈马','古巴','牙买加','海地','多米尼加共和国','安提瓜和巴布达','圣基茨和尼维斯','多米尼克','圣卢西亚','圣文森特和格林纳丁斯','格林纳达','巴巴多斯','特立尼达和多巴哥','波多黎各','英属维尔京群岛','美属维尔京群岛','安圭拉','蒙特塞拉特','瓜德罗普','马提尼克','荷属安的列斯','阿鲁巴','特克斯和凯科斯群岛','开曼群岛','百慕大','哥伦比亚','委内瑞拉','圭亚那','法属圭亚那','苏里南','厄瓜多尔','秘鲁','玻利维亚','巴西','智利','阿根廷','乌拉圭','巴拉圭']
def get_random_country():
    country_id = random.randint(0, len(countrys) - 1)
    return countrys[country_id]

currencys = ['人民币','美元','日元','欧元','英镑','德国马克','瑞士法郎','法国法郎','加拿大元','澳大利亚元','港币','奥地利先令','芬兰马克','比利时法郎','爱尔兰镑','意大利里拉','卢森堡法郎','荷兰盾','葡萄牙埃斯库多','西班牙比塞塔','印尼盾','马来西亚林吉特','新西兰元','菲律宾比索','俄罗斯卢布','新加坡元','韩国元','泰铢']
def get_currency():
    n = len(currencys)
    c_id = random.randint(0, n - 1)
    return currencys[c_id]

nations = ['汉','壮','回','藏','裕固','彝','瑶','锡伯','乌孜别克','维吾尔','佤','土家','土','塔塔尔','塔吉克','水','畲','撒拉','羌',
 '普米','怒','纳西','仫佬','苗','蒙古','门巴','毛南','满','珞巴','僳僳','黎','拉祜','柯尔克孜','景颇','京','基诺','保安','布朗',
 '赫哲','哈萨克','哈尼','仡佬','高山','鄂温克','俄罗斯','鄂伦春','独龙','东乡','侗','德昂','傣','达斡尔','朝鲜','布依','白','阿昌']
def get_nation():
    n = len(nations)
    c_id = random.randint(0, n - 1)
    if random.random < 0.90:
        return '汉'
    elif random.random < 0.92:
        return '回'
    elif random.random < 0.94:
        return '壮'
    else:
        return nations[c_id]

def get_amount_number(max_prefix=8, max_suffix=2):
    rand_ranges = []
    ratios = [1, 1, 2, 3, 2, 1, 1, 1]
    base = 1
    for i in range(max_prefix):
        rand_ranges.append((base, base*10))
        base *= 10

    r_sum = 0.0
    for r in ratios[:max_prefix]:
        r_sum += r
    for i, r in enumerate(ratios[:max_prefix]):
        ratios[i] = r/r_sum

    r_value = random.random()
    pre_sum = 0.0
    pre_value = 0
    # print r_value, ratios
    for i, r in enumerate(ratios[:max_prefix]):
        if r_value <= r + pre_sum:
            pre_value = random.randint(*rand_ranges[i])
            break
        pre_sum += r
    suffix_value = 0.0
    if random.random() < 0.5:
        suffix_value = random.randint(1, (10**max_suffix) - 1)/ (10**max_suffix)
    # print pre_value + suffix_value
    return str(pre_value + suffix_value)

def get_amount_in_words(value, capital=True, prefix=False):
    '''人民币数字转大写汉字
    参数:
    capital:    True   大写汉字金额
                False  一般汉字金额
    prefix:     True   以'人民币'开头
                False, 无开头
    '''
        
    # 汉字金额前缀
    if prefix is True:
        prefix = '人民币'
    else:
        prefix = ''
        
    # 汉字金额字符定义
    dunit = ('角', '分')
    if capital:
        num = ('零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖')
        iunit = [None, '拾', '佰', '仟', '万', '拾', '佰', '仟','亿', '拾', '佰', '仟', '万', '拾', '佰', '仟']
    else:
        num = ('〇', '一', '二', '三', '四', '五', '六', '七', '八', '九')
        iunit = [None, '十', '百', '千', '万', '十', '百', '千','亿', '十', '百', '千', '万', '十', '百', '千']
    iunit[0] = '元' if random.randint(1, 100) < 50 else '圆'

    # 转换为Decimal，并截断多余小数
    if not isinstance(value, Decimal):
        value = Decimal(value).quantize(Decimal('0.01'))

    # 处理负数
    if value < 0:
        prefix += '负'          # 输出前缀，加负
        value = - value         # 取正数部分，无须过多考虑正负数舍入
                                # assert - value + value == 0
    # 转化为字符串
    s = str(value)
    if len(s) > 19:
        return None
    istr, dstr = s.split('.')           # 小数部分和整数部分分别处理
    istr = istr[::-1]                   # 翻转整数部分字符串
    so = []     # 用于记录转换结果
    
    # 零
    if value == 0:
        return (prefix + num[0] + iunit[0])
        # .decode('utf8')
    haszero = False     # 用于标记零的使用
    if dstr == '00':
        haszero = True  # 如果无小数部分，则标记加过零，避免出现“圆零整”
        
    # 处理小数部分
    # 分
    if dstr[1] != '0':
        so.append(dunit[1])
        so.append(num[int(dstr[1])])
    # 角
    if dstr[0] != '0':
        so.append(dunit[0])
        so.append(num[int(dstr[0])])
    elif dstr[1] != '0':
        so.append(num[0])       # 无角有分，添加“零”
        haszero = True          # 标记加过零了
    else:
        so.append('整')         # 无分无角，则加“整”
        
    # 无整数部分
    if istr == '0':
        if haszero:             # 既然无整数部分，那么去掉角位置上的零
            so.pop()
        so.append(prefix)       # 加前缀
        so.reverse()            # 翻转
        return ''.join(so)
        # .decode('utf8')

    # 处理整数部分
    for i, n in enumerate(istr):
        n = int(n)
        if i % 4 == 0:                          # 在万、亿等位上，即使是零，也必须有单位
            if i == 8 and so[-1] == iunit[4]:   # 亿和万之间全部为零的情况
                so.pop()                        # 去掉万
            so.append(iunit[i])
            if n == 0:                          # 处理这些位上为零的情况
                if i != 0:                      # 在元位为零除外
                    if not haszero:             # 如果以前没有加过零
                        so.insert(-1, num[0])   # 则在单位后面加零
                        haszero = True          # 标记加过零了
                else:
                    haszero = True
            else:                               # 处理不为零的情况
                so.append(num[n])
                haszero = False                 # 重新开始标记加零的情况
        else:                                   # 在其他位置上
            if n != 0:                          # 不为零的情况
                so.append(iunit[i])
                so.append(num[n])
                haszero = False                 # 重新开始标记加零的情况
            else:                               # 处理为零的情况
                if not haszero:                 # 如果以前没有加过零
                    so.append(num[0])
                    haszero = True

    # 最终结果
    so.append(prefix)
    so.reverse()
    return ''.join(so)
    # .decode('utf8')

def get_cn_amount():
    amount_number = get_amount_number()
    return get_amount_in_words(amount_number)

def get_interest_rate():
    result = str(random.randint(1, 100))
    result += u'.' + u'0'*random.randint(4, 7)
    if random.random() < 0.5:
        result += u'‰'
    else:
        result += u'%'
    return result

def get_year():
    return str(random.randint(1000, 9999))

def get_month():
    number = random.randint(1, 12)
    return "%02d" %  number
    
def get_day():
    number = random.randint(1, 30)
    return "%02d" %  number

def get_random_colon():
    if random.random() < 0.5:
        return ':'
    return '：'

def get_random_space(max_n=4):
    return ' '*random.randint(0, max_n)

def get_random_cn(max_n=20):
    str_cn = ''
    cn_charset = cn_words_first + cn_words_second
    n = 0
    while n < max_n:
        c = cn_charset[random.randint(0,len(cn_charset)-1)]
        str_cn +=c
        n+=1
    return str_cn

