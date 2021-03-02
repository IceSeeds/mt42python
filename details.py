from datetime import datetime as dt

import tkinter as tk
from tkinter import StringVar, Variable, ttk
from tkinter.constants import W
from typing import ValuesView
from PIL import Image, ImageTk

from db.main import DBConnect

class Detail( tk.Frame ):
    def __init__( self, master, data, title="Details", width=900, height=600 ):
        super().__init__( master )
        self.pack()

        self.master.geometry( f"{width}x{height}" )
        self.master.title( title )

        #self.data = data
        #print( data )
        self.data = (5, '2021.02.26 21:37:21', 91654980, 'USDJPY', 'SELL', 1.0, '2021.02.26 21:30:02', '2021.02.26 21:39:00', 106.900, 106.500, -200, 'img', 'true')
        self.set_data()

        self.create_widgets()



    def set_data( self ):
        self.db_number   = self.data[1]
        self.add_time    = self.data[2]
        self.number      = self.data[3]
        self.symbol      = self.data[4]
        self.type        = self.data[5]
        self.lots        = self.data[6]
        self.open_time   = self.data[7]
        self.close_time  = self.data[8]
        self.open_price  = self.data[9]
        self.close_price = self.data[10]
        self.profit      = self.data[11]
        self.images      = self.data[12]
        #self.closed      = self.data[13]
        self.hold_time   = 0#self.get_hold_time()
        self.pips        = 0#self.get_pips()

    def quit_window( self ):
        self.master.destroy()

    def create_widgets( self ):
        self.detail()

    def detail( self ):
        #Frame
        self.frame_details = ttk.Frame( self.master, width=900, height=600, relief="groove" )
        self.frame_details.propagate( False )
        self.frame_details.place( x = 0, y = 0 )
        
        #LabelFrame
        self.labelframe_base = ttk.LabelFrame( self.frame_details, text = "base", width=500, height=200 )
        self.labelframe_base.propagate( False )
        self.labelframe_base.place( x=5, y=1 )
        self.view_base()

        #LabelFrame
        self.labelframe_time = ttk.LabelFrame( self.frame_details, text = "時間", width=500, height=200 )
        self.labelframe_time.propagate( False )
        self.labelframe_time.place( x=200, y=1 )
        self.view_time()

        #LabelFrame
        self.labelframe_price = ttk.LabelFrame( self.frame_details, text = "価格", width=500, height=200 )
        self.labelframe_price.propagate( False )
        self.labelframe_price.place( x=400, y=1 )
        self.view_price()

        #LabelFrame
        self.labelframe_image = ttk.LabelFrame( self.frame_details, text = "画像", width=500, height=200 )
        self.labelframe_image.propagate( False )
        self.labelframe_image.place( x=550, y=1 )
        self.view_image()

        #LabelFrame
        self.labelframe_comment = ttk.LabelFrame( self.frame_details, text = "コメント", width=890, height=250 )
        self.labelframe_comment.propagate( False )
        self.labelframe_comment.place( x=5, y=300 )
        self.view_comment()

        #LabelFrame
        self.labelframe_radio = ttk.LabelFrame( self.frame_details, text = "radio", width=300, height=100 )
        self.labelframe_radio.propagate( False )
        self.labelframe_radio.place( x=5, y=150 )
        #self.view_radio()
        self.view_spin()

        self.command_button()
        #print( self.data )
    
    def command_button( self ):
        self.menubar = tk.Menu( self.master )
        self.master.config( menu=self.menubar )

        # menubarを親として設定メニューを作成と表示
        self.setting_menu = tk.Menu( self.menubar, tearoff=0 )
        self.menubar.add_cascade( label='設定', menu=self.setting_menu )

        # menubarを親としてヘルプメニューを作成と表示
        help_menu = tk.Menu( self.menubar, tearoff=0 )
        self.menubar.add_cascade( label='ヘルプ', menu=help_menu )
        # 設定メニューにプルダウンメニューを追加
        self.setting_menu.add_command( label='編集', command=self.edit_all )
        self.setting_menu.add_command( label='画像の表示' )
        self.setting_menu.add_separator()
        self.setting_menu.add_command( label='終了' )

    def edit_all( self ):
        print( "comming sooon" )
    
    def view_spin( self ):
        val = StringVar()
        val.set('0')
        self.radio1 = ttk.Spinbox( self.labelframe_radio, format="%d",textvariable=val, from_=0, increment=1 )
        self.radio1.pack()
        self.radio2 = ttk.Spinbox( self.labelframe_radio, format="%d",textvariable=val, from_=0, increment=1 )
        self.radio2.pack()
        self.radio3 = ttk.Spinbox( self.labelframe_radio, format="%d",textvariable=val, from_=0, increment=1 )
        self.radio3.pack()
    def view_radio( self ):
        #https://suzutaka-programming.com/tkinter-ttk-radiobutton-value-variable/
        self.radio_item = StringVar()
        self.radio_item.set( "感情" )
        
        #Radiobutton
        self.radio_emotions = ttk.Radiobutton( self.labelframe_radio, text="感情", variable=self.radio_item, value="emotions" )
        self.radio_emotions.place( x=1, y=1 )
        #Radiobutton
        self.radio_rule = ttk.Radiobutton( self.labelframe_radio, text="ルール", variable=self.radio_item, value="rules" )
        self.radio_rule.place( x=1, y=30 )

    def send_comment_DB( self ):
        sendDB = []
        
        com1 = self.text_comment_1.get( 1.0, tk.END+"-1c" )
        com2 = self.text_comment_2.get( 1.0, tk.END+"-1c" )
        sendDB.append( com1 )
        sendDB.append( com2 )
        self.text_comment_1.delete( 1.0, tk.END )
        self.text_comment_2.delete( 1.0, tk.END )
        #print( com1 )
        db = DBConnect()
        db.com_add( sendDB )

    def view_comment( self ):
        self.text_comment_1 = tk.Text( self. labelframe_comment, width=50 )
        self.text_comment_1.place( x=1, y=0 )
        self.text_comment_2 = tk.Text( self. labelframe_comment, width=50 )
        self.text_comment_2.place( x=500, y=0 )

        self.button_comment_send = ttk.Button( self.labelframe_comment, command=self.send_comment_DB )
        self.button_comment_send.place( x = 1, y = 200 )
    
        """
        #Label
        self.label_comment_1_L = ttk.Label( self.labelframe_comment )
        self.label_comment_1_L.configure( text = "感想 1." )
        self.label_comment_1_L.place( x=1, y=0 )
        #Label
        self.label_comment_1 = ttk.Label( self.labelframe_comment )
        self.label_comment_1.configure( text = "geeeeeeeeeefsdfe\nefsfdsfesfs\nefsefefsdfedsfe\nsefsf" )
        self.label_comment_1.place( x=55, y=0 )

        #Label
        self.label_comment_2_L = ttk.Label( self.labelframe_comment )
        self.label_comment_2_L.configure( text = "感想 2." )
        self.label_comment_2_L.place( x=1, y=100 )
        #Label
        self.label_comment_2 = ttk.Label( self.labelframe_comment )
        self.label_comment_2.configure( text = "geeeeeeeeeefsdfe\nefsfdsfesfs\nefsefefsdfedsfe\nsefsf" )
        self.label_comment_2.place( x=55, y=100 )
        """
    def view_image( self ):
        img = "images\imgs.jpg"
        image = Image.open( img )
        self.imgTT = ImageTk.PhotoImage( image )
        #Button
        self.button_image = ttk.Button( self.labelframe_image, width=30 )
        self.button_image.configure( image = self.imgTT )
        self.button_image.place( x=1, y=0 )

    def view_time( self ):
        #Label
        self.label_open_time_L = ttk.Label( self.labelframe_time )
        self.label_open_time_L.configure( text = "OPEN" )
        self.label_open_time_L.place( x=1, y=0 )
        #Label
        self.label_open_time = ttk.Label( self.labelframe_time )
        self.label_open_time.configure( text = self.open_time )
        self.label_open_time.place( x=55, y=0 )
        
        #Label
        self.label_close_time_L = ttk.Label( self.labelframe_time )
        self.label_close_time_L.configure( text = "CLOSE" )
        self.label_close_time_L.place( x=1, y=20 )
        #Label
        self.label_close_time = ttk.Label( self.labelframe_time )
        self.label_close_time.configure( text = self.close_time )
        self.label_close_time.place( x=55, y=20 )

        #Label
        self.label_hold_time_L = ttk.Label( self.labelframe_time )
        self.label_hold_time_L.configure( text = "HOLD" )
        self.label_hold_time_L.place( x=1, y=40 )
        #Label
        self.label_hold_time = ttk.Label( self.labelframe_time )
        self.label_hold_time.configure( text = self.hold_time )
        self.label_hold_time.place( x=55, y=40 )
    
    def view_price( self ):
        #Label
        self.label_open_price_L = ttk.Label( self.labelframe_price )
        self.label_open_price_L.configure( text = "OPEN" )
        self.label_open_price_L.place( x=1, y=0 )
        #Label
        self.label_open_price = ttk.Label( self.labelframe_price )
        self.label_open_price.configure( text = self.open_price )
        self.label_open_price.place( x=55, y=0 )

        #Label
        self.label_close_price_L = ttk.Label( self.labelframe_price )
        self.label_close_price_L.configure( text = "CLOSE" )
        self.label_close_price_L.place( x=1, y=20 )
        #Label
        self.label_close_price = ttk.Label( self.labelframe_price )
        self.label_close_price.configure( text = self.close_price )
        self.label_close_price.place( x=55, y=20 )

        #Label
        self.label_open_pips_L = ttk.Label( self.labelframe_price )
        self.label_open_pips_L.configure( text = "PIPS" )
        self.label_open_pips_L.place( x=1, y=40 )
        #Label
        self.label_open_pips = ttk.Label( self.labelframe_price )
        self.label_open_pips.configure( text = self.pips )
        self.label_open_pips.place( x=55, y=40 )

    def view_base( self ):
        #Label
        self.label_order_number_L = ttk.Label( self.labelframe_base )
        self.label_order_number_L.configure( text = "注文番号" )
        self.label_order_number_L.place( x=1, y=0 )
        #Label
        self.label_order_number = ttk.Label( self.labelframe_base )
        self.label_order_number.configure( text = self.number )
        self.label_order_number.place( x=55, y=0 )
        
        #Label
        self.label_pair_L = ttk.Label( self.labelframe_base )
        self.label_pair_L.configure( text = "通貨ペア" )
        self.label_pair_L.place( x=1, y=20 )
        #Label
        self.label_pair = ttk.Label( self.labelframe_base )
        self.label_pair.configure( text = self.symbol )
        self.label_pair.place( x=55, y=20 )
        
        #Label
        self.label_ls_L = ttk.Label( self.labelframe_base )
        self.label_ls_L.configure( text = "取引種別" )
        self.label_ls_L.place( x=1, y=40 )
        #Label
        self.label_ls_L = ttk.Label( self.labelframe_base )
        self.label_ls_L.configure( text = self.type )
        self.label_ls_L.place( x=55, y=40 )

        #Label
        self.label_lots_L = ttk.Label( self.labelframe_base )
        self.label_lots_L.configure( text = " 数  量 " )
        self.label_lots_L.place( x=1, y=60 )
        #Label
        self.label_lots = ttk.Label( self.labelframe_base )
        self.label_lots.configure( text = self.lots )
        self.label_lots.place( x=55, y=60 )

    def get_hold_time( self ):
        open  = dt.strptime( self.open_time,  '%Y.%m.%d %H:%M:%S' )
        close = dt.strptime( self.close_time, '%Y.%m.%d %H:%M:%S' )
        time = close - open
        #print( time )
        return time

    def get_pips( self ):
        price = 0
        if self.type == "SELL":
            price = self.open_price - self.close_price
        else:
            price = self.close_price - self.open_price
        
        price = round( price, 3 ) * 100
        return price

#Debug
def main():
    root = tk.Tk()
    app = Detail( master=root, data = {} )
    app.mainloop()

if __name__ == "__main__":
    main()


#radiobutton
#感情
#ルール
#集中 ... Concentration コンセントレーション

#label
#良い
#悪い
#改善点