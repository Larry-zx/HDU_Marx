import docx
import json

docxFile = '单选题.docx'
doc = docx.Document(docxFile)
timu_list = []
a_list = []
flag = 0
option_dict = [None, "A", "B", "C", "D"]
tmp_dict = {
    "id":None,
    "subject": None,
    "option": {"A": None, "B": None, "C": None, "D": None},
    "answer": None,
}
for i in doc.paragraphs:
    if len(i.text) == 0:
        continue
    if flag == 0:
        tmp_dict["id"] = int(i.text.split("、")[0].strip())
        tmp_dict["subject"] = i.text.split("、")[-1].strip()
        flag += 1
    elif 1 <= flag <= 4:
        tmp_dict["option"][option_dict[flag]] = i.text.split("、")[-1].strip()
        flag += 1
    elif flag == 5:
        tmp_dict["answer"] = i.text.split("：")[-1].strip()
        flag = 0
        timu_list.append(tmp_dict.copy())
        tmp_dict = {
            "id": None,
            "subject": None,
            "option": {"A": None, "B": None, "C": None, "D": None},
            "answer": None,
        }

fp = open("单选题.json","w")
fp.write(json.dumps(timu_list,ensure_ascii=False))
