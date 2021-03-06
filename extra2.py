#!/usr/bin/env python
# -*- coding: utf-8 -*-
#*****************************************************************************************
# ぐるなびWebサービスのレストラン検索APIで緯度経度検索を実行しパースするプログラム
# 注意：ここでは緯度と経度の値は固定でいれています。
# 　　　APIアクセスキーの値にはユーザ登録で取得したものを入れてください。
#*****************************************************************************************
import sys
import urllib
import json
import unicodedata
 
####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
  if isinstance( data, str ) or isinstance( data, unicode ) :
    return True
  else :
    return False
 
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

####
# 初期値設定
####
# APIアクセスキー
keyid     = "7d85b5e681e6566433f7eb5338427fd9"
# エンドポイントURL
if(japan):
	url       = "http://api.gnavi.co.jp/RestSearchAPI/20150630/"

	# 緯度・経度、範囲を変数に入れる
	# 緯度経度は日本測地系で日比谷シャンテのもの。範囲はrange=1で300m以内を指定している。
	# 緯度
	latitude  = "35.670083"
	# 経度
	longitude = "139.763267"
	# 範囲
	range     = "1"
		 
	####
	# APIアクセス
	####
	# URLに続けて入れるパラメータを組立
	query = [
	( "format",    "json"    ),
	( "keyid",     keyid     ),
	( "latitude",  latitude  ),
	( "longitude", longitude ),
	( "range",     range     ),
	( "freeword", sys.argv[1] ),
	]

	# URL生成
	url += "?{0}".format( urllib.urlencode( query ) )
	# API実行
	try :
	  result = urllib.urlopen( url ).read()
	except ValueError :
	  print u"APIアクセスに失敗しました。"
	  sys.exit()
		 
	####
	# 取得した結果を解析
	####
	data = json.loads( result )
	 
	# エラーの場合
	if "error" in data :
	  if "message" in data :
		print u"{0}".format( data["message"] )
	  else :
		print u"データ取得に失敗しました。"
	  sys.exit()
		 
	# ヒット件数取得
	total_hit_count = None
	if "total_hit_count" in data :
	  total_hit_count = data["total_hit_count"]
		 
	# ヒット件数が0以下、または、ヒット件数がなかったら終了
	if total_hit_count is None or total_hit_count <= 0 :
	  print u"指定した内容ではヒットしませんでした。"
	  sys.exit()
		 
	# レストランデータがなかったら終了
	if not "rest" in data :
	  print u"レストランデータが見つからなかったため終了します。"
	  sys.exit()
		 
	# ヒット件数表示
	print "{0}件ヒットしました。".format( total_hit_count )
	print "----"
		 
	# 出力件数
	disp_count = 0
		 
	# レストランデータ取得
	for rest in data["rest"]:
	  line                 = []
	  id                   = ""
	  name                 = ""
	  access_line          = ""
	  access_station       = ""
	  access_walk          = ""
	  code_category_name_s = []
	  # 店舗番号
	  if "id" in rest and is_str( rest["id"] ) :
		id = rest["id"]
	  line.append( id )
	  # 店舗名
	  if "name" in rest and is_str( rest["name"] ) :
		name = u"{0}".format( rest["name"] )
	  line.append( name )
	  if "access" in rest :
		access = rest["access"]
		# 最寄の路線
		if "line" in access and is_str( access["line"] ) :
		  access_line = u"{0}".format( access["line"] )
		# 最寄の駅
		if "station" in access and is_str( access["station"] ) :
		  access_station = u"{0}".format( access["station"] )
		# 最寄駅から店までの時間
		if "walk"    in access and is_str( access["walk"] ) :
		  access_walk = u"{0}分".format( access["walk"] )
	  line.extend( [ access_line, access_station, access_walk ] )
	  # 店舗の小業態
	  if "code" in rest and "category_name_s" in rest["code"] :
		for category_name_s in rest["code"]["category_name_s"] :
		  if is_str( category_name_s ) :
			code_category_name_s.append( u"{0}".format( category_name_s ) )
	  line.extend( code_category_name_s )
	  # タブ区切りで出力
	  print "\t".join( line )
	  disp_count += 1
		 
	# 出力件数を表示して終了
	print "----"
	print u"{0}件出力しました。".format( disp_count )
	sys.exit()

if(english):
	# エンドポイントURL
	url       = "http://api.gnavi.co.jp/ForeignRestSearchAPI/20150630/"
	# 緯度・経度、範囲を変数に入れる
	# 緯度経度は日本測地系で日比谷シャンテのもの。範囲はrange=1で300m以内を指定している。
	# 緯度
	latitude  = "35.670083"
	# 経度
	longitude = "139.763267"
	# 範囲
	range     = "1"
 
	####
	# APIアクセス
	####
	# URLに続けて入れるパラメータを組立
	query = [
	( "format",    "json"    ),
	( "keyid",     keyid     ),
	( "lang",      "en"      ),
	( "latitude",  latitude  ),
	( "longitude", longitude ),
	( "range",     range     ),
	( "freeword", sys.argv[1] ),
	]
	# URL生成
	url += "?{0}".format( urllib.urlencode( query ) )
	# API実行
	try :
	  result = urllib.urlopen( url ).read()
	except ValueError :
	  print u"APIアクセスに失敗しました。"
	  sys.exit()
 
	####
	# 取得した結果を解析
	####
	data = json.loads( result )
 
	# エラーの場合
	if "error" in data :
	  if "message" in data :
	    print u"{0}".format( data["message"] )
	  else :
	    print u"データ取得に失敗しました。"
	  sys.exit()
 
	# ヒット件数取得
	total_hit_count = None
	if "total_hit_count" in data :
	  total_hit_count = data["total_hit_count"]
 
	# ヒット件数が0以下、または、ヒット件数がなかったら終了
	if total_hit_count is None or total_hit_count <= 0 :
	  print u"指定した内容ではヒットしませんでした。"
	  sys.exit()
 
	# レストランデータがなかったら終了
	if not "rest" in data :
	  print u"レストランデータが見つからなかったため終了します。"
	  sys.exit()
	 
	# ヒット件数表示
	print "{0}件ヒットしました。".format( total_hit_count )
	print "----"
	 
	# 出力件数
	disp_count = 0
	 
	# レストランデータ取得
	for rest in data["rest"] :
	  line                 = []
	  id                   = ""
	  name                 = ""
	  access               = ""
	 
	  # 店舗番号
	  if "id" in rest and is_str( rest["id"] ) :
	    id = rest["id"]
	  line.append( id )
 
	  if "name" in rest :
	    name = rest["name"]
	    # 最寄の路線
	    if "name" in name and is_str( name["name"] ) :
	      name = u"{0}".format( name["name"] )
	    line.append( name )
	  #　アクセス情報
	  if "access" in rest and is_str( rest["access"] ) :
	    access = u"{0}".format( rest["access"] )
	  line.append( access )
	 
	  # タブ区切りで出力
	  print "\t".join( line )
	  disp_count += 1
	 
	# 出力件数を表示して終了
	print "----"
	print u"{0}件出力しました。".format( disp_count )
	sys.exit()
		
