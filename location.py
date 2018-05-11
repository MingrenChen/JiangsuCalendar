import urllib.request as request
import urllib.parse as parse
import json
from bs4 import BeautifulSoup


def generateURL(name):
    code = parse.quote(name)
    return "http://db.qiumibao.com/f/index/team?name=" + code


def getPark(name):
    headers = {
        "Host": "db.qiumibao.com",
        "Connection": "keep-alive",
        "Accept": "application/json, text/plain, */*",
        "Origin": "http://data.zhibo8.cc",
        "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Mobile Safari/537.36",
        "DNT": "1",
        "Referer": "http://data.zhibo8.cc/html/team.html?match=%E4%B8%AD%E8%B6%85&team=%E6%B1%9F%E8%8B%8F%E8%8B%8F%E5%AE%81",
        "Accept-Encoding": "UTF-8",
        "Accept-Language": "zh-CN,zh;q=0.9"
    }
    req = request.Request(generateURL(name),  headers=headers)
    content = request.urlopen(req)
    jsonString = BeautifulSoup(content, "lxml").find('p').text
    obj = json.loads(jsonString)
    return obj['info']['ball_park']

