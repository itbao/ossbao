#!/bin/env python
# -*- coding: utf-8 -*-

import yaml
import os
from osslib.ossbao import OssBao

with open("oss.conf") as ossf:
    oss_conf = yaml.load(ossf)

ossb = OssBao(
        access_key_secret=oss_conf['access_key_secret'],
        access_key_id=oss_conf['access_key_id'],
        bucket_name=oss_conf['bucket_name'],
        endpoint=oss_conf['endpoint'],
        )

public_f = 'public_config.json'

ossb.oss_get(public_f, 'my.json')
