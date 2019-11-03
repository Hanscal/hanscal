#!/usr/bin/env bash

ROOT_DIR=`pwd`
ROOT_DIR=$ROOT_DIR/..

cd $ROOT_DIR/src

#background_dir=/data/caihua/scripts/text_renderer/data/background/bg
#fonts_dir=/data/caihua/scripts/text_renderer/data/fonts
#out_root=/data/caihua/scripts/ocr-recognition-datamaker/run_shs/output
#gen_number=200

background_dir=/data_ssd/ocr/liweihao/wanli/backgrounds
fonts_dir=/data_ssd/ocr/liweihao/wanli/fonts
out_root=/data_ssd/ocr/caihua/en/wanli_en
gen_number=200000

for i in {1..5};do
nohup python3 run.py --config config/config_server.yaml \
                        --bg_dir $background_dir \
                        --font_dir $fonts_dir \
                        --font_chars $fonts_dir/en_fonts_char.json \
                        --gen_number $gen_number \
                        --output_dir $out_root/output_reg$i \
                        --pre_fix reg$i_  > $ROOT_DIR/run_shs/log/reg_$i.log 2>&1 &
done

nohup python3 run.py --config config/config_server.yaml \
                     --bg_dir $background_dir \
                     --font_dir $fonts_dir \
                     --font_chars $fonts_dir/en_fonts_char.json \
                     --gen_number 300  \
                     --output_dir $out_root/test_data \
                     --pre_fix reg_test > $ROOT_DIR/run_shs/log/reg_test.log 2>&1 &

