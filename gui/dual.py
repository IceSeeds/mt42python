from os import close
import tkinter as tk
from tkinter import ttk

from gui.details import Detail
from db.db import DBConnect

class Main( tk.Frame ):
    def __init__( self, master, title="Template", width=500, height=500 ):
        super().__init__( master )
        self.pack()

        self.master.geometry( f"{width}x{height}" )
        self.master.title( title )

        self.db = DBConnect()

        self.create_widgets()

    def create_widgets( self ):
        self.left()
        self.right()


    def left( self ):
        #Frame
        self.frame_button = ttk.Frame( width=100, height=500, relief="groove" )
        self.frame_button.propagate( False )
        self.frame_button.place( x = 0, y = 0 )
        
        #Button
        self.button_list = ttk.Button( self.frame_button, text="list", width=50, command=self.right )
        self.button_list.pack()
        #Button
        self.button_first = ttk.Button( self.frame_button, text="oepn", width=50, command=self.on_button_open )
        self.button_first.pack()
        #Button
        self.button_way = ttk.Button( self.frame_button, text="途中", width=50 )
        self.button_way.pack()
        #Button
        self.button_end = ttk.Button( self.frame_button, text="close", width=50, command=self.on_button_close )
        self.button_end.pack()
        #Button
        self.button_new = ttk.Button( self.frame_button, text="新規作成", width=50 )
        self.button_new.pack()
        #Button
        self.button_serch = ttk.Button( self.frame_button, text="検索", width=50 )
        self.button_serch.pack()
        #Button
        self.button_cure = ttk.Button( self.frame_button, text="かれんだー", width=50 )
        self.button_cure.pack()

    def right( self ):
        #Frame
        self.frame_list = ttk.Frame( width=900, height=600, relief="groove" )
        self.frame_list.propagate( False )
        self.frame_list.place( x = 100, y = 0 )

        self.tree = ttk.Treeview( self.frame_list )
        self.tree_init()
        self.tree_update( mode="all" )

    def on_button_open( self ):
        #Frame
        self.frame_open = ttk.Frame( width=900, height=600, relief="groove" )
        self.frame_open.propagate( False )
        self.frame_open.place( x = 100, y = 0 )

        self.tree = ttk.Treeview( self.frame_open )
        self.tree_init()
        self.tree_update( mode="false" )
    
    def on_button_close( self ):
        #Frame
        self.frame_close = ttk.Frame( width=900, height=600, relief="groove" )
        self.frame_close.propagate( False )
        self.frame_close.place( x = 100, y = 0 )

        self.tree = ttk.Treeview( self.frame_close )
        self.tree_init()
        self.tree_update( mode="true" )
        

    def tree_update( self, mode ):
        result = self.db.get( closed = mode )
        for item in result:
            self.add_tree( item )
            #print( item )
        
    def add_tree( self, item ):
        self.tree.insert( "", "end", values = item )

    def on_tree_select( self, event ):
        data = {}
        for id in self.tree.selection():
            data = self.tree.set( id )
        self.new_window( data )

    def tree_init( self ):
        # 列を作成（３列）
        self.tree["columns"] = ( 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 )
        # ヘッダーの設定
        self.tree["show"] = "headings"
        self.tree.heading( 1,  text = "No." )
        self.tree.heading( 2,  text = "AddTime." )
        self.tree.heading( 3,  text = "Number" )
        self.tree.heading( 4,  text = "Symbol" )
        self.tree.heading( 5,  text = "Type" )
        self.tree.heading( 6,  text = "Lots" )
        self.tree.heading( 7,  text = "OpenTime" )
        self.tree.heading( 8,  text = "CloseTime" )
        self.tree.heading( 9,  text = "OpenPrice" )
        self.tree.heading( 10, text = "ClosePrice" )
        # 各列の幅設定
        self.tree.column( 1,  width = 30 )
        self.tree.column( 2,  width = 130 )
        self.tree.column( 3,  width = 70 )
        self.tree.column( 4,  width = 70 )
        self.tree.column( 5,  width = 50 )
        self.tree.column( 6,  width = 50 )
        self.tree.column( 7,  width = 130 )
        self.tree.column( 8,  width = 130 )
        self.tree.column( 9,  width = 80 )
        self.tree.column( 10, width = 80 )
        # データ挿入
        #self.add_tree( "91539611", "USDJPY", "0.1" )
        # 表の配置
        self.tree.place( x = 0, y = 0 )
        #上の関数を呼び出すための設定
        self.tree.bind( "<<TreeviewSelect>>", self.on_tree_select )

    def new_window( self, data ):
        self.newWindow = tk.Toplevel( self.master )
        self.app2 = Detail( self.newWindow, data )

"""
def main():
    root = tk.Tk()
    app = Main( master=root, width=1000, height=500 )
    app.mainloop()

if __name__ == "__main__":
    main()
"""