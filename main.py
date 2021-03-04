import tkinter as tk

from gui import keg_main, details
#from pipe.pipe_on import Pipe_mt4_2_python as pipe
from pipe import pipe_on

def main():
    pipe = pipe_on.Pipe_mt4_2_python()

    while( True ):
        if pipe.connecting():
            data = pipe.roop()
            if data is not None:
                create( data )
                data = None
        else:
            continue

def create( data ):
    root = tk.Tk()
    app  = details.Details( master=root, data=data, closed=data[11], where_view="order", width=1000, height=500 )
    app.mainloop()
    

if __name__ == "__main__":
    main()
    """
    root = tk.Tk()
    app  = keg_main.Main( master=root, width=1000, height=500 )
    app.mainloop()
    """
    

"""
   str_result = (string)t_add + SPLITS + 
                (string)i_ticket + SPLITS + 
                str_symbol + SPLITS + 
                str_type + SPLITS + 
                (string)d_lots + SPLITS + 
                (string)t_open + SPLITS + 
                (string)t_close + SPLITS + 
                (string)d_open + SPLITS + 
                (string)d_close + SPLITS + 
                (string)d_profit + SPLITS + 
                g_str_files + SPLITS + 
                b_closed;
"""