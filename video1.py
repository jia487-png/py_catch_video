import requests          # 导入requests模块
import re                # 导入re模块
# 定义视频播放页面的url
url = 'http://site2.rjkflm.com:666/index/index/view/id/1.html'
# 定义请求头信息
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
response = requests.get(url=url,headers=headers)     # 发送网络请求
if response.status_code==200:   # 判断请求成功后
    # 通过正则表达式匹配视频地址
    video_url = re.findall('<source src="(.*?)" type="video/mp4">',response.text)[0]
    video_url='http://site2.rjkflm.com:666/'+video_url    # 将视频地址拼接完整
    video_response = requests.get(url=video_url,headers=headers)  # 发送下载视频的网络请求
    if video_response.status_code==200:    # 如果请求成功
        data = video_response.content      # 获取返回的视频二进制数据
        file =open('java视频.mp4','wb')    # 创建open对象
        file.write(data)                   # 写入数据
        file.close()                       # 关闭
