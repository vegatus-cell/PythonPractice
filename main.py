print("두번째 버전입니다.")
# 원뿔 부피 및 겉넓이 계산 프로그램
# 반지름 과 높이 사용자 입력
rad = int(input("반지름을 입력하세요: "))
hei = int(input("높이를 입력하세요: "))
# 모선 계산
sla = pow(rad ** 2 + hei ** 2, 0.5)
#부피 & 겉넓이 출력
vol = 1 / 3 * 3.14 * rad ** 2 * hei
suf = 3.14 * rad ** 2 + 3.14 * rad * sla
print("원뿔의 부피는", str(vol) + "입니다.")
print("원뿔의 겉넓이는", str(suf) + "입니다.")
print("두번째 버전입니다.")

#약간 수정