from tkinter import *
import tkinter
import tkinter.ttk as ttk

#tkinter初期
root = tkinter.Tk()
root.title( u"MT4_to_Dairy" )
root.geometry( "800x500" )

#LEFT
frame_button = tkinter.Frame( root, bg='LightSkyBlue' )

#Button
button_list = Button( frame_button, text = "一覧", width = 20 )
button_list.pack()
#Button
button_new = Button( frame_button, text = "新規作成", width = 20 )
button_new.pack()
#Button
button_first = Button( frame_button, text = "初め", width = 20 )
button_first.pack()
#Button
button_way = Button( frame_button, text = "途中", width = 20 )
button_way.pack()
#Button
button_end = Button( frame_button, text = "終わり", width = 20 )
button_end.pack()
#Button
button_serch = Button( frame_button, text = "検索", width = 20 )
button_serch.pack()
#Button
button_cure = Button( frame_button, text = "カレンダー", width = 20 )
button_cure.pack()


#Label
#title = Label( frame_list, text = u"Title" )
#title.pack()


#RIGHT
frame_list = tkinter.Frame( root, bg="blue" )

#Treeview
tree = ttk.Treeview( frame_list )
# 列を作成（３列）
tree["columns"] = (1,2,3)
# ヘッダーの設定
tree["show"] = "headings"
tree.heading(1,text="注文番号")
tree.heading(2,text="通貨")
tree.heading(3,text="数量")
# 各列の幅設定
tree.column(1,width=100)
tree.column(2,width=100)
tree.column(3,width=50)
# データ挿入
tree.insert("", "end", values=("91539611", "USDJPY", "0.1"))
tree.insert("", "end", values=("91539622", "USDJPY", "0.1"))
tree.insert("", "end", values=("91539633", "USDJPY", "0.1"))
# 表の配置
tree.pack()

#行が選択されたときに呼び出される関数
def on_tree_select( event ):
    for id in tree.selection():
        print(tree.set(id))
        data_is_tree = tree.set( id )

#上の関数を呼び出すための設定
tree.bind("<<TreeviewSelect>>", on_tree_select)
    
#Button
button_send = Button( frame_list, text = "表示", width = 20 )
button_send.pack()



#view
frame_button.pack( side = tkinter.LEFT, fill = 'y' )
frame_list.pack( fill = tkinter.BOTH )

root.mainloop()
