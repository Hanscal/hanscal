## 印章图片生成工具

运行：
```
python3 run.py --config configs/seal_conf.yaml   # 生成印章相关配置
			   --bg_dir bg_imgs/                 # 背景图目录
			   --font_dir fonts/                 # 字体目录
			   --gen_number 100                  # 生成图片数量
			   --output_dir output/              # 输出目录
			   --pre_fix p                       # 输出文件名固定前缀
```

配置：

```
min_font_size: 20              # 最小字体size
max_font_size: 30      		   # 最大字体size
max_content_length: 15         # 最大文本长度
image_width: 224               # 印章图片宽度
image_height: 224              # 印章图片高度
contents:                      # 生成文本配置
  -
    id: company
    corpus_path: data/corpus/company.txt
    w: 1.0
seal_base:                     # 印章相关配置
  min_radius: 100              # 印章外圈最小半径
  max_radius: 110              # 印章外圈最大半径
  min_circle_width: 4          # 印章外圈最小宽度
  max_circle_width: 9          # 印章外圈最大宽度
  min_star_radius: 20          # 印章中心五角星最小半径
  max_star_radius: 35          # 印章中心五角星最大半径
  min_interval_angle: 18       # 字符最小间隔角度
  max_interval_angle: 22       # 字符最大间隔角度


```

