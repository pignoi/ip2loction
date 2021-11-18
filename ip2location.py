import urllib.request
import socket

def ip2loc1(wip):
    tool1 = 'https://ip38.com/ip.php?ip='
    url = tool1 + wip
    while True:
        req=urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
        
        sta = urllib.request.urlopen(req).getcode()
        
        if sta == 200:
            fhtml = urllib.request.urlopen(req)
            lines = fhtml.readlines()
            for line in lines:
                line = line.decode()
                if 'IP详细地址' in line:
                    loc = line.split('<font color=#FF0000>')[2].split('</font>')[0]
                    break
            return loc
        if sta == 403:
            print('403 forbidden')
            break

def ip2loc2(wip):
    socket.setdefaulttimeout(15)
    tool1 = 'https://ip.cn/ip/'
    url = tool1 + wip + '.html'
    while True:
        req=urllib.request.Request(url)
        req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36')
        
        # sta = urllib.request.urlopen(req).getcode()

        try:
            fhtml = urllib.request.urlopen(req)
            lines = fhtml.readlines()
            for line in lines:
                line = line.decode()
                if 'tab0_address' in line:
                    loc = line.split('>')[1].split('<')[0]
                    return loc

        except urllib.error.HTTPError:
            return 0
        
        except socket.timeout:
            return 0
        
