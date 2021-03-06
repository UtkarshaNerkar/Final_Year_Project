import re
import os
for root, dirs, filenames in os.walk('.',topdown=False):
        for name in filenames:
            if(name.endswith('txt')):
                file_name  = os.path.join(root, name)
                print('\n')
                print(file_name)
                f = open(file_name, 'r')
                content = f.read()
                regexs = [
                          r'Hon\'ble(.*)',
                          r'HONOURABLE(.*)',
                          r'CORAM(.*\n){2}',
                          r'Bench(.*)',
                          r'IN THE COURT OF(.*)',
                          r'Present (.*\n){2}',
                          r'Author(.*)'
                          ]
                for r in regexs:
                    m = re.search(r,content[:3000],re.IGNORECASE)
                    if m:
                        print (m.group().strip())
                        break
                
