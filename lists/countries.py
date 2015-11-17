#!/usr/bin/env python
# -*- coding: utf-8 -*-

LIST = "英国, 法国, 美国, 爱尔兰, 澳大利亚, 加拿大, 德国, 芬兰, 挪威, 新西兰, 瑞士, 意大利, 瑞典, 荷兰, 克罗地亚"


# DO NOT EDIT LINES BELOW

if __name__ == '__main__':
    print("This file only contains a list for a template to randomly choose an argument from.\n"
          "Do not run it directly.\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    LIST = [item.strip() for item in LIST.split(',')]

