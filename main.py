import tkinter as tk

from gui import keg_main, details
from pipe import pipe_on

def main():
    pipe = pipe_on.Pipe_mt4_2_python()

    while( True ):
        if pipe.connecting():
            data = pipe.roop()
            if data == False:
                continue
            elif data is not None:
                create( data )
                data = None
        else:
            continue

def create( data ):
    root = tk.Tk()
    app  = details.Details( master=root, data=data, closed=data[11], where_view="order", width=1000, height=500 )
    app.mainloop()

def create():
    root = tk.Tk()
    app  = keg_main.Main( master=root, width=1000, height=500 )
    app.mainloop()

if __name__ == "__main__":
    #main()
    create()


#起動したら、guiを表示させて、
#リストを表示か、注文の待機をさせる
