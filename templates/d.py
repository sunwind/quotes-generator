#!/usr/bin/env python
# -*- coding: utf-8 -*-

TEMPLATE = '我是%s，真的。 --- %s %s'
ARGS_TYPE = 'animals first_names last_names'


# DO NOT EDIT LINES BELOW IF NOT NECESSARY

if __name__ == '__main__':
    print("This file only contains a template for generating a kind of quote.\n"
          "Do not run it directly.\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    ARGS_TYPE = [item.strip() for item in ARGS_TYPE.split(' ')]

