#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
現在の日時を表示する
'''

html = '''Content-Type: text/html

<html>
<head>
  <title>現在の日時を表示する</title>
</head>
<body>
<h1>現在の日時を表示する</h1>
<p>現在の日時は、「%s」です。</p>
</body>
</html>
'''

import time
now = time.strftime('%Y年%m月%d日 %H時%M分%S秒')
print ( html % now)
