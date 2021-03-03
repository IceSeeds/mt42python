from tkinter import StringVar, Variable, ttk
from PIL import Image, ImageTk

class DetailsView():
    def __init__( self ):
        pass

    def base( self, frame, number, symbol, type, lots ):
        #Label
        self.label_order_number_L = ttk.Label( frame )
        self.label_order_number_L.configure( text = "注文番号" )
        self.label_order_number_L.place( x=1, y=0 )
        #Label
        self.label_order_number = ttk.Label( frame )
        self.label_order_number.configure( text = number )
        self.label_order_number.place( x=55, y=0 )
        
        #Label
        self.label_pair_L = ttk.Label( frame )
        self.label_pair_L.configure( text = "通貨ペア" )
        self.label_pair_L.place( x=1, y=20 )
        #Label
        self.label_pair = ttk.Label( frame )
        self.label_pair.configure( text = symbol )
        self.label_pair.place( x=55, y=20 )
        
        #Label
        self.label_ls_L = ttk.Label( frame )
        self.label_ls_L.configure( text = "取引種別" )
        self.label_ls_L.place( x=1, y=40 )
        #Label
        self.label_ls_L = ttk.Label( frame )
        self.label_ls_L.configure( text = type )
        self.label_ls_L.place( x=55, y=40 )

        #Label
        self.label_lots_L = ttk.Label( frame )
        self.label_lots_L.configure( text = " 数  量 " )
        self.label_lots_L.place( x=1, y=60 )
        #Label
        self.label_lots = ttk.Label( frame )
        self.label_lots.configure( text = lots )
        self.label_lots.place( x=55, y=60 )

    def time( self, frame, open_time, close_time, hold_time ):
        #Label
        self.label_open_time_L = ttk.Label( frame )
        self.label_open_time_L.configure( text = "OPEN" )
        self.label_open_time_L.place( x=1, y=0 )
        #Label
        self.label_open_time = ttk.Label( frame )
        self.label_open_time.configure( text = open_time )
        self.label_open_time.place( x=55, y=0 )
        
        #Label
        self.label_close_time_L = ttk.Label( frame )
        self.label_close_time_L.configure( text = "CLOSE" )
        self.label_close_time_L.place( x=1, y=20 )
        #Label
        self.label_close_time = ttk.Label( frame )
        self.label_close_time.configure( text = close_time )
        self.label_close_time.place( x=55, y=20 )

        #Label
        self.label_hold_time_L = ttk.Label( frame )
        self.label_hold_time_L.configure( text = "HOLD" )
        self.label_hold_time_L.place( x=1, y=40 )
        #Label
        self.label_hold_time = ttk.Label( frame )
        self.label_hold_time.configure( text = hold_time )
        self.label_hold_time.place( x=55, y=40 )

    def price( self, frame, open_price, close_price, pips ):
        #Label
        self.label_open_price_L = ttk.Label( frame )
        self.label_open_price_L.configure( text = "OPEN" )
        self.label_open_price_L.place( x=1, y=0 )
        #Label
        self.label_open_price = ttk.Label( frame )
        self.label_open_price.configure( text = open_price )
        self.label_open_price.place( x=55, y=0 )

        #Label
        self.label_close_price_L = ttk.Label( frame )
        self.label_close_price_L.configure( text = "CLOSE" )
        self.label_close_price_L.place( x=1, y=20 )
        #Label
        self.label_close_price = ttk.Label( frame )
        self.label_close_price.configure( text = close_price )
        self.label_close_price.place( x=55, y=20 )

        #Label
        self.label_open_pips_L = ttk.Label( frame )
        self.label_open_pips_L.configure( text = "PIPS" )
        self.label_open_pips_L.place( x=1, y=40 )
        #Label
        self.label_open_pips = ttk.Label( frame )
        self.label_open_pips.configure( text = pips )
        self.label_open_pips.place( x=55, y=40 )

    def image( self, frame ):
        img = "images\imgs.jpg"
        image = Image.open( img )
        self.imgTT = ImageTk.PhotoImage( image )
        #Button
        self.button_image = ttk.Button( frame, width=30 )
        self.button_image.configure( image = self.imgTT )
        self.button_image.place( x=1, y=0 )

    def radio( self, frame ):
        #https://suzutaka-programming.com/tkinter-ttk-radiobutton-value-variable/
        self.radio_item = StringVar()
        self.radio_item.set( "感情" )
        
        #Radiobutton
        self.radio_emotions = ttk.Radiobutton( frame, text="感情", variable=self.radio_item, value="emotions" )
        self.radio_emotions.place( x=1, y=1 )
        #Radiobutton
        self.radio_rule = ttk.Radiobutton( frame, text="ルール", variable=self.radio_item, value="rules" )
        self.radio_rule.place( x=1, y=30 )
    
    def comment( self, frame ):
        #Label
        self.label_comment_1_L = ttk.Label( frame )
        self.label_comment_1_L.configure( text = "感想 1." )
        self.label_comment_1_L.place( x=1, y=0 )
        #Label
        self.label_comment_1 = ttk.Label( frame )
        self.label_comment_1.configure( text = "geeeeeeeeeefsdfe\nefsfdsfesfs\nefsefefsdfedsfe\nsefsf" )
        self.label_comment_1.place( x=55, y=0 )

        #Label
        self.label_comment_2_L = ttk.Label( frame )
        self.label_comment_2_L.configure( text = "感想 2." )
        self.label_comment_2_L.place( x=1, y=100 )
        #Label
        self.label_comment_2 = ttk.Label( frame )
        self.label_comment_2.configure( text = "geeeeeeeeeefsdfe\nefsfdsfesfs\nefsefefsdfedsfe\nsefsf" )
        self.label_comment_2.place( x=55, y=100 )
