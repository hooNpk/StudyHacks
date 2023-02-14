import requests
import time

url = input("받고 싶은 icampus 영상 자막 url을 입력해주세요 : ")
file_name = input("저장할 파일 이름을 지정해주세요 (예: caption.txt) : ")
agree = input("이 프로그램 제작자는 박정훈입니다. 커피 한 잔 사주시겠어요? (YES/no) : ")

if agree=='YES':
    res = requests.get(url)
    res.encoding = 'utf-8'
    caption_list = [cap for cap in res.text.replace('\r', '').split('\n') if cap and cap[0]!='0']
    temp_str = ''
    with open(file_name, 'a', encoding='utf-8') as f:
        for caption in caption_list:
            if caption[-1] == '?' or caption[-1] == '.' or caption[-1]=='!' or len(temp_str)>40:
                temp_str += caption
                f.write(temp_str+'\n')
                temp_str = ''
            else:
                temp_str += caption
    print(f"{file_name}으로 잘 저장해뒀습니다. 커피 잊지 말라구요! 5초 뒤에 프로그램이 자동 종료됩니다.")
    time.sleep(5)
else:
    print("흥칫뿡")