#coding: utf-8
#获取微信推送封面图
import urllib.request
import webbrowser
from time import sleep
#获取网页源码，返回值为html
def getHtml(url):
    page = urllib.request.urlopen(url)
    html = page.read()
    return html
#用来判断是否是微信页
def web_if(site):
    if 输入.find("mp.weixin.qq.com") > 0:
        print("地址检查通过")
        return "1"
    else:
        print("地址检查未通过，请确保输入了正确的推送链接")
#
def main0():
    #获取源码
    html = getHtml(输入)
    html_str = str(html,'utf-8')
    #查找msg_cdn_url在源码中的位置
    搜索量 = 'msg_cdn_url'
    位置1 = html_str.find(搜索量)
    位置2 = 位置1 + 14
    位置3 = html_str.find('"',位置2 + 1)
    起始位置 = 位置2 + 1
    结束位置 = 位置3 - 1
    print("起始位置：", 起始位置)
    print("结束位置：", 结束位置)
    地址 = html_str[起始位置: 结束位置 + 1]
    print("微信推送封面图的地址如下，3秒后将使用浏览器打开。在浏览器右键保存即可")
    print(地址)
    sleep(3)
    webbrowser.open(地址)
#欢迎语
print("欢迎使用微信推送封面图下载")
print("程序由文轩制作")
print("2019.05")
print("-" * 50)

#主流程
#获取用户输入
输入 = input("请在此输入或粘贴微信推送链接:\n")
print("内部判断返回值", web_if(输入))
while  not web_if(输入):
    输入 = input("请在此输入或粘贴微信推送链接:\n")
main0()

