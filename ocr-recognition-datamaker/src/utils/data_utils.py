# coding:utf-8

import os, sys, random, math
from PIL import Image, ImageDraw

def save_label_list(output_path, label_list):
    with open(output_path, 'w') as f:
        for label in label_list:
            try:
                f.write(','.join([unicode(i).encode('utf-8') for i in label[:4]]))
                f.write(',"{}"\n'.format(unicode(label[-1]).encode('utf-8')))
            except Exception as e:
                print (e, label)

def save_det_data(output_dir, name_id ,img, label_list):
    img.save(os.path.join(output_dir, '{}.jpg'.format(name_id)))
    save_label_list(os.path.join(output_dir, '{}.txt'.format(name_id)), label_list)


def save_reg_data(output_dir, name_id, crop_img, text, aug_func, writer):
    # target_img = aug_func(crop_img.resize((256, 32) ))
    target_img = aug_func(crop_img)
    w, h = target_img.size
    if w > 100 and h > 64:
        scale_r = 64.0 / h
        target_img = target_img.resize(( int(w*scale_r), 64))
    # target_img = target_img.convert('L')
    target_img.save(os.path.join(output_dir, name_id + '.jpg'))
    writer.write('{}.jpg {}\n'.format(name_id, text))
