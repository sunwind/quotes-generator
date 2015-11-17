#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cgi
from random import randint
from traverse import *

# enable debugging or not
DEBUG = True

if DEBUG:
    import cgitb; cgitb.enable()


# randomly get an item from a list
def get_random_item(some_list):
    return some_list[randint(0, len(some_list)-1)]


def main():
    # get CGI URL arguments
    arguments = cgi.FieldStorage()

    # output TXT format by default. could change the format by ?v= argument in the URL
    version = arguments.getvalue('v', 'txt')

    # get template id to render. start from 0. specify id by ?t= argument in the URL
    template_id = int(arguments.getvalue('t', -1))

    # the dictionary for different types of lists, such as args_dict['countries'] for the country list
    args_dict = {}
    read_lists_to_dict(args_dict)

    # the list for storing qupte templates
    templates = []
    read_templates_to_list(templates)

    # randomly choose a template id unless previously specified by the ?t= argument
    if template_id < 0 or template_id >= len(templates):
        random_int = randint(0, len(templates)-1)
    else:
        random_int = template_id

    # get a sequence of arguments to complete the chosen template
    try:
        args_keys_list = templates[random_int]['types']
        args_list = map(get_random_item, map(args_dict.get, args_keys_list))
    except TypeError as e:
        print('Content-Type: text/plain')
        print('')
        print('有一只模板文件出了问题，请检查 templates 目录下的模板。')
        
        if DEBUG:
            print(e)

        sys.exit(1)

    # get a quote from the template and arguments generated above
    quote = templates[random_int]['template'] % tuple(args_list)
    quote = quote.strip()

    if version == 'txt':
        print('Content-Type: text/plain')
        print('')
        print(quote)
    elif version == 'json':
        print('Content-Type: application/json')
        print('')
        quote, author = map(str.strip, (quote.split('---')))  # separate the quote and author FIXME: ---
        print('{"quote": "' + quote + '", "author": "' + author + '" }')
    else:
        print('Status: 403')    # return 403 if provided with invalid ?v= argument
        print('')

if __name__ == '__main__':
    main()
