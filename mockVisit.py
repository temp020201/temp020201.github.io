import urllib.request
import urllib.parse
 
url = "https://webvpn.neu.edu.cn/https/77726476706e69737468656265737421f2f50f92222526557a1dc7af96/bbcswebdav/pid-233737-dt-content-rid-2408118_1/xid-2408118_1"

headers = {
	'Accept': '*/*',
	'Accept-Encoding': 'gzip, deflate, br',
	'Accept-Language': 'zh-CN,zh;q=0.9',
	'Connection': 'keep-alive',
	'Cookie': 'show_vpn=0; wengine_vpn_ticketwebvpn_neu_edu_cn=77e8ba3e37af418c; refresh=0',
	'Host': 'webvpn.neu.edu.cn',
	'Referer': 'https://webvpn.neu.edu.cn/https/77726476706e69737468656265737421f2f50f92222526557a1dc7af96/bbcswebdav/pid-233737-dt-content-rid-2408118_1/xid-2408118_1',
	'Sec-Fetch-Dest': 'empty',
	'Sec-Fetch-Mode': 'cors',
	'Sec-Fetch-Site': 'same-origin',
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36',
}
request = urllib.request.Request(url=url,headers=headers)
response = urllib.request.urlopen(request)
#输出所有
# print(response.read().decode('gbk'))
#将内容写入文件中
with open('test.pdf','wb') as fp:
 fp.write(response.read())
