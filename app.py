import sys

import requests

print(sys.executable)
r = requests.get('http://google.com')
print(r.status_code)
