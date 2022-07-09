#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Description: redis used to communitcate with redis-server
Author: Prabal Pathak
"""


import redis


redis_client = redis.Redis()

redis_client.mset({"name":"Prabal Pathak", "age": 23, "group": "A"})
print(redis_client.hgetall())
