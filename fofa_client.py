'''
Author:Huang YuWen
completed time:2022.05.20 20:30

'''

# -*- coding: utf-8 -*-
import base64
import json
import urllib
import urllib.request
import urllib.parse
import urllib.error


class Client:
    def __init__(self, email, key):
        self.email = email
        self.key = key
        self.base_url = "https://fofa.info"
        self.search_api_url = "/api/v1/search/all?"

    def get_data(self, query_str, page=1, fields="",size=100):
        res = self.get_json_data(query_str, page, fields,size)
        return json.loads(res)

    def get_json_data(self, query_str, page=1, fields="",size=100):
        api_full_url = "%s%s" % (self.base_url, self.search_api_url)
        param = {"email": self.email, "key": self.key, "qbase64": base64.b64encode(query_str.encode()), "page": page,
                 "fields": fields,"size":size}
        res = self.__http_get(api_full_url, param)
        return res

    def __http_get(self, url, param):
        param = urllib.parse.urlencode(param)
        url = "%s%s" % (url, param)
        #print("url=", url)
        try:
            req = urllib.request.Request(url)
            response = urllib.request.urlopen(req)
            html = response.read()
            # print("html:",html)
            # print(type(html))
            if "errmsg".encode() in html:
                print('run errmsg')
                raise RuntimeError(html)
        except urllib.error.HTTPError as e:
            print("errmsg：" + e.read())
            raise e
        return html
