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


public_f = 'public_config.json'

now = datetime.datetime.now()
logtime=now.strftime('%Y-%m-%d %H:%M:%S')

if not os.path.exists(public_f):
    print '%s oss_get ...' % logtime
    ossb.oss_get(public_f, public_f)

new_ip = ossb.get_public_ip()

if ossb.check_update(new_ip, public_f):
    ossb.oss_push(public_f, public_f)
else:
    print '%s No update!' % logtime

