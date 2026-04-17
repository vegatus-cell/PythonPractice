score_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

score_list.sort()
score_list = score_list[1:-1]
print(score_list)
mid_index = (len(score_list)//2)
print(score_list[mid_index])
avg = sum(score_list) / len(score_list)
print(format(avg, ".2f"))

print(score_list)

tech_stack = ["Python", "Java", "Docker", "Python", "Linux", "SQL", "Git", "AWS"]
tech_stack.append("Kubernetes")
print(tech_stack)
tech_stack.insert(2, "CS Teory")
print(tech_stack)

hei_list = [ 1, 5, 14, 26, 31]
sub_hei = hei_list[1:-1]
print(sub_hei)

new_list = [h for h in hei_list if h % 2 == 0]
print(new_list)

sq_list = []
for i in [ 1, 5, 6, 134, 24, 34 ,34, 243, 234]:
    sq_list.append(i*2)
    print(sq_list)

sq_list = [ h**2 for h in [1, 5, 6, 134, 24, 34 ,34, 243, 234] if h % 2 == 0]

print(sq_list)

even_list = []
for i in range (0, 100, 2):
    even_list.append(i)
    print(even_list)

even_list2 = [ i**3 for i in range(1, 100) if i % 2 == 1]
print(even_list2)