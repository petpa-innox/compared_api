#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 宠物品种识别 Python示例代码
if __name__ == '__main__':
    url = 'https://gwgp-dmgjrjt5y5f.n.bdcloudapi.com/s/api/open/petType'
    params = {}
    params['imageBase64'] = ''
    params['imageUrl'] = ''
    params['petType'] = ''
    params['topK'] = ''
    
    
    headers = {
        
        'Content-Type': 'application/json;charset=UTF-8',
        'X-Bce-Signature': 'AppCode/您的AppCode'
    }
    r = requests.request("POST", url, params=params, headers=headers)
    print(r.content)
