Ahp=100
Bhp=100

print("----------------------------------------------------------------")
print("게임을 시작하기 전 사전 설정이 필요합니다.")
print("질문과 유의사항을 꼼꼼이 읽고 작성해주세요.")
print()
print("Q. 캐릭터의 이름을 입력해주세요.") #캐릭터의 이름 입력
nameA=input("A. 캐릭터1: ")                #nameA:캐릭터1의 이름
nameB=input("   캐릭터2: ")                #nameB:캐릭터2의 이름
print()
print()
      
print("Q. 캐릭터의 포지션을 공격 혹은 방어 중 하나를 골라 입력해주세요.") #캐릭터의 공격 혹은 방어 선택
print("A.",nameA,end='')        #posA:캐릭터1의 포지션
posA=input("의 포지션: ")       #posB:캐릭터2의 포지션
print("  ",nameB,end='')
posB=input("의 포지션: ")
print()
print()

print("Q. 각 캐릭터의 스킬명을 입력해주세요.") #스킬 이름 입력
print(" ")
print("A.",nameA,end='')             #캐릭터1의 스킬명
skaf=input("의 평타: ")                #skaf:캐릭터1의 평타 이름
print("  ", nameA,end='')
skas=input("의 고유 스킬: ")             #skas:캐릭터2의 고유 스킬 이름
print("  ", nameA,end='')
skat=input("의 궁극기: ")               #skat:캐릭터3의 궁극기 이름

print()

print("  ", nameB,end='')         #캐릭터2의 스킬명
skbf=input("의 평타: ")            #skbf:캐릭터2의 평타 이름
print("  ", nameB,end='')   
skbs=input("의 고유 스킬: ")         #skbs:캐릭터2의 고유 스킬 이름
print("  ", nameB,end='')
skbt=input("의 궁극기: ")           #skbt: 캐릭터3의 궁극기 이름

print()
print()
#각각의 캐릭터의 공격력 혹은 방어력의 수치와 이가 성공할 확률을 작성
print("Q.",nameA,"이(가)",posA,"을(를) 시전할 수 있는 확률과",posA,"력을 입력해주세요.")
print("  ",nameB,"이(가)",posB,"을(를) 시전할 수 있는 확률과",posB,"력을 입력해주세요.")
print()
      
print("----------------*유의할 점*----------------") #수치와 확률을 입력할때의 유의점, 밸런스를 맞추기 위해서
print("1. 성공 확률은 5% 단위로 설정되어야 합니다.")
print("평타의 성공 확률은 70%이상, 고유 스킬의 성공 확률은 30%이상 50%이하,")
print("궁극기의 성공 확률은 10%이하가 되어야 합니다.")
print()
print("2. 스킬 시전 확률과 공격/방어력을 곱한 값이")
print("평타는 700이하, 고유 스킬은 1000이하, 궁극기는 350이하가 되어야 합니다.")
print("-------------------------------------------")
print()
print()

print("A.",nameA,"의", posA,"력과 성공 확률")

print("  ",skaf,"의",posA,end='')       
skafr=input("력 : ")
skafr=int(skafr)                #캐릭터1의 평타의 공격력
print("  ",skaf,end='')
skafp=input("의 성공 확률: ")    #캐릭터1의 평타의 성공확률
skafp=int(skafp)
print()

print("  ", skas,"의",posA,end='')
skasr=input("력 : ")
skasr=int(skasr)                #캐릭터1의 고유 스킬의 공격력
print("  ", skas,end='')
skasp=input("의 성공 확률: ")
skasp=int(skasp)                #캐릭터1의 고유스킬의 성공확률
print()

print("  ", skas,"의",posA,end='')
skatr=input("력 : ")
skatr=int(skatr)             
print("  ",skat,end='')
skatp=input("의 성공 확률: ")
skatp=int(skatp)

print()

print("  ", nameB,"의",posB,"력과 성공 확률")

print("  ", skbf,"의",posB,end='')
skbfr=input("력 : ")
skbfr=int(skbfr)
print("  ", skbf,end='')
skbfp=input("의 성공 확률: ")
skbfp=int(skbfp)
print()

print("  ", skbs,"의",posB,end='')
skbsr=input("력 : ")
skbsr=int(skbsr)
print("  ", skbs,end='')
skbsp=input("의 성공 확률: ")
skbsp=int(skbsp)
print()

print("  ", skbt,"의",posB,end='')
skbtr=input("력 : ")
skbtr=int(skbtr)
print("  ", skbt,end='')
skbtp=input("의 성공 확률: ")
skbtp=int(skbtp)
print()


print("캐릭터에 대한 사전 설정이 완료되었으니,")
print("이제 '게임'을 시작합니다.")
print("--------------------------------------------------------------------")

import random
 
gen_count =   # 생성할 개수
 
arr = [x for x in range(1, 46)]  # 1부터 45까지 생성
for x in range(0, gen_count):
    random.shuffle(arr)     # 섞기
    arr_selected = arr[:6]  # 6개만 선택
    arr_selected.sort()     # 선택된 번호를 정렬
    print(arr_selected)     # 출력
