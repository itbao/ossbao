#!/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
from osslib.ossbao import OssBao
import datetime


with open("oss.conf") as ossf:
    oss_conf = yaml.load(ossf)

ossb = OssBao(
        access_key_secret=oss_conf['access_key_secret'],
        access_key_id=oss_conf['access_key_id'],
        bucket_name=oss_conf['bucket_name'],
        endpoint=oss_conf['endpoint'],
        )


new_public_f = 'public_config.json'
alioss_public_f = 'alioss_public_config.json'



now = datetime.datetime.now()
logtime=now.strftime('%Y-%m-%d %H:%M:%S')

#if not os.path.exists(new_public_f):
#    print '%s oss_get ...' % logtime
#    ossb.oss_get(public_f, new_public_f)

new_ip = ossb.get_public_ip()

if not os.path.exists(new_public_f):
    data = {"peIp": "no"}
    ossb.touch_json_file(new_public_f,data)

if os.path.exists(alioss_public_f):
    if ossb.check_change(new_ip, alioss_public_f):
        ossb.update(new_ip,new_public_f)
        ossb.oss_push(new_public_f, new_public_f)
    else:
        print '%s No update!' % logtime
else:
    ossb.oss_push(new_public_f, new_public_f)
