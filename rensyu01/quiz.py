import random

def shutudai():
    qa = random.choice(q_list)
    print(qa["q"])
    return qa["a"]

def kaito(a):
    ans = input("答えを入力してください")
    if ans in a:
        print("正解です")
    else:
        print("不正解")

if __name__ == "__main__":
    q_list = [{"q":"サザエさんの旦那の名前は？", "a" :["マスオ", "ますお"]},
    {"q":"カツオの妹の名前は？", "a":["わかめ","ワカメ"]} , 
    {"q":"タラオはカツオから見てどんな関係？", "a":["甥","おい","甥っ子","おいっこ"]}]
    
    a = shutudai()
    kaito(a)