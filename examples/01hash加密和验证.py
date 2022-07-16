# !/usr/bin/python
# -*- coding: utf-8 -*-
"""
@File    :  z06_hash加密和验证.py
@Time    :  2022/7/16 7:30
@Author  :  张大鹏
@Version :  v0.1.0
@Contact :  lxgzhw@163.com
@License :  (C)Copyright 2022-2023
@Desc    :  描述
"""
from zdppy_password_hash.hash import pbkdf2_sha256

hash = pbkdf2_sha256.hash("toomanysecrets")
print(hash)

# 校验
print(pbkdf2_sha256.verify("toomanysecrets", hash))

# 校验
print(pbkdf2_sha256.verify("joshua", hash))
