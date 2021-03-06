#!/usr/bin/env bash
ROOT_DIR=`pwd`
ROOT_DIR=$ROOT_DIR/..

base_data_dir=$ROOT_DIR/datas/corpus_input
existing_corpus_dir1=/data/caihua/data/wiki
existing_corpus_dir2=$base_data_dir
generate_number_rand=300
generate_number_semantic=1000000
output_dir=$ROOT_DIR/datas/corpus_output

for var in $existing_corpus_dir1 $existing_corpus_dir2; do
    cd $var
    for file in $(ls *.txt)
        do
            file_name="${file%.*}".txt
        echo "copy:$file_name"
            if [ ! -f "$tgt_path" ];then
                cp $var/$file_name $base_data_dir/$file_name
            fi
        done
done

echo $base_data_dir
sed -i "s#corpus_base_dir:.*#corpus_base_dir: $base_data_dir#" $ROOT_DIR/src/config/config_server.yaml

cd $ROOT_DIR
#echo "随机文本"
#python3 src/corpus_generate_script/generate_random_sequence.py -n $generate_number_rand -o $output_dir/rand_chinese.txt

echo "语义文本"
python3 src/corpus_generate_script/generate_semantic_sequence.py -n $generate_number_semantic -i $base_data_dir -o $output_dir/sementic_corpus.txt

#echo "特定文本"
#python3 src/corpus_generate_script/generate_specific_sequence.py -n $generate_number -o $output_dir/specific_corpus.txt
