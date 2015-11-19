import sys
import os


# traverse the "lists" folder to automatically read all lists available
def read_lists_to_dict(args_dict):
    sys.path.append("lists")

    for dirpath, dirnames, filenames in os.walk('lists'):
        for some_list_file in filenames:
            module_name = os.path.splitext(some_list_file)[0]

            if module_name[0] == "_":  # ignore __init__.py or other files that are not meant to load
                continue
            
            try:
                args_dict[module_name] = __import__(module_name).LIST
            except ImportError:   # ignore modules that cannot be imported
                pass

    sys.path.pop()


# traverse the "templates" folder to automatically read all templates available
def read_templates_to_list(templates):
    sys.path.append("templates")

    for dirpath, dirnames, filenames in os.walk('templates'):
        for template_file in filenames:
            module_name = os.path.splitext(template_file)[0]

            if module_name[0] == "_":  # ignore __init__.py or other files that are not meant to load
                continue

            try:
                template_set = dict()

                template_set['template'] = __import__(module_name).TEMPLATE
                template_set['types'] = __import__(module_name).ARGS_TYPE

                templates.append(template_set)
            except ImportError:  # ignore modules that cannot be imported
                pass

    sys.path.pop()
