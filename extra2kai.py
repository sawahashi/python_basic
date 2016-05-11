#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import unicodedata
#import japanrestaurant
#import englishrestaurant

#コマンドライン引数
argv=sys.argv
argc=len(argv)
if(argc!=2):
    print 'Usage pyton %s word' %argv[0]
    quit()
#言語判定
japan=0
english=0
uni=unicode(argv[1],'utf-8')
for i in uni:
	name=unicodedata.name(i)
	if("CJK UNIFIED" in name or "HIRAGANA" in name or "KATAKANA" in name):
		japan=1

if(japan==0):
	english=1

if(japan):
	import japanrestaurant
if(english):
	import englishrestaurant
