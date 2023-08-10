#!/usr/bin/python3
# -*- coding: utf-8 -*-
import datetime
from string import Template

# 現在時刻を文字列で取得
nowDate = datetime.datetime.now().strftime('%Y年%m月%d日');

# html を読み込み テンプレート文字列 にする
file = open('./testy.html', 'r', encoding="utf-8")
rowData = file.read()
data = Template(rowData)
file.close()

# HTML用のヘッダー情報とページの内容を出力
print('Content-type: text/html\n')
print(data.substitute(now=nowDate))