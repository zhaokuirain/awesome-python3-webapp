
import asyncio, os, inspect, logging, functools

from urllib import parse

from aiohttp import web

## apis是处理分页的模块,代码在本章页面末尾,请将apis.py放在www下以防报错
## APIError 是指API调用时发生逻辑错误
from apis import APIError

## 编写装饰函数 @get()
def get(path):
    ## Define decorator @get('/path')
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'GET'
        wrapper.__route__ = path
        return wrapper
    return decorator

 ## 编写装饰函数 @post()
def post(path):
    ## Define decorator @post('/path')
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            return func(*args, **kw)
        wrapper.__method__ = 'POST'
        wrapper.__route__ = path
        return wrapper
    return decorator

