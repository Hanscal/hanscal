#!/usr/bin/env bash

ROOT_DIR=`pwd`
ROOT_DIR=$ROOT_DIR/..

cd $ROOT_DIR/src

background_dir=/data/caihua/scripts/ocr-recognition-datamaker/text_renderer/data/background
fonts_dir=/data/caihua/scripts/ocr-recognition-datamaker/text_renderer/data/fonts
out_root=/data/caihua/data/vanke
gen_number=200000

nohup python3 run.py --config config/config_server.yaml \
                        --bg_dir $background_dir \
                        --font_dir $fonts_dir \
                        --font_chars $fonts_dir/../fonts_char.json \
                        --gen_number 3000  \
                        --output_dir $out_root/test_data \
                        --pre_fix reg_test > reg_test.log 2>&1 &


