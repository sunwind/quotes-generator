#!/usr/bin/env python
#-*- coding: utf-8 -*-

import cgi
from random import randint

# 获取 CGI URL 参数，以判断输出 TXT 或者 JSON 版本
arguments = cgi.FieldStorage()

# 默认输出 TXT 格式的『名言』
version = arguments.getvalue('v', 'txt')

# 从一个  tuple 或者 list 中随机获取一项
def get_random_item(some_list):
	return some_list[randint(0, len(some_list)-1)]

# 从外部文件读取姓名列表。姓名列表来自 https://github.com/dominictarr/random-name
def get_name_list(filename):
	name_list = []
	with open(filename, 'r') as name_file:
		for line in name_file.readlines():
			name_list.append(line.strip())

	return name_list

# 姓名列表
first_names = get_name_list('first_name.txt')
last_names = get_name_list('last_name.txt')

# 各个可选的列表
moods = ('快乐', '悲伤', '兴奋', '愉悦', '失落', '寂寥', '焦躁', '孤独', '孤单', '无力')
countries = ('英国', '法国', '美国', '爱尔兰', '澳大利亚', '加拿大', '德国', '芬兰', '挪威', '新西兰', '瑞士', '意大利')
professions = ('小说家', '作家', '设计师', '画家', '社会学家', '学者', '艺术家')
fruits = ('苹果', '西瓜', '橘子', '水蜜桃', '香蕉', '橙子', '火龙果', '草莓', '柚子', '荔枝', '甘蔗')
languages = ('Java', 'C', 'PHP', 'Go', 'Erlang', 'JavaScript', 'C++', 'Python', 'Ruby', 'C#', 'Objective C', 'Swift', 'Scala')
advantages = ('优雅', '效率', '灵活', '博大精深', '语法', '一切都', '可靠')
companies = ('Ambrella', 'AETex', 'Greenlake', 'FrontAge', 'Clevbit', 'Fantasy')
company_types = ('LLC', 'GmbH', 'Ltd.', 'AG', 'Corp.', 'Inc.')
job_titles = ('CEO', '系统架构师', '资深开发工程师', '项目经理', '技术总监')
descriptions = ('爱不释手', '感到随心所欲', '如虎添翼', '始终保持高效', '披荆斩棘，无所不能')

random_int = randint(0, 2)

if random_int == 0:
	# 生成用于格式化字符串的参数
	args_list = (None, None)

	while args_list[0] == args_list[1] :	# 避免重复生成两个相同的 mood
		# map 的结果是 list (Python 3 下是 map object)，必须转为 tuple 才可以用于格式化字符串
		args_list = tuple(map(get_random_item, (moods, moods, countries, professions, first_names, last_names)))

	# 生成「名言」
	quote = '%s的本质是一种隐藏的%s。  --- %s著名%s %s %s'  % args_list		

elif random_int == 1:
	args_list = tuple(map(get_random_item, (languages, advantages, descriptions, companies, company_types, job_titles, first_names, last_names)))
	quote = '我认为 %s 是世界上最好的语言，它的%s让我们的团队%s。 --- %s %s %s %s %s' % args_list

elif random_int == 2:
	args_list = tuple(map(get_random_item, (fruits, moods, countries, professions, first_names, last_names)))
	quote = '%s是甜的。这是一种让人感到%s的甜。 --- %s著名%s %s %s' % args_list

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
