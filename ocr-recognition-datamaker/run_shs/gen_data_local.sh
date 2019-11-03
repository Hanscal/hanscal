#!/usr/bin/env bash

ROOT_DIR=`pwd`
ROOT_DIR=$ROOT_DIR/..

cd $ROOT_DIR/src

background_dir=/Volumes/work/build-tools/ocr-recognition-datamaker/text_renderer/data/bg
fonts_dir=/Volumes/work/build-tools/ocr-recognition-datamaker/text_renderer/data/fonts
gen_number=100


python3 run.py --config config/config_local.yaml \
                --bg_dir $background_dir \
                --font_dir $fonts_dir \
                --font_chars $fonts_dir/../fonts_char.json \
                --gen_number $gen_number \
                --output_dir $ROOT_DIR/run_shs/output