# Installation

```
pip install fonttools 
pip install pillow
```

# fonttools
这个工具主要依赖于fonttools，需要扩展功能可以参考：
https://github.com/fonttools/fonttools

# 获取字体的一个子集
使用make_subset_fonts.sh脚本可以把字体中的一部分字符提取出来，生成一个新的字体，可以降低字体的大小。

字符集文件可以参考：word_set/words.txt
```
bash make_subset_fonts.sh input_font_dir output_dir word_set_file
```

# 生成ttx文件
ttx文件是将字体转化为对应的json文件，其中有字体相关的全部信息，文件格式为fonttools中的定义。

```
bash make_ttx_data.sh /input_fonts_dir /output_dir
```

# 获取字体的字符集
由于字体中的字符可能不全，这个脚本可以给出字体中包含哪些给定范围内的字符。
```
python3 get_fonts_charset.py --input_ttx_dir ttx_dir --output_path save_file --charset_path word_set/word.txt
```
参数说明：
- input_ttx_dir: 输入的ttx文件夹，脚本从ttx文件中获取字符信息。
- output_path: 输出文件路径。输出为json格式，是{"font_name": "charset"}的dict。
- charset_path： 给定字符集。



# 字符内容可视化
把给定字符集中的字符贴在图片上输出。
```
python draw_all_words_to_img.py --input_fonts_dir fonts_dir --output_dir save_dir --charset_path word_set/word.txt
```

# 所有步骤联合执行脚本
上述脚本串连执行，允许添加新字体等
```
bash auto_process.sh config/base_config.cfg
```