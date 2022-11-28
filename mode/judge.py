import json
import PySimpleGUI as sg
import random

data = json.load(open("题库/判断题.json", "r"))
subject_num = len(data)


def start(start_id, random_flag):
    i = start_id - 2
    acc = 0
    count = 0
    while True:
        if random_flag:
            i = random.randint(0, subject_num)
        else:
            i += 1
            if i >= subject_num: break
        layout = [
            [sg.Text("%d.%s" % (data[i]["id"], data[i]["subject"]), size=(64, 3), font=20, text_color='Black',
                     auto_size_text=True)],
            [sg.Button(' 正确 ', key="正确", font=20), sg.Button(' 错误 ', key="错误", font=20)],
            [sg.Text("正确率:%d/%d" % (acc, count), size=(64, 1), font=30, text_color='black')],
            [sg.Button('主页面', key="menu", font=20),sg.Button('退出', key="exit", font=20), ],
        ]
        window = sg.Window('马原题库', layout, default_element_size=(24, 2), auto_size_text=True)
        event, values = window.read()
        window.close()
        if event == 'menu':break
        if event == 'exit': exit(0)
        answer = data[i]["answer"]
        if event != answer:
            str = '正确答案是: %s ' % (answer)
            layout_ = [
                [sg.Text("%d.%s" % (data[i]["id"], data[i]["subject"]), size=(64, 3), font=20, text_color='Black',
                         auto_size_text=True)],
                [sg.Button('下一题', key="continue", font=20), ],
                [sg.Text(str, size=(64, 1), font=20, text_color='#CD2626')],
                [sg.Button('主页面', key="menu", font=20),sg.Button('退出', key="exit", font=20), ],
            ]
            window = sg.Window('马原题库', layout_, default_element_size=(24, 2), auto_size_text=True)
            event, values = window.read()
            window.close()
            if event == 'menu':break
            if event == 'exit': exit(0)
        else:
            acc += 1
        count += 1
