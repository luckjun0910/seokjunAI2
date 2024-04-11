import random

lotto = input("이번주 로또 번호를 추천해드릴까요? 예는 1 아니요 2")

if lotto == "1":
    lotto_num = random.sample(range(1,46),6)
    print(f"추천 번호 : {lotto_num}")

else:
    print("운이 없겠네요")