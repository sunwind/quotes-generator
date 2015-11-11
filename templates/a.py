#!/usr/bin/env python

TEMPLATE = '%s的本质是一种隐藏的%s。  --- %s著名%s %s %s'
ARGS_TYPE = 'moods moods countries professions first_names last_names'


# DO NOT EDIT LINES BELOW IF NOT NECESSARY

if __name__ == '__main__':
    print("This file only contains a list for a template to randomly choose an argument from.\n"
          "Do not run it directly.\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    ARGS_TYPE = [item.strip() for item in ARGS_TYPE.split(' ')]