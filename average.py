score = input("점수를 입력하세요(,로 분리) : ").split(",")
score = [int(s) for s in score]


score.sort()
score = score[1:-1]
avg = sum(score) / len(score)
print("유효 평균값은", str(format(avg, ".2f")))

mid_index = len(score)//2
print("중앙값은", str(score[mid_index]))