import tkinter as tk
from tkinter import ttk

class Application( tk.Frame ):
    def __init__( self, master, title="Template", width=300, height=300 ):
        super().__init__( master )
        self.pack()

        self.master.geometry( f"{width}x{height}" )
        self.master.title( title )

        self.create_widgets()

    def create_widgets( self ):
        pass

    def callBack( self ):
        pass

def main():
    root = tk.Tk()
    app = Application( master=root )
    app.mainloop()

if __name__ == "__main__":
    main()
