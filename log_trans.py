# -*- coding: utf-8 -*-
import os
import paramiko
import re
import time
import requests

remote_file_path = "/home/logs/ppcloud/common-all.log"
log_mark=r'''http://115.231.44.26/ws/liveipn/'''
proxy_domain=r'''115.231.44.26'''
qa_domain=r'''10.200.24.71'''
qa_url_path=r'''http://svc.pptvyun.com/svc/v1/api/channel/streamstatus/'''


def demo():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect('10.200.13.226', username='robertpicyu', password='RObertpicyul_111_')

    chan = ssh.invoke_shell()
    #chan.settimeout(5)
    chan.send('ssh 115.231.44.26\n')
    buff = ''
    while not buff.endswith('\'s password: '):
        resp = chan.recv(9999)
        buff += resp

    chan.send('RObertpicyul_111_\n')
    buff = ''
    while not buff.endswith(r'~]$ '):
        resp = chan.recv(9999)
        buff += resp

    buff = ""
    chan.send("cat /home/logs/ppcloud-livedemo-api/common-all.log\n")
    time.sleep(1)
    while True:
        buff += chan.recv(10000)
        # 清除buff，只留下最后一行
        buff = transpond_call_bak(buff)
        time.sleep(0.1)
    ssh.close()

## 提取log日志中的目标行，并返回最后一行
def transpond_call_bak(logs):
    for line in logs.splitlines():
        if(line.find(log_mark) != -1):
            print line
            trans_to_qa(line)
    return line

## ，并转发到内网测试环境
def trans_to_qa(request):
    urlPattern = re.compile(r'''url:([^,]*)''')
    url = urlPattern.search(request).group(1)
    queryPattern = re.compile(r'''query:([^,]*)''')
    query = queryPattern.search(request).group(1)
    query = query.strip()
    reqUrl = url.replace(log_mark,qa_url_path)+"?"+query
    html = requests.get(reqUrl)
    print reqUrl

demo()
