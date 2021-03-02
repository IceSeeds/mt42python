import win32pipe
import win32file

from db.main import DBConnect

print("ok@pipe?")

str_pipeName = "KEG_Pipe_Dairy"

# 名前付きパイプの作成
pipe = win32pipe.CreateNamedPipe(
    r'//./pipe/' + str_pipeName,
    win32pipe.PIPE_ACCESS_DUPLEX,
    win32pipe. PIPE_TYPE_BYTE | win32pipe.PIPE_READMODE_BYTE | win32pipe.PIPE_WAIT,
    1, 256, 256, 0, None)

print("ok?")

# クライアントの接続を待つ
win32pipe.ConnectNamedPipe(pipe, None)
print("ok")

result = ""

db = DBConnect()

# 無限ループ
while True:
    # パイプから 1 文字読み取って
    hr, c = win32file.ReadFile(pipe, 1)
    # 表示する
    #print(c.decode(), end='')
    if c.decode() != "@":
        result += c.decode()
    else:
        print( result )
        result_split = result.split( "#" )
        result = ""
        db.add( result_split )
        #for item in result_split:
        #    print( item )


#Tkinter ... GUI
#写真画像をネットに保存？
#日記もネットに保存？読み取り？

#日付、時間なども記録しておいて、カレンダーを作る

#画像アップサイトがあったが、まぁ制約がね。。。
#画像圧縮して、sqlite3に登録しておくって感じにするかも。
#GUIにルール通りできたか？のチェックボックス（予定

#DBの登録は、同じ注文番号があったら、closeTimeが1970じゃなかったら、登録する。 - ok

#-----------------このソフトのいい所--------------------
#DB登録時の実際の価格を取得（周辺）して、それを再現する動画プレイヤー？の画面を作る。
#更には、そのチャートのラインを全て再現する。
#最終的に相互で、読み込みおしたら、MT4からもってくる？


#googleの音声認識を使って、感想などを描く。
