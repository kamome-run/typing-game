#tkinterのimport
import tkinter as tk
import tkinter.ttk as ttk

#グローバル変数
root = tk.Tk() #root
frame = ttk.Frame(root) #メインフレームの作成
label = ttk.Label(frame, text='これはラベルです')
entry = ttk.Entry(frame)
btn = ttk.Button(frame, text="回答")

#rootメインウィンドウの設定
root.title("Typing game")
root.geometry("500x400")

#配置
frame.pack() #メインフレームの配置
label.pack() #Labelの配置
entry.pack() #Entryの配置
btn.pack() #ボタンの配置

root.mainloop()