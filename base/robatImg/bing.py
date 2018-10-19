#!usr/bin/python3
# --*-- coding:utf-8 --*--

'''
# 每天定时抓取Bing搜索的壁纸并保存在本地
## 分析Bing搜索的页面结构
## 分析Bing搜索的壁纸接口
## 根据分析的结果编码实现壁纸爬虫

# 技术点
## http组件: urllib
## json解析
## 文件操作
## 生成时间戳
'''

import urllib
import urllib.request
import ssl
import time
import json
import os.path

class BingBgDownloader(object):
  # _bing_interface = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1524048535881&pid=hp'
  _bing_interface = 'https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=%d&nc=%d&pid=hp'
  _bing_url = 'https://cn.bing.com/'
  # 规定文件名的格式
  _img_filename = '[%s%s][%s].%s'

  def __init__(self):
    super(BingBgDownloader, self).__init__()
    # 设置https
    ssl._create_default_https_context = ssl._create_unverified_context

  # 下载
  def download(self, num=1, local_path='./'):
    if num < 1:
      num = 1
    url = self._bing_interface%( num, int(time.time()) )
    img_info = self._get_img_infos(url)
    print(img_info)
    for info in img_info:
      print(self._get_img_filename(info))
      print(self._get_img_url(info))
      self._down_img(self._bing_url + self._get_img_url(info), local_path + self._get_img_filename(info))

  # 私有方法 从接口获取图片资源信息
  def _get_img_infos(self, url):
    request = urllib.request.urlopen(url).read()
    bgObjs = json.loads(bytes.decode(request))
    return bgObjs['images']

  # 从接口数据提取图片URL
  def _get_img_url(self, img_info):
    return img_info['url']
  
  # 从接口数据提取图片文件名
  def _get_img_filename(self, img_info):
    # 图片中文名
    zh_name = ''
    cr = img_info['copyright']
    pos = cr.index('(')

    if pos < 0:
      zh_name = cr
    else:
      zh_name = cr[0:pos]

    url = img_info['url']

    # 图片英文名
    en_name = url[url.rindex('/') + 1 : url.rindex('_ZH')]
    # 图片扩展名
    ex_name = url[url.rindex('.') + 1 : len(url)]
    # 分辨率
    pix = url[url.rindex('_'): url.rindex('.')]

    img_name = self._img_filename %(zh_name, en_name, pix, ex_name)

    return img_name

  # 下载图片
  def _down_img(self, img_url, img_path):
    print(img_url)
    # 读取图片
    img_data = urllib.request.urlopen(img_url).read()
    # 以二进制方式写文件
    f = open(img_path, 'wb')
    f.write(img_data)
    # 关闭
    f.close()
    print('success saved image:', img_url)

if __name__ == '__main__':
  dl = BingBgDownloader()
  dl.download(6, './downloads/')