#!/usr/bin/env python

LIST = "苹果, 西瓜, 橘子, 水蜜桃, 香蕉, 橙子, 火龙果, 草莓, 柚子, 荔枝, 甘蔗, 柿子, 甜瓜"


# DO NOT EDIT LINES BELOW

if __name__ == '__main__':
    print("This file only contains a list for a template to randomly choose an argument from.\n"
          "Do not run it directly.\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    LIST = [item.strip() for item in LIST.split(',')]