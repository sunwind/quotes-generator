#!/usr/bin/env python
# -*- coding: utf-8 -*-

TEMPLATE = '我认为 %s 是世界上最好的语言，它的%s让我们的团队%s。 --- %s %s %s %s %s'
ARGS_TYPE = 'languages advantages descriptions companies company_types job_titles first_names last_names'


# DO NOT EDIT LINES BELOW IF NOT NECESSARY

if __name__ == '__main__':
    print("This file only contains a template for generating a kind of quote.\n"
          "Do not run it directly.\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    ARGS_TYPE = [item.strip() for item in ARGS_TYPE.split(' ')]

