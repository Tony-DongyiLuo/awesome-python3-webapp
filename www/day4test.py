#!usr/bin/env python3
#-*- coding: utf-8 -*-

from www import orm
import asyncio
import sys
from www.models import User, Blog, Comment

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='password',db='awesome')

    u = User(name='Tony', email='Tony@example.com', passwd='dddd', image='about:blank')

    await u.save()

if __name__ == '__main__':
        loop = asyncio.get_event_loop()
        loop.run_until_complete(asyncio.wait([test(loop)]))
        loop.close()