#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
from random import randint

# 获取 CGI URL 参数，以判断输出 TXT 或者 JSON 版本
arguments = cgi.FieldStorage()

# 默认输出 TXT 格式的『名言』
version = arguments.getvalue('v', 'txt')

# 从一个  tuple 或者 list 中随机获取一项
def get_random_item(some_list):
    return some_list[randint(0, len(some_list)-1)]

# 从外部文件读取到列表。姓名列表来自 https://github.com/dominictarr/random-name
def get_list_from_file(filepath):
    the_list = []
    with open(filepath, 'r') as name_file:
        for line in name_file.readlines():
            if line.strip() != '':
                the_list.append(line.strip())

    return the_list

# 从列表名得到文件地址
def get_path(list_name):
    return 'lists/' + list_name + '.txt'

# 姓名列表
file_path_list = list(map(get_path, ['first_name', 'last_name', 'moods', 'countries', 'professions', 'fruits', 'languages', 'advantages', 'companies', 'company_types', 'job_titles', 'descriptions']))
first_names, last_names, moods, countries, professions, fruits, languages, advantages, companies, company_types, job_titles, descriptions = list(map(get_list_from_file, file_path_list))

# TODO: 模板要分离出去
# FIXME: 减少逻辑和模板的耦合度

# 随机决定使用哪个模板
random_int = randint(0, 3)

if random_int == 0:
    # 生成用于格式化字符串的参数
    args_list = (None, None)

    while args_list[0] == args_list[1] :    # 避免重复生成两个相同的 mood
        # map 的结果是 list (Python 3 下是 map object)，必须转为 tuple 才可以用于格式化字符串
        args_list = tuple(map(get_random_item, (moods, moods, countries, professions, first_names, last_names)))

    # 生成第一种「名言」
    quote = '%s的本质是一种隐藏的%s。  --- %s著名%s %s %s'  % args_list        

elif random_int == 1:
    args_list = tuple(map(get_random_item, (languages, advantages, descriptions, companies, company_types, job_titles, first_names, last_names)))
    quote = '我认为 %s 是世界上最好的语言，它的%s让我们的团队%s。 --- %s %s %s %s %s' % args_list

elif random_int == 2:
    args_list = tuple(map(get_random_item, (fruits, moods, countries, professions, first_names, last_names)))
    quote = '%s是甜的。这是一种让人感到%s的甜。 --- %s著名%s %s %s' % args_list

elif random_int == 3:
    args_list = tuple(map(get_random_item, (languages, fruits, advantages, companies, job_titles, first_names, last_names)))
    quote = '%s 语言就像%s一样，需要细细品味，才能充分体会它那愈久弥深的%s。 --- %s 公司 %s : %s %s' % args_list

if version == 'txt':
    print('Content-Type: text/plain')
    print('')
    print(quote)
elif version == 'json':
    print('Content-Type: application/json')
    print('')
    quote, author = map(str.strip, (quote.split('---')))  # 分开名言和作者
    print('{"quote": "' + quote + '", "author": "' + author + '" }')
else:
    print('Status: 403')    # 参数不对禁止访问哦
    print('')
