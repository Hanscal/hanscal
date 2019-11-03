#!/usr/bin/env bash
ROOT_DIR=`pwd`
ROOT_DIR=$ROOT_DIR/..

cd $ROOT_DIR/src/corpus_generate_script

base_data_dir=$ROOT_DIR/datas/corpus_input
existing_corpus_dir=/data/caihua/data/NLP_data/cnews
generate_number=1000
output_dir=$ROOT_DIR/datas/corpus_output

cd $existing_corpus_dir
for file in $(ls *.txt)
    do  
        file_name="${file%.*}".txt
        if [ ! -f "$tgt_path" ];then
            cp $existing_corpus_dir/$file_name $base_data_dir/$file_name
        fi  
    done
cd -

echo $base_data_dir
sed -i "" "s#corpus_base_dir:.*#corpus_base_dir: $base_data_dir#" $ROOT_DIR/src/config/config_local.yaml

echo "随机文本"
python3 generate_random_sequence.py -n $generate_number -o $output_dir/random_corpus.txt

echo "语义文本"
python3 generate_semantic_sequence.py -n $generate_number -o $output_dir/sementic_corpus.txt

#echo "特定文本"
#python3 generate_specific_sequence.py -n $generate_number -o $output_dir/specific_corpus.txt