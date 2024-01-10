#tkinterのimport
import tkinter as tk
import tkinter.ttk as ttk

#グローバル変数
root = tk.Tk() #root
frame = ttk.Frame(root) #メインフレームの作成
topic_list = [] #topicのリスト

#rootメインウィンドウの設定
root.title("Typing game")
root.geometry("500x400")

#Notebookウィジェットの作成
notebook = ttk.Notebook(root)

#タブの作成
tab_game = tk.Frame(notebook, bg='white')
tab_add_topic = tk.Frame(notebook, bg='white')

#Notebookにタブを追加
notebook.add(tab_game, text="Typing game")
notebook.add(tab_add_topic, text="お題の追加")

#ウィジェットの作成
#tab_game
label_game = ttk.Label(tab_game, text='タイピングゲーム')

entry_answer = ttk.Entry(tab_game)
btn_answer = ttk.Button(tab_game, text="回答")

#tab_add_topic
label_entry_topic = ttk.Label(tab_add_topic, text="お題の入力フォーム")

def click_btn_topic():
    
    get_topic = add_topic.get() #入力されたtopicを取得
    topic_list.append(get_topic) #新たに入力されたtopicをリストに追加
    
    for inputed in topic_list: #topicのリストをループ処理で取り出す
        label_show_topic = ttk.Label(tab_add_topic, text=inputed) #入力済みのtopicを表示
        label_show_topic.pack() #入力済みのtopicを表示
        topic_list.remove(inputed) #表示したtopic（inputedに代入された要素）を削除     

add_topic = ttk.Entry(tab_add_topic) #topicの入力フォーム
btn_topic = ttk.Button(tab_add_topic, text="お題の追加！", command=click_btn_topic)

#配置 tab_game
notebook.pack(expand=True, fill='both', padx=10, pady=10)
frame.pack() #メインフレームの配置
label_game.pack() #Labelの配置
entry_answer.pack() #Entryの配置
btn_answer.pack() #回答ボタンの配置

#配置 tab_add_topic
label_entry_topic.pack() #Labelの配置
add_topic.pack()
btn_topic.pack() #ボタンの配置

root.mainloop()