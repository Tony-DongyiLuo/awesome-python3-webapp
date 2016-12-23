#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Tony Luo'

' url handlers '

import re, time, json, logging, hashlib, base64, asyncio

from www.coroweb import get, post

from www.models import User, Comment, Blog, next_id

@get('/')
async def index(request):
    users = await User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }