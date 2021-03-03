from datetime import datetime as dt

import tkinter as tk
from tkinter import StringVar, Variable, ttk
from tkinter.constants import W
from typing import ValuesView
from PIL import Image, ImageTk

from db.db import DBConnect
from gui.edit import DetailsEdit as edit
from gui.view import DetailsView as view

class Details( tk.Frame ):
    def __init__( self, master, data, closed, title="Details", width=900, height=600 ):
        super().__init__( master )
        self.pack()

        self.master.geometry( f"{width}x{height}" )
        self.master.title( title )

        self.db = DBConnect()

        self.view = view()
        self.edit = edit()

        self.data = data
        self.mode = "view"
        self.closed = closed

        self.set_data()

        self.create_widgets()

    def set_data( self ):
        self.db_number   = self.data["1"]
        self.add_time    = self.data["2"]
        self.number      = self.data["3"]
        self.symbol      = self.data["4"]
        self.type        = self.data["5"]
        self.lots        = self.data["6"]
        self.open_time   = self.data["7"]
        self.close_time  = self.data["8"]
        self.open_price  = self.data["9"]
        self.close_price = self.data["10"]
        self.profit      = self.db.get_select( self.number, self.closed, "profit" )[0]
        self.images      = self.db.get_select( self.number, self.closed, "images" )[0]
        self.hold_time   = 0#self.get_hold_time()
        self.pips        = 0#self.get_pips()

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

    def quit_window( self ):
        self.master.destroy()

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

    def create_widgets( self ):
        self.detail()

        if self.mode == "view":
            self.view_all()
        elif self.mode == "edit":
            self.edit_all()
        else:
            print( "None Error in logger an after" )

    def detail( self ):
        #Frame
        self.frame_details = ttk.Frame( self.master, width=900, height=600, relief="groove" )
        self.frame_details.propagate( False )
        self.frame_details.place( x = 0, y = 0 )
        
        #LabelFrame
        self.labelframe_base = ttk.LabelFrame( self.frame_details, text = "base", width=500, height=200 )
        self.labelframe_base.propagate( False )
        self.labelframe_base.place( x=5, y=1 )
        #self.view_base()

        #LabelFrame
        self.labelframe_time = ttk.LabelFrame( self.frame_details, text = "時間", width=500, height=200 )
        self.labelframe_time.propagate( False )
        self.labelframe_time.place( x=200, y=1 )
        #self.view_time()

        #LabelFrame
        self.labelframe_price = ttk.LabelFrame( self.frame_details, text = "価格", width=500, height=200 )
        self.labelframe_price.propagate( False )
        self.labelframe_price.place( x=400, y=1 )
        #self.view_price()

        #LabelFrame
        self.labelframe_image = ttk.LabelFrame( self.frame_details, text = "画像", width=500, height=200 )
        self.labelframe_image.propagate( False )
        self.labelframe_image.place( x=550, y=1 )
        #self.view_image()

        #LabelFrame
        self.labelframe_comment = ttk.LabelFrame( self.frame_details, text = "コメント", width=890, height=250 )
        self.labelframe_comment.propagate( False )
        self.labelframe_comment.place( x=5, y=300 )
        #self.view_comment()

        #LabelFrame
        self.labelframe_radio = ttk.LabelFrame( self.frame_details, text = "radio", width=300, height=100 )
        self.labelframe_radio.propagate( False )
        self.labelframe_radio.place( x=5, y=150 )
        #self.view_radio()

    
    def view_all( self ):
        self.view.base( self.labelframe_base, self.number, self.symbol, self.type, self.lots )
        self.view.time( self.labelframe_time, self.open_time, self.close_time, self.hold_time )
        self.view.price( self.labelframe_price, self.open_price, self.close_price, self.pips )
        self.view.image( self.labelframe_image )
        self.view.radio( self.labelframe_radio )
        self.view.comment( self.labelframe_comment )

    def edit_all( self ):
        pass

"""
#Debug
def main():
    root = tk.Tk()
    app = Details( master=root, data = {} )
    app.mainloop()

if __name__ == "__main__":
    main()
"""

#radiobutton
#感情
#ルール
#集中 ... Concentration コンセントレーション

#label
#良い
#悪い
#改善点