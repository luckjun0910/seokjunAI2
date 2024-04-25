from datetime import datetime, timedelta
from win10toast import ToastNotifier
import time
import requests
from bs4 import BeautifulSoup
import os

toaster = ToastNotifier()

while True:
    now = datetime.now()
    if now.weekday() in [0,1,2,3,4] and now.hour == 21 and now.minute == 34:
        
        toaster.show_toast("알림", "기상시간 입니다!!!", duration=3)

        
        code = '005930'
        url = f'https://finance.naver.com/item/main.nhn?code={code}'
        res = requests.get(url)
        soup = BeautifulSoup(res.content, 'html.parser')
        market_cap = soup.select_one('#content > div.section.trade_compare > table > tbody > tr:nth-child(1) > td:nth-child(2)')
        toaster.show_toast(f"좋은 아침 이네요. 오늘의 삼성전자주가는 {market_cap.text}원 입니다." duration=5)
        

        
        print("얼마나 배고프신가요?")
        print("1. 많이")
        print("2. 중간")
        print("3. 조금")
        print("4. 안고파")

        choice = input("번호를 입력하세요: ")
        if choice == "1":
            food_recommendation = "찌개가 있으면 간단하게 식사를 하시는 게 좋겠네요."
        elif choice == "2":
            food_recommendation = "토스트 어떠세요? 없으면 빵이 좋겠네요!"
        elif choice == "3":
            food_recommendation = "커피 한잔의 여유를 하시는 게 좋겠네요."
        else:
            food_recommendation = "굶어 그럼."

        print(food_recommendation)

        while True:
            user_input = input("몇분후에 종료할까요? 숫자 or 취소 만 입력해 주세요 : ")
            if user_input.isdigit():
                minutes = int(user_input)
                if minutes > 0:
                    os.system(f"shutdown /s /t {minutes * 60}")
                    print(f"{minutes}분 후에 컴퓨터가 종료됩니다. 좋은하루 되세요")
                    break
                else:
                    print("0 이상의 숫자를 입력하세요.")
            elif user_input == "취소":
                os.system("shutdown /a")
                print("컴퓨터 종료 예약이 취소되었습니다. 좋은하루 되세요")
                break
            else:
                print("유효한 입력이 아닙니다. 다시 입력해주세요.")
        
        print("오늘도 즐거운 하루 보내시고 화이팅하세요")
        
        time.sleep(60)
    if now.weekday() == 4 :
        break


