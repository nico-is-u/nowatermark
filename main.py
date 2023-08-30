# coding=utf-8
import cv2
from nowatermark import WatermarkRemover2

# 水印处理
image_path = './images'                         # 图片路径
mask_name = 'mask.png'                          # 水印图片
mask2_name = 'mask-2.jpg'                       # 水印拓补图

image_name = '2-2.jpeg'

remover = WatermarkRemover2()
remover.remove_watermark2(image_path,mask_name,mask2_name,image_name)


# 图形归一化测试
# image_path = './images'
# mask_name = 'mask.jpg'

# remover = WatermarkRemover2()
# mask_image = cv2.imread(f'{image_path}/{mask_name}')
# result = remover.normalize_image(mask_image,0,1)
# print (result)

