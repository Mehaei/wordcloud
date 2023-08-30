

# -*- coding: utf-8 -*-
# @Author: Mehaei
# @Date:   2023-08-29 20:23:38
# @Last Modified by:   Mehaei
# @Last Modified time: 2023-08-30 21:14:22
# 导入需要使用的模块
import matplotlib.pyplot as plt
import jieba
import wordcloud
from wordcloud import ImageColorGenerator
import numpy as np
from PIL import Image


class genCordCloudPic(object):
    """
    生成词云图类
    """
    def __init__(self, ftext, fbg=None, fsave="wordcloud.png"):
        """
        :param ftext: 文本文件路径
        :param fbg: 背景图片路径
        :param fsave: 词云图片保存路径
        """
        self.ftext = ftext
        self.fbg = fbg
        self.fsave = fsave

    def getWord(self):
        """
        读取文本文件
        """
        with open(self.ftext, 'r+') as f:
            text = f.read()
        cut_text = jieba.cut(text)
        return ' '.join(cut_text)

    def save_pic(self, use_bg_color=False, **wordcloud_kwargs):
        """
        保存词云图
        :param use_bg_color: 使用背景图片颜色渲染词云图的颜色
        """
        word = self.getWord()
        if not word:
            raise ValueError("分词结果为空")
        if not self.fbg:
            raise ValueError("背景图片为空")
        pic = np.array(Image.open(self.fbg))
        # 生成图片颜色中的颜色
        image_colors = ImageColorGenerator(pic)
        wd = wordcloud.WordCloud(
            mask=pic,
            font_path='97txj03p17q39w692ecpjely52o1v6z9.ttf',
            background_color='white',
            max_font_size=100,
            scale=2,
            max_words=500,
            **wordcloud_kwargs
        ).generate(word)
        if use_bg_color:
            wd.recolor(color_func=image_colors)
        plt.imshow(wd, interpolation='bilinear')
        # 关闭显示x轴、y轴下标
        plt.axis('off')
        plt.show()
        wd.to_file(self.fsave)


# 生成随机颜色的图片
# gccp = genCordCloudPic("text.txt", "goutou.png", "random_color.png")
# gccp.save_pic()


# 生成与背景图片颜色一致的图片
gccp = genCordCloudPic("text.txt", "goutou.png", "bg_color.png")
gccp.save_pic(use_bg_color=True)

