import re

print(re.findall(r'www\.\w+\.\w{3}\.\w{2}(/\w+)?|\w+\.\w{3}\.\w{2}(/\w+)?', 'multivix.edu.br/ead'))