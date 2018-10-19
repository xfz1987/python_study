import urllib
import urllib.request
import re

def get_html(url):
  page = urllib.request.urlopen(url)
  html = page.read
  return html

reg = r'src="(.+?\.jpg)" width'
reg_img = reg.compile(reg)
imglist = reg_img.findall(get_html('http://xxxx'))

x = 0

# 如果imglist有100万张图片，则 需要分成4个部分来做，4*10
for img in imglist:
  urllib.urlretrieve(img, '%s.jpg', %x)
  x += 1

# regx101