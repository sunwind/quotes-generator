#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
import sys
import os
from random import randint

# 启用 CGI 调试信息显示
import cgitb; cgitb.enable()

# 从一个 list 中随机获取一项
def get_random_item(some_list):
    return some_list[randint(0, len(some_list)-1)]

# TODO 提高效率。for 太多了。做一些 profiling
# 遍历 lists 文件夹读取各个列表到词典
def read_lists_to_dict(args_dict):
    try:
        for dirpath, dirnames, filenames in os.walk('lists'):
            for some_list_file in filenames:
                with open(os.path.join('lists', some_list_file), 'r') as some_list:
                    all_content = some_list.read().split()

                    all_content = [x for x in all_content if len(x.strip())]    # 过滤掉一些空行产生的空项

                args_dict[some_list_file.split('.txt')[0]] = all_content
    except Exception as e:
        print('Content-Type: text/plain')
        print('')
        print(e)
        sys.exit(1)

# TODO 与上面的那个函数合并下，减少代码
# 遍历 templates 文件夹的每一个模板
def read_templates_to_list(templates):
    for dirpath, dirnames, filenames in os.walk('templates'):
        for template_file in filenames:
            with open(os.path.join('templates', template_file), 'r') as one_template_file:
                template_set = {}

                for line in one_template_file:
                    if len(line.strip()) and line[0] != '#':   # 如果不是注释行
                        if 'template' not in template_set:
                            template_set['template'] = line
                        elif 'types' not in template_set:
                            template_set['types'] = line
                        else:
                            break

                templates.append(template_set)

def main():
    # 获取 CGI URL 参数，以判断输出 TXT 或者 JSON 版本
    arguments = cgi.FieldStorage()

    # 默认输出 TXT 格式的『名言』。也支持 JSON 格式的输出
    version = arguments.getvalue('v', 'txt')

    # 存放各个参数的词典，比如 args_dict['moods'] 等
    args_dict = {}
    read_lists_to_dict(args_dict)

    # 用来存放模板和参数字典的列表
    templates = []
    read_templates_to_list(templates)

    # 随机决定使用哪个模板
    random_int = randint(0, len(templates)-1)

    # 随机得到 types 指定类别的参数列表
    try:
        args_keys_list = templates[random_int]['types'].split()
        args_list = map(get_random_item, map(args_dict.get, args_keys_list))
    except TypeError as e:
        print('Content-Type: text/plain')
        print('')
        print('有一只模板文件出了问题，请检查 templates 目录下的模板。')
        sys.exit(1)

    # 按照模板生成一句名言
    quote = templates[random_int]['template'] % tuple(args_list)
    quote = quote.strip()

    if version == 'txt':
        print('Content-Type: text/plain')
        print('')
        print(quote)
    elif version == 'json':
        print('Content-Type: application/json')
        print('')
        quote, author = map(str.strip, (quote.split('---')))  # 分开名言和作者。TODO 这里有待改进
        print('{"quote": "' + quote + '", "author": "' + author + '" }')
    else:
        print('Status: 403')    # 参数不对禁止访问哦
        print('')

if __name__ == '__main__':
    main()
