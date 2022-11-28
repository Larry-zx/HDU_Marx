import json
import PySimpleGUI as sg
import random

data = json.load(open("题库/多选题.json", "r"))
subject_num = len(data)

def start(start_id,random_flag):
    i = start_id - 2
    count = 0
    acc = 0
    while True:
        if random_flag:
            i = random.randint(0, subject_num)
        else:
            i += 1
            if i >= subject_num: break
        layout = [
            [sg.Text("%d.%s" % (data[i]["id"], data[i]["subject"]), size=(64, 3), font=20, text_color='Black',
                     auto_size_text=True)],
            [sg.Checkbox("A.%s" % (data[i]['option']["A"]), default=False, key="A", size=(64, 1), font=20,
                         text_color='navy')],
            [sg.Checkbox("B.%s" % (data[i]['option']["B"]), default=False, key="B", size=(64, 1), font=20,
                         text_color='navy')],
            [sg.Checkbox("C.%s" % (data[i]['option']["C"]), default=False, key="C", size=(64, 1), font=20,
                         text_color='navy')],
            [sg.Checkbox("D.%s" % (data[i]['option']["D"]), default=False, key="D", size=(64, 1), font=20,
                         text_color='navy')],
            [sg.Button(' 确定 ', key="ok", font=20)],
            [sg.Text("正确率:%d/%d" % (acc, count), size=(64, 1), font=30, text_color='black')],
            [sg.Button('主页面', key="menu", font=20),sg.Button('退出', key="exit", font=20), ],
        ]
        window = sg.Window('马原题库', layout, default_element_size=(24, 2), auto_size_text=True)
        event, values = window.read()
        total = ""
        for x in values.keys():
            if values[x]:
                total += x
        window.close()
        if event == 'menu':break
        if event == 'exit': exit(0)
        answer = data[i]["answer"]
        if total != answer:
            str = '正确答案是: %s ' % (answer)
            test_color_dict = {"A": "navy", "B": "navy", "C": "navy", "D": "navy"}
            for i in range(len(answer)):
                test_color_dict[answer[i]] = "#CD2626"
            layout_ = [
                [sg.Text("%d.%s" % (data[i]["id"], data[i]["subject"]), size=(64, 3), font=20, text_color='Black',
                         auto_size_text=True)],
                [sg.Text("A.%s" % (data[i]['option']["A"]), size=(64, 1), font=20, text_color=test_color_dict["A"])],
                [sg.Text("B.%s" % (data[i]['option']["B"]), size=(64, 1), font=20, text_color=test_color_dict["B"])],
                [sg.Text("C.%s" % (data[i]['option']["C"]), size=(64, 1), font=20, text_color=test_color_dict["C"])],
                [sg.Text("D.%s" % (data[i]['option']["D"]), size=(64, 1), font=20, text_color=test_color_dict["D"])],
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
