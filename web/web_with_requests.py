"""
Quick offline reference for web requests in Python
"""

import requests
import json

payload = {'test1': 'val1', 'test2': 'val2'}
custom_headers = {'user-agent': 'james-bond'}

# Testing GET requests
get = requests.get(
    'http://httpbin.org/get', params=payload, headers=custom_headers
    )

print('\n' + 'GET request testing' + '\n')
print('URL: ' + get.url)
print('Status code: ' + str(get.status_code))
print('Headers: ' + str(get.headers) + '\n')
print('Returned JSON: ')
print(get.json())
print()

# Testing POST requests
post = requests.post(
    'http://httpbin.org/post', data=json.dumps(payload), headers=custom_headers
    )

print('\n' + 'POST request testing' + '\n')
print(post.text)
print()

# Testing cookies
cookies = dict(cookies_are='working')
cookies_request = requests.get('http://httpbin.org/cookies', cookies=cookies)
print('\n' + 'Cookie testing' + '\n')
print(cookies_request.text)
print()

# Testing redirects
redirect = requests.get('http://github.com', allow_redirects=True)
print('\n' + 'Redirect testing' + '\n')
print('Status code: ' + str(redirect.status_code))
print('Redirect history: ')
print(redirect.history)
print()

# Testing timeouts
print('\n' + 'Timeout testing' + '\n')
try:
    timeout = requests.get('http://github.com', timeout=0.002)
except requests.exceptions.ConnectTimeout:
    print('Timeout triggered correctly.')
print()