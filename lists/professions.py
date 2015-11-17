#!/usr/bin/env python
# -*- coding: utf-8 -*-

LIST = "小说家, 作家, 设计师, 画家, 社会学家, 学者, 艺术家"


# DO NOT EDIT LINES BELOW

if __name__ == '__main__':
    print("This file only contains a list for a template to randomly choose an argument from.\n"
          "Do not run it directly.\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    LIST = [item.strip() for item in LIST.split(',')]

