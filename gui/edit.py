import tkinter as tk
from tkinter import StringVar, Variable, ttk

from db.db import DBConnect

class DetailsEdit():
    def __init__( self ):
        self.db = DBConnect

    def base( self, frame ):
        pass
    def time( self, frame ):
        pass
    def price( self, frame ):
        pass
    def image( self, frame ):
        pass
    def radio( self, frame ):
        pass
    
    def comment( self, frame ):
        #ttk.Scrollbar( 盾にスクロールするように
        self.text_comment_1 = tk.Text( frame, width=35 )
        self.text_comment_1.place( x=40, y=10 )
        self.text_comment_2 = tk.Text( frame, width=35 )
        self.text_comment_2.place( x=300, y=10 )
        self.text_comment_3 = tk.Text( frame, width=35 )
        self.text_comment_3.place( x=560, y=10 )
    
    def send( self, frame ):
        self.button_send = ttk.Button( frame, text="適用", command=self.press )
        self.button_send.pack()

    def press( self ):
        #self.db.add_comment( data )
        pass
