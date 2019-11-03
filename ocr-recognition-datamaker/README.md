# ocr-recognition-datamaker
Generate corpus data and the needed data(e.g. image data).

## Libraries
- Imgaug -> pip instal imgaug
- common anaconda libs, e.g. PIL, math etc.

## File structure

```
ocr-recognition-datamaker/
├── README.md
├── datas
│   ├── charsets
│   │   ├── fonts_char.json
│   │   └── rpa_charset_v4.txt
│   └── corpus_data
│       └── xinchou.json
├── run_shs
│   ├── gen_corpus_local.sh
│   ├── gen_corpus_server.sh
│   ├── gen_data_local.sh
│   └── gen_data_server.sh
└── src
    ├── config
    │   ├── config_local.yaml
    │   └── config_server.yaml
    ├── corpus_generate_script
    │   ├── __init__.py
    │   ├── gen_rpa_words.py
    │   ├── generate_news.py
    │   ├── generate_random_cn.py
    │   ├── to_xinchou_json.py
    │   └── utils.py
    ├── libs
    │   ├── __init__.py
    │   ├── bg_generator.py
    │   ├── content_generator.py
    │   ├── draw_form.py
    │   ├── font_selector.py
    │   ├── position_selector.py
    │   ├── sp_utils
    │   │   ├── __init__.py
    │   │   └── wanke.py
    │   ├── special_draw.py
    │   └── text_paster.py
    ├── run.py
    ├── tools
    │   └── get_charset.py
    └── utils
        ├── __init__.py
        └── data_utils.py
        
```

## rpa训练数据v4版本

1. 添加了黑体
2. 添加了字符：犇
3. 调整了字体大小的范围