#!/usr/bin/env python3

import os

for dirpath, dirnames, filenames in os.walk('.'):
    for each_file in filenames:
        if os.path.splitext(each_file)[1] == ".txt":
            print("Converting " + each_file)
            
            items = ""

            with open(each_file) as f:
                lines = f.readlines()
                lines = [item.strip() for item in lines]
                #items = lines.split()

                items = '"' + ', '.join(lines) + '"'

            with open(os.path.splitext(each_file)[0] + ".py", 'w') as f:
                file_content = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nLIST = " + items + "\n\n"

                other_part = """
# DO NOT EDIT LINES BELOW

if __name__ == '__main__':
    print("This file only contains a list for a template to randomly choose an argument from.\\n"
          "Do not run it directly.\\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    LIST = [item.strip() for item in LIST.split(',')]\n
"""
                
                file_content += other_part
                f.write(file_content)
