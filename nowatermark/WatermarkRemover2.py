import re
import cv2

from .WatermarkRemover import WatermarkRemover

class WatermarkRemover2(WatermarkRemover):

    image_path = ''                     # 图片目录路径
    mask_name = ''                      # 水印文件路径
    image_name = ''                     # 原图文件名
    image_suffix = ''                   # 原图文件后缀

    dev_output = False                  # 调试输出

    def __init__(self):
        super().__init__()
        # 打开调试输出
        # self.dev_output = True

    """ 给图片消去水印 """
    def remove_watermark2(self,image_path,mask_name,mask2_name,image_name):

        self.image_path = image_path
        
        # 得到文件名和后缀
        re_result = re.split('\.',image_name)
        self.image_name = re_result[0]
        self.image_suffix = re_result[1]
    
        self.image2_name = f'{self.image_name}-2'
        
        # 加载水印
        self.generate_template_gray_and_mask(f'{self.image_path}/{mask_name}',f'{self.image_path}/{mask2_name}')

        # 去除水印
        self.remove_watermark(f'{self.image_path}/{self.image_name}.{self.image_suffix}',f'{self.image_path}/{self.image2_name}.{self.image_suffix}')


    """ 图片去色 """
    def remove_image_color(self,image_path,image_name):
        self.image_path = image_path

        # 得到文件名和后缀
        re_result = re.split('\.',image_name)
        self.image_name = re_result[0]
        self.image_suffix = re_result[1]
    
        image2_name = f'{self.image_path}/{self.image_name}-2.{self.image_suffix}'

        # 原图
        img = cv2.imread(f'{self.image_path}/{self.image_name}.{self.image_suffix}')
        # 灰度图
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # 输出
        cv2.imwrite(image2_name,gray)


    """ 水印图片膨胀后取得边缘，便于在photoshop中进一步处理（白底实心）"""
    def filter_mask(self,image_path,mask_name):

        # 得到文件名和后缀
        re_result = re.split('\.',mask_name)
        mask_name = re_result[0]
        mask_suffix = re_result[1]
    
        # 水印模板原图
        img = cv2.imread(f'{image_path}/{mask_name}.{mask_suffix}')
        
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, mask = cv2.threshold(gray, 0, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)
        _, mask = cv2.threshold(mask, 127, 255, cv2.THRESH_BINARY)

        mask = self.dilate(mask)  # 使得掩码膨胀一圈，以免留下边缘没有被修复
        mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # 输出
        cv2.imwrite(f'{image_path}/{mask_name}-2.{mask_suffix}',mask)

    """ 图片归一化测试 """


