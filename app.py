import PySimpleGUI as sg
from mode import single_select, multi_select, judge

sg.theme('GreenMono')

while True:
    layout = [
        [sg.Text("这是HDU马克思主义基本原理刷题app", size=(64, 2), font=20, text_color='Black', auto_size_text=True)],
        [sg.Text("由于开发者的技术水平较弱且极为懒惰", size=(64, 2), font=20, text_color='Black')],
        [sg.Text("只能设计出如此简陋敷衍的UI界面", size=(64, 2), font=20, text_color='Black')],
        [sg.Text("相信大家最在乎的不是这个所谓的皮囊而且接下来有趣的灵魂", size=(64, 2), font=20, text_color='Black')],
        [sg.Text("那请选择模式吧", size=(64, 2), font=20, text_color='Black')],
        [sg.Text("顺序模式下起始题目号", font=20, text_color="navy"), sg.InputText("1", size=(6, 2), font=26)],
        [sg.Checkbox(" 随机模式 ", default=False, key="random", size=(64, 1), font=20,
                     text_color='#00688B'), ],
        [sg.Button('  单选题  ', key="single", font=20), sg.Button('  多选题  ', key="multi", font=20),
         sg.Button('  判断题  ', key="judge", font=20), sg.Button('  退出程序  ', key='exit', font=20)],
        [sg.Text(
            "                                                                                                        By HDU_钟鑫")]]
    window = sg.Window('马原题库', layout, default_element_size=(24, 2), auto_size_text=True)
    event, values = window.read()
    if event == "exit": break
    random_flag = values["random"]
    start_id = int(values[0])
    window.close()
    if event == "single":
        single_select.start(start_id, random_flag)
    elif event == "multi":
        multi_select.start(start_id, random_flag)
    elif event == "judge":
        judge.start(start_id, random_flag)
