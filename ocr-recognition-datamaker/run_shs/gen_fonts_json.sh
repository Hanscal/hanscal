#!/bin/bash

# git reset --hard

# git clean -xdf

# git pull

help_word='use this script like: \nbash auto_process.sh config_path'

if [ ! -n "$1" ] ;then
    echo "you have not input a config_path!"
    echo -e $help_word
    echo 'format refer to src/tools/font_utils/config'
    exit 1
fi

config_path=$1

source $config_path

# 输出ttx目录
mkdir -p $TTX_DATA_DIR


if [[ "$RUN_MODE" == "all" ]];then
    REAL_FONTS_DIR=$INPUT_FONTS_DIR

elif [[ "$RUN_MODE" == "new" ]];then
    REAL_FONTS_DIR=$NEW_FONTS_DIR
else
    echo "RUN_MODE only support 'all' and 'new'"
    exit 8
fi

echo 'fonts path:'$REAL_FONTS_DIR

# 在ttf文件名中把空格之类的字符消掉
echo "font name preprocess"
cd ${config_path//base_config.cfg/..}
python3 preprocess_fonts_name.py -i $REAL_FONTS_DIR

# 生成ttx文件
echo "generate ttx file"
python3 make_ttx_data.py -i $REAL_FONTS_DIR \
                         -o $TTX_DATA_DIR

# 如果是新加入字体，将新的字体文件copy到总目录
if [[ "$RUN_MODE" == "new" ]];then
    cd $REAL_FONTS_DIR
    for file in $(ls *.ttf)
    do
        file_name="${file%.*}".ttf
        tgt_path=$INPUT_FONTS_DIR/$file_name
        if [ ! -f "$tgt_path" ];then
            cp $REAL_FONTS_DIR/$file_name $INPUT_FONTS_DIR/$file_name
        fi
    done
    cd -
fi

mkdir -p $OUTPUT_FONTS_DIR

# 生成最终选择的字体
# echo "make subset fonts"
#python3 make_subset_fonts.py  -i $REAL_FONTS_DIR \
#                              -c $CHARSET_PATH \
#                              -o $OUTPUT_FONTS_DIR


# 生成字体的字符集json
echo "generate fonts_charset json data"
python3 make_fonts_charset.py -i $TTX_DATA_DIR \
                              -o $OUTPUT_FONTS_DIR/fonts_char.json \
                              -c $CHARSET_PATH \
                              -p 4 \
                              -f $OUTPUT_FONTS_DIR/font_name_list.json

# 生成字体图片集
echo "visualize the fonts to image"
mkdir -p $OUTPUT_FONTS_DIR/draw_fonts
python3 visual_fonts.py -i $REAL_FONTS_DIR -o $OUTPUT_FONTS_DIR/draw_fonts -c $CHARSET_PATH
