import tkinter as tk
import time
import threading
import tkinter.messagebox as tkbox
import random


win = tk.Tk()
win.title("幸运抽奖")
win.geometry("760x700")
bg = "white"
sleep = True
vary_sleep = True
text1 = tk.Label(win,text="奖品1:\n\n卡通水杯",bg=bg,height=6,width=16)
text1.place(x=60,y=40)
text2 = tk.Label(win,text="奖品2:\n\n体重秤",bg=bg,height=6,width=16)
text2.place(x=230,y=40)
text3 = tk.Label(win,text="奖品3:\n\n旺仔QQ糖",bg=bg,height=6,width=16)
text3.place(x=400,y=40)
text4 = tk.Label(win,text="奖品4:\n\n秘制小汉堡",bg=bg,height=6,width=16)
text4.place(x=570,y=40)
text5 = tk.Label(win,text="奖品5:\n\n好果汁吃",bg=bg,height=6,width=16)
text5.place(x=570,y=170)
text6 = tk.Label(win,text="奖品6:\n\n王甜心饺子",bg=bg,height=6,width=16)
text6.place(x=570,y=300)
text7 = tk.Label(win,text="奖品7:\n\n暑假密卷",bg=bg,height=6,width=16)
text7.place(x=570,y=430)
text8 = tk.Label(win,text="奖品8:\n\n旺仔套装",bg=bg,height=6,width=16)
text8.place(x=570,y=560)
text9 = tk.Label(win,text="奖品9:\n\n大逼斗",bg=bg,height=6,width=16)
text9.place(x=400,y=560)
text10 = tk.Label(win,text="奖品10:\n\n战斧牛排",bg=bg,height=6,width=16)
text10.place(x=230,y=560)
text11 = tk.Label(win,text="奖品11:\n\n谢谢参与",bg=bg,height=6,width=16)
text11.place(x=60,y=560)
text12 = tk.Label(win,text="奖品12:\n\n云南",bg=bg,height=6,width=16)
text12.place(x=60,y=430)
text13 = tk.Label(win,text="奖品13:\n\n加餐",bg=bg,height=6,width=16)
text13.place(x=60,y=300)
text14 = tk.Label(win,text="奖品14:\n\n海贼王",bg=bg,height=6,width=16)
text14.place(x=60,y=170)
text_list = [text1,text2,text3,text4,text5,text6,text7,text8,text9,text10,text11,text12,text13,text14]
 
def menu():
    tkbox.showinfo("作者", "李狗蛋")
 
mainmenu = tk.Menu(win)
filemenu = tk.Menu(mainmenu,tearoff=False)
mainmenu.add_cascade (label="操作",menu=filemenu)
filemenu.add_command (label="作者",command=menu)
filemenu.add_command (label="退出",command=win.quit)
 
win.config (menu=mainmenu)
 
def end_code():
    global vary_sleep
    vary_sleep = False
 
def rounds():
    global sleep,vary_sleep
    x = 0
    sl = 0.4
    if sleep==True:
        while True:
            if vary_sleep==False:
                sl = sl +0.04
                time.sleep(sl)
                for i in text_list:
                    i['bg'] = "white"
                text_list[x]['bg'] = 'red'
                x += 1
                if x >= len(text_list):
                    x = x%len(text_list)
                if sl>0.3:
                    value = text_list[x-1]['text']
                    if x not in [9,7,11]:
                        continue
                    tkbox.showinfo("感谢您的关注","恭喜获得:{}".format(value))
                    vary_sleep=True
                    return
                    # tkbox.showinfo("如果对您有帮助", "请前往某某地 领取您的奖品！！！")

            else:
                sl = sl -0.01
                if sl<0.02:
                    sl = 0.02
                time.sleep(sl)
                for i in text_list:
                    i['bg'] = "white"
                text_list[x]['bg'] = 'red'
                # print(x)
                x += 1
                if x >= len(text_list):
                    x = x%len(text_list)
    else:
        return
 
def start():
    t = threading.Thread(target=rounds)
    t.start()
 
start_button = tk.Button(win,text="开始",height=8,width=20,command=start)
start_button.place(x=210,y=250)
start_button = tk.Button(win,text="结束",height=8,width=20,command=end_code)
start_button.place(x=390,y=250)
win.mainloop()
start_button = tk.Button(win,text="开始",height=8,width=20,command=start)
start_button.place(x=210,y=250)
start_button = tk.Button(win,text="结束",height=8,width=20,command=end_code)
start_button.place(x=390,y=250)
win.mainloop()