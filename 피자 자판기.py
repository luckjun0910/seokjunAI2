print("석준 피자에 오신것을 환영합니다 !")
pizza = str(input("원하시는 피자사이즈는 ? Small(S) or Medium (M) or Large(L)"))
pizzapay = 0


if pizza == "S" : 
    pizzapay = 15000
    print("스몰 사이즈는 15000원 입니다.")
elif pizza == "M" :
    pizzapay = 20000
    print("미디움 사이즈는 20000원 입니다.")
else :
    pizzapay = 30000
    print("라지 사이즈는 30000원 입니다.")

wants_pepperoni = input("페퍼로니 를 추가하시겠습니까? 예(Y) or 아니오(N)")
if wants_pepperoni == "Y" :
    pizzapay += 2000
    print(f"현재{pizzapay}입니다")

wnats_cheeze = input("치즈 추가 하시겠습니까? 예(Y) or 아니오(N)")
if wnats_cheeze == "Y" :
    pizzapay += 3000

how_credit = str(input("어떤 수단으로 결제 하실껀가요? 카드(C) or 현금(M)"))
if how_credit == "C" :
    print(f"IC카드를 꽂아주세요 총 결제 금액은 {pizzapay}입니다.")
else :
    print(f"현금은 카운터에서 결제해주세요 총 결제 금액은 {pizzapay}입니다.")
