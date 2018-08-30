#1. 만든이: 3303 배예원
#2. 프로젝트 주제: 금요일에 퇴사할 때 아침에 짐을 쌀지, 전날에 짐을 쌀지 권유해주는 프로그램
#3. 프로그램 설명: 평균 취침시간과 재침 여부에 대한 습관, 이번주 요일별 아침의 재침 여부, 요일별 밤의 취침시간을 적어주면 짐을 언제 쌀지 알려준다.
#4. 프로그램 후기: 원래 이렇게 길게 짤 생각이 없었는데 아이디어를 조건에 맞추다보니 프로그램의 길이가 무진장 길어졌다.
#                   그래도 조건에 맞추어 프로그램을 하다보니 확실히 공부가 되는 것 같고 내가 원하는 것을 구현하는 과정에서 어떻게 함수를 짤지,
#                   범위를 어떻게 설정할지 많은 고민을 했다. 리스트 내에서 내가 원하는 원소가 몇개 있는지 구하는 함수를 통해 프로그램 길이를 다소 줄일 수 있었다.
#                   좀 궁금한 과정이라면 함수자체를 반복하게 한다면 프로그램 길이와 함수 내에 들어가는 변수의 수를 줄일 수 있었을텐데       
#                   이 과정이 조금 아쉽다.
#
#
#
#
#


print("--------------유의사항---------------------")
print("만약 밤 12시에 잔다면 24:00으로 새벽 1시 30분에 잔다면 25:30, 이런 방식으로 작성부탁.")
print("------------------------------------------")
print() #평상시의 취침시간의 시와 분을 각각 정수 형태의 변수로 저장
a,b=input("Q. 평상시의 취침시간은 몇시임?\nA. ").split(":")
a=int(a)
b=int(b)

print()
print("너님은 지금부터 월요일부터 목요일까지 취침시간을 적으셔야 함.") #이번주의 취침시간의 시와 분을 각각 정수 형태의 변수로 저장
print("시간 작성은 유의사항을 따라 주셈. 안따라하면 오류남.")
print()
msh,msm=input("Q. 월요일의 취침시간\nA. ").split(":") #msh: 월요일의 취침시간의 시, msm:월요일의 취침시간의 분
msh=int(msh)
msm=int(msm)
tsh,tsm=input("Q. 화요일의 취침시간\nA. ").split(":") #tsh: 화요일의 취침시간의 시, tsm:화요일의 취침시간의 분
tsh=int(tsh)
tsm=int(tsm)
wsh,wsm=input("Q. 수요일의 취침시간\nA. ").split(":") #wsh: 수요일의 취침시간의 시, wsm:수요일의 취침시간의 분
wsh=int(wsh)
wsm=int(wsm)
thsh,thsm=input("Q. 목요일의 취침예정시간\nA. ").split(":") #thsh: 목요일의 취침예정시간의 시, thsm:월요일의 취침예정시간의 분
thsh=int(thsh)
thsm=int(thsm)

print()
print("지금부터는 화요일부터 목요일까지의 재침여부를 적으셔야함.")
print("O 혹은 X로 적어주셈.")
print()
tms=input("Q. 화요일 아침의 재침 여부: ") #재침여부를 문자로 저장
wms=input("Q. 수요일 아침의 재침 여부: ")
thms=input("Q. 목요일 아침의 재침 여부: ")


wsth=(msh+tsh+wsh+thsh)/4 #이번주의 취침시간의 평균을 구해주기
wstm=(msm+tsm+wsm+thsm)/4 #wsth: 평균 취침시간의 시, wstm: 평균 취침시간의 분

#def 함수 정의
def cal(wsth,a,wstm,b): #이번주 취침시간의 평균을 계산해서 평소 잘 때의 시간과의 차를 이용해서 피곤한 정도를 측정
   
    #조건문 사용
    if (wsth-a)<=0:
        print("숙면을 취하셨네")
        
    elif (wsth-a)<=1:
        print("그럭저럭 괜찮음. 살만하네")

    elif (wsth-a)<=1 and (wstm-b)<=30:
        print("님 지금 피곤함")

    elif (wsth-a)<=1 and (wsth-a)>30:
        print("매우 피곤함")
        
    else:
        print("죽을지도 모름. 시험기간임?")
    
import random #random 함수를 이용해 재침횟수를 토대로 범위를 정해, 무작위로 재침할 확률을 알려줌

t10=random.randint(90,100)
t11=random.randint(90,100)
t12=random.randint(90,100)
t13=random.randint(90,100)
t14=random.randint(90,100)

t20=random.randint(70,90)
t21=random.randint(70,90)
t22=random.randint(70,90)
t23=random.randint(70,90)
t24=random.randint(70,90)

t30=random.randint(50,70)
t31=random.randint(50,70)
t32=random.randint(50,70)
t33=random.randint(50,70)
t34=random.randint(50,70)

t40=random.randint(30,50)
t41=random.randint(30,50)
t42=random.randint(30,50)
t43=random.randint(30,50)
t44=random.randint(30,50)

t50=random.randint(0,30)
t51=random.randint(0,30)
t52=random.randint(0,30)
t53=random.randint(0,30)
t54=random.randint(0,30)


#def 함수 정의
def tomorrow(wsth,wstm,a,b,t10,t11,t12,t13,t14,t20,t21,t22,t23,t24,t30,t31,t32,t33,t34,t40,t41,t42,t43,t44,t50,t51,t52,t53,t54): #짐을 싸야할 확률을 알려주는 함수
    if (wsth-a)>=2:
        print(">>니가 짐을 싸야할 대략적 확률.")

        for t1 in [t10,t11,t12,t13,t14] :  #for문을 이용해 짐을 싸야할 대략적 확률을 반복해서 나오게 함.
            print(t1,"%")
        def list_sum(lst):
            sum=0
            for i in lst:
                sum +=i
            return sum
        print()
        print(">>니가 짐을 싸야할 평균 확률입니다.")
        print(list_sum([t10,t11,t12,t13,t14])/5,"%")
        print()
        print("P.S. 짐 꼭 싸라. 내일 허둥지둥 나가지 말고.")
        
    elif (wsth-a)>=1 and (wstm-b)>=30:
        print(">>니가 짐을 싸야할 대략적 확률.")

        for t2 in [t20,t21,t22,t23,t24] :
            print(t2,"%")
        def list_sum(lst):
            sum=0
            for i in lst:
                sum +=i
            return sum
        print()
        print(">>니가 짐을 싸야할 평균 확률입니다.")
        print(list_sum([t20,t21,t22,t23,t24])/5,"%")
        print()
        print("P.S. 짐 쌌으면 좋겠는데; ^p^.")
        
    elif (wsth-a)>=1:
        print(">>니가 짐을 싸야할 대략적 확률.")

        for t3 in [t30,t31,t32,t33,t34] :
            print(t3,"%")
        def list_sum(lst):
            sum=0
            for i in lst:
                sum +=i
            return sum
        print()
        print(">>니가 짐을 싸야할 평균 확률입니다.")
        print(list_sum([t30,t31,t32,t33,t34])/5,"%")
        print()
        print("P.S. 짐 싸면 좋고.")
        
        
    elif (wsth-a)<1 and (wsth-a)>=0:
        print(">>니가 짐을 싸야할 대략적 확률.")

        for t4 in [t40,t41,t42,t43,t44] :
            print(t4,"%")
        def list_sum(lst):
            sum=0
            for i in lst:
                sum +=i
            return sum
        print()
        print(">>니가 짐을 싸야할 평균 확률입니다.")
        print(list_sum([t40,t41,t42,t43,t44])/5,"%")
        print()
        print("P.S. 끌리는데로 하세요.")
        
        
    else:
        print(">>니가 짐을 싸야할 대략적 확률.")

        for t5 in [t50,t51,t52,t53,t54] :
            print(t5,"%")
        def list_sum(lst):
            sum=0
            for i in lst:
                sum +=i
            return sum
        print()
        print(">>니가 짐을 싸야할 평균 확률입니다.")
        print(list_sum([t50,t51,t52,t53,t54])/5,"%")
        print()
        print("P.S. 오늘 짐 쌀 시간에 어여 잠이나 자셈.")

        
list1=[tms,wms,thms]
slist1=list1.count("O")
slist1=int(slist1) #리스트함수이용

def jaechimhae(slist1): #당신의 금요일 학교 생활을 위해 재침을 권장하는 함수
    if slist1==3:
        print(">>금요일 재침 필요 없을 듯")
    elif slist1==2:
        print(">>재침 하고 싶으면 하고, 아님 말고")
    else:
        print(">>재침 꼭 해라. 학교에서 죽을 일 있나?")
print()
print()
print("=========================================================")
print()
print("결과를 알려드리겠습니다.")
print()
print("A. 너님의 피곤도 입니다")
print(">>",end="")
cal(wsth,a,wstm,b)
print()
print("A. 너님의 금요일 아침의 재침 필요성입니다.")
jaechimhae(slist1)
print()
print("A. 너님이 목요일 밤 지금 짐을 싸야할 확률입니다.")
tomorrow(wsth,wstm,a,b,t10,t11,t12,t13,t14,t20,t21,t22,t23,t24,t30,t31,t32,t33,t34,t40,t41,t42,t43,t44,t50,t51,t52,t53,t54)
