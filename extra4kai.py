import asyncio
import concurrent.futures
import requests
from urllib import request
from urllib import parse
import json
import sys
####
# 初期値設定
####
# APIアクセスキー
keyid     = "7d85b5e681e6566433f7eb5338427fd9"
# メニュー
menu_name = u"ハンバーグ"

menu_name2 = u"ラーメン"

menu_name3 = u"カレー"
#文字コード
encoding = 'utf-8'
url="http://api.gnavi.co.jp/PhotoSearchAPI/20150630/"

url2="http://api.gnavi.co.jp/PhotoSearchAPI/20150630/"

url3="http://api.gnavi.co.jp/PhotoSearchAPI/20150630/"
####
# APIアクセス
####
# URLに続けて入れるパラメータを組立
query = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "menu_name", menu_name.encode(encoding) ),
  ( "hit_per_page" ,3)
]

query2 = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "menu_name", menu_name2.encode(encoding) ),
  ( "hit_per_page" ,3)
]

query3 = [
  ( "format",    "json"    ),
  ( "keyid",     keyid     ),
  ( "menu_name", menu_name3.encode(encoding) ),
  ( "hit_per_page" ,3)
]
url+="?{0}".format(parse.urlencode( query ) )
url2+="?{0}".format(parse.urlencode( query2 ) )
url3+="?{0}".format(parse.urlencode( query3 ) )
####
# 変数の型が文字列かどうかチェック
####
def is_str( data = None ) :
    if isinstance( data, str ) or isinstance( data, unicode ) :
        return True
    else :
        return False


def analysis(data):
    if "error" in data :
        if "message" in data :
            print (u"{0}".format( data["message"] ))
        else :
            print (u"データ取得に失敗しました。")
            sys.exit()

    # ヒット件数取得
    total_hit_count = None
    if "total_hit_count" in data["response"] :
        total_hit_count = data["response"]["total_hit_count"]

    #ページごとの件数を取得
    hit_per_page = None
    if "hit_per_page" in data["response"] :
        hit_per_page = data["response"]["hit_per_page"]
 
    # ヒット件数が0以下、または、ヒット件数がなかったら終了
    if total_hit_count is None or total_hit_count <= 0 or hit_per_page is None or hit_per_page <= 0 :
       print (u"指定した内容ではヒットしませんでした。")
       sys.exit()

    # ヒット件数表示
    print ("{0}件ヒットしました。".format( total_hit_count ))
    print ("----")

    # 出力件数
    disp_count = 0
 
    # 応援口コミデータ取得
    for i in range( hit_per_page ) :
        photo = data["response"]["{0}".format(i)]["photo"]
        line                 = []
        id                   = ""
        name                 = ""
        mname                = ""
        comment              = ""
        shop_url             = ""
 
        # 店舗番号
        if "shop_id" in photo and is_str( photo["shop_id"] ) :
            id = photo["shop_id"]
        line.append( id )
 
        # 店舗名
        if "shop_name" in photo and is_str( photo["shop_name"] ) :
            name = photo["shop_name"]
        line.append( name )
 
        # メニュー名
        if "menu_name" in photo and is_str( photo["menu_name"] ) :
            mname = photo["menu_name"]
        line.append( mname )
 
        # コメント
        if "comment" in photo and is_str( photo["comment"] ) :
            comment = photo["comment"]
        line.append( comment )

        #URL
        if "shop_url"in photo and is_str( photo["shop_url"]):
            shop_url=photo["shop_url"]
        line.append( shop_url)
        # タブ区切りで出力
        print ("\t".join( line ))
        disp_count += 1
 
    # 出力件数を表示して終了
    print ("----")
    print (u"{0}件出力しました。".format( disp_count ))
    sys.exit()
def get_async_iterator(arg_urls):

    class AsyncIterator():

        def __init__(self, urls):
            self.urls = iter(urls)
            self.__loop = None

        async def __aiter__(self):
            self.__loop = asyncio.get_event_loop()
            return self

        async def __anext__(self):
            try:
                u = next(self.urls)
                #u += "?{0}".format(parse.urlencode( query ) )
                future = self.__loop.run_in_executor(None, requests.get, u)
                result=requests.get(u)
                data=json.loads(result.text)
                analysis(data)
                resp = await future
                
            except StopIteration:
                raise StopAsyncIteration
            return resp


    return AsyncIterator(arg_urls)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    async def async_fetch(urls):
        ai = get_async_iterator(urls)
        async for resp in ai:
            print(resp.url)

    loop.run_until_complete(async_fetch([
        url,
        url2,
        url3
    ]))
