import tkinter as tk

from gui import keg_main, details
from pipe import pipe_on


def main():
    root = tk.Tk()
    app  = keg_main.Main( master=root, width=1000, height=500 )
    app.mainloop()

if __name__ == "__main__":
    main()
