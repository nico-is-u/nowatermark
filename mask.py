# coding=utf-8

# desc: 主要用于水印图片的制作和输出

from nowatermark import WatermarkRemover2

# 水印
image_path = './mask'
mask_name = 'mask.jpg'

remover = WatermarkRemover2()
remover.filter_mask(image_path,mask_name)



# 图片去色
# image_path = './mask'
# image_name = '155fun.jpeg'
# remover = WatermarkRemover2()
# remover.remove_image_color(image_path,image_name)
