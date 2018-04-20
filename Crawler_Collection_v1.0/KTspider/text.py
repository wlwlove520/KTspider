import requests
res = requests.get('http://www.zp798.com/index.php?c=content&a=list&catid=1')
print(res.headers)