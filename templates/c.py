#!/usr/bin/env python
# -*- coding: utf-8 -*-

TEMPLATE = '%s 语言就像%s一样，需要细细品味，%s充分体会它那愈久弥深的%s。 --- %s 公司 %s : %s %s'
ARGS_TYPE = 'languages fruits still advantages companies job_titles first_names last_names'


# DO NOT EDIT LINES BELOW IF NOT NECESSARY

if __name__ == '__main__':
    print("This file only contains a template for generating a kind of quote.\n"
          "Do not run it directly.\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    ARGS_TYPE = [item.strip() for item in ARGS_TYPE.split(' ')]

