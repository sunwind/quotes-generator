#!/usr/bin/env python3

import os

for dirpath, dirnames, filenames in os.walk('.'):
    for each_file in filenames:
        if os.path.splitext(each_file)[1] == ".txt":
            print("Converting " + each_file)
            
            items = []

            with open(each_file) as f:
                lines = f.readlines()
                lines = [item.strip() for item in lines if item[0] != '#' and item.strip()]
                #items = lines.split()

                items = lines

            with open(os.path.splitext(each_file)[0] + ".py", 'w') as f:
                file_content = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\n\nTEMPLATE = '" + lines[0] + "'\nARGS_TYPE = '" + lines[1] + "'\n\n"

                other_part = """
# DO NOT EDIT LINES BELOW IF NOT NECESSARY

if __name__ == '__main__':
    print("This file only contains a template for generating a kind of quote.\\n"
          "Do not run it directly.\\n"
          "Otherwise you may risk letting the cat out of the bag.")
else:
    ARGS_TYPE = [item.strip() for item in ARGS_TYPE.split(' ')]

"""
                
                file_content += other_part

                f.write(file_content)
