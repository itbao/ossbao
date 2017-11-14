#!/bin/env python
# -*- coding: utf-8 -*-

import oss2
import os
import time
import json
import urllib2
import shutil

class OssBao():
    def __init__(self, access_key_id, access_key_secret, bucket_name, endpoint):

        self.bucket = oss2.Bucket(
                oss2.Auth(access_key_id, access_key_secret),
                endpoint,
                bucket_name
                )

    def get_public_ip(self):
        req = urllib2.Request('http://ip.cip.cc')
        response = urllib2.urlopen(req)
        return response.read().strip('\n')

    @staticmethod
    def write_json_file(conf,data):
        with open(conf, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def read_json_file(conf):
        with open(conf, 'r') as f:
            return json.load(f)


    def check_change(self, new_ip, cfile):
        data = OssBao.read_json_file(cfile)
        if data['peIp'] == new_ip:
            return False
        else:
            return True

    def touch_json_file(self, cfile, data):
        OssBao.write_json_file(conf=cfile, data=data)


    def update(self, new_ip, cfile):
            data = OssBao.read_json_file(cfile)
            data['peIp'] = new_ip
            OssBao.write_json_file(cfile, data)

    def oss_get(self, oss_file, local_file):
        self.bucket.get_object_to_file(oss_file, local_file)

    def oss_push(self, oss_file,local_file):
        self.bucket.put_object_from_file(oss_file, local_file)
        shutil.copy(local_file, 'alioss_%s' % local_file)

        for i, object_info in enumerate(oss2.ObjectIterator(self.bucket)):
            timeArray = time.localtime(object_info.last_modified)
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            print("{0} {1}".format(otherStyleTime, object_info.key))
            if i >= 9:
                break

