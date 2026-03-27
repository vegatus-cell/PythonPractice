def prt_cone_vol(r, h):
    if r>0 and h>0:
        #r, h 모두 양수일 때
        vol = 1/3*3.14*r**2*h
        return vol
    else:
        #r, h가 음수 일 때
        return("반지름과 높이 값에 양수를 입력하세요")

r = int(input("반지름을 입력하세요"))
h = int(input("높이를 입력하세요"))

prt_cone_vol(r, h)