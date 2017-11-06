# ossbao

## 简单介绍
- push_oss_file.py 根据出口公网IP变化，更新aliyun OSS中的文件，需要OSS的bucket读写权限。
- get_oss_file.py 下载最新的IP信息文件，需要OSS的bucket读权限。

## 基本用法
```shell
# 修改配置
mv oss.conf_example oss.conf

# 修改上传数据文件
mv public_config.json_example public_config.json

# 让push功能安时间间隔自动执行
nohup bash daemon.sh &
```

