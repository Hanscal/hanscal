#!/usr/bin/env bash

ROOT_DIR=`pwd`
ROOT_DIR=$ROOT_DIR/../../..

cd $ROOT_DIR

#background_dir=/data/caihua/scripts/text_renderer/data/background/bg
#fonts_dir=/data/caihua/scripts/text_renderer/data/fonts
#out_root=/data/caihua/scripts/ocr-recognition-datamaker/run_shs/output
#gen_number=200

background_dir=/data/caihua/data/fonts/idcard/all_bg
fonts_dir=/data/caihua/data/fonts/idcard/fonts
out_root=/data_ssd/ocr/caihua/cn/idcard
gen_number=600000

for i in {1..5};do
nohup python3 src/run.py --config run_shs/exp_sh/idcard/config_server.yaml \
                        --bg_dir $background_dir \
                        --font_dir $fonts_dir \
                        --font_chars $fonts_dir/fonts_char.json \
                        --gen_number $gen_number \
                        --output_dir $out_root/output_reg$i \
                        --pre_fix reg$i_  > $ROOT_DIR/run_shs/log/reg_$i.log 2>&1 &
done

nohup python3 src/run.py --config run_shs/exp_sh/idcard/config_server.yaml \
                     --bg_dir $background_dir \
                     --font_dir $fonts_dir \
                     --font_chars $fonts_dir/fonts_char.json \
                     --gen_number 1000  \
                     --output_dir $out_root/test_data \
                     --pre_fix reg_test > $ROOT_DIR/run_shs/log/reg_test.log 2>&1 &

