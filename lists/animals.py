#!/usr/bin/env python
# -*- coding: utf-8 -*-

LIST = "猫, 一只猫, 两只猫, 三只猫"


# DO NOT EDIT LINES BELOW

if __name__ == '__main__':
    print("This file only contains a list for a template to randomly choose an argument from.\n"
          "Do not run it directly.\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    LIST = [item.strip() for item in LIST.split(',')]

