# fofa_client
fofa的client代码修改，可以兼容python3.8。代码实现见fofa_client.py


# 示例代码

```python
# -*- coding: utf-8 -*-
import fofa_client as fofa

if __name__ == "__main__":
    email = 'xxx@xxx.com'  # your email
    key = 'xxxxxxxxxxxxxxxxxxx'  # your key
    client = fofa.Client(email, key)
    query_str = 'header="thinkphp" || header="think_template"'
    data = client.get_data(query_str, size=100, page=1, fields="ip,city")
    for ip, city in data["results"]:
        print("%s,%s" % (ip, city))

```
