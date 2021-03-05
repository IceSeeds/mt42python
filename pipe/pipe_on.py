import win32pipe
import win32file

from db.db import DBConnect

class Pipe_mt4_2_python():
    def __init__( self ):
        print( "__init__" )
        self.pipe_name = "KEG_Pipe_Dairy"
        ## 名前付きパイプの作成
        self.pipe = win32pipe.CreateNamedPipe(
            r'//./pipe/' + self.pipe_name,
            win32pipe.PIPE_ACCESS_DUPLEX,
            win32pipe. PIPE_TYPE_BYTE | win32pipe.PIPE_READMODE_BYTE | win32pipe.PIPE_WAIT,
            1, 256, 256, 0, None)
        
        self.db = DBConnect()

    def connecting( self ):
        print( "connecting..." )
        # クライアントの接続を待つ
        win32pipe.ConnectNamedPipe( self.pipe, None )
        print( "connect complete!!" )
        return True

    def roop( self ):
        result = ""
        while True:
            # パイプから 1 文字読み取って
            hr, c = win32file.ReadFile( self.pipe, 1 )
            # 表示する
            if c.decode() != "@":
                result += c.decode()
            else:
                print( result )
                result_split = result.split( "#" )
                result = ""
                if self.db.add( result_split ) == False:
                    return False

                return result_split


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
