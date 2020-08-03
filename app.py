import sys
import math
import requests

print(sys.implementation)
r = requests.get('http://google.com')

print(r.status_code)
print(2 * math.pi)
