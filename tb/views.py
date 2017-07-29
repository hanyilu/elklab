# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
import re
from selenium import webdriver
import os
import platform


def index(request):
    siteURL = 'https://s.taobao.com/search?search_type=item&commend=all&q=%E8%BF%9E%E8%A1%A3%E8%A3%99&_input_charset=utf-8&wq=lianyiqun&suggest_query=lianyiqun&source=suggest&style=list&filter=reserve_price%5B100%2C250%5D'

    dir_path = os.path.join(os.path.dirname(__file__), "phantom")
    phantomjs_path = 'phantomjs' if 'linux' in platform.system().lower() else 'phantomjs_dev'
    print dir_path
    driver = webdriver.PhantomJS(executable_path=os.path.join(dir_path, phantomjs_path),
                                 service_log_path=os.path.join(dir_path, 'ghostdriver.log'))

    driver.get(siteURL)
    driver.implicitly_wait(30)
    page = driver.page_source
    pattern = re.compile(
        r'<div class="item g-clearfix">.*?<img.*?alt="(.*?)">.*?"title".*?<a.*?href="(.*?)".*?shopname.*?href="(.*?)".*?<span>(.*?)</span>.*?price.*?<strong>(.*?)</strong>.*?<p class="deal-cnt">(\d*)',
        re.S
    )
    items = re.findall(pattern, page)
    print items
    return render(request, 'search.html', {'item_list': items})