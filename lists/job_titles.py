#!/usr/bin/env python
# -*- coding: utf-8 -*-

LIST = "CEO, 系统架构师, 资深开发工程师, 项目经理, 技术总监, CTO, 总裁"


# DO NOT EDIT LINES BELOW

if __name__ == '__main__':
    print("This file only contains a list for a template to randomly choose an argument from.\n"
          "Do not run it directly.\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    LIST = [item.strip() for item in LIST.split(',')]

