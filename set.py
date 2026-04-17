rad_set = {7, 22, 4, 22, 47}
rad_set2 = {22, 4, 7, 47}

print(rad_set == rad_set2)

if 47 in rad_set:
    print("있음")

print(len(rad_set))
print(sum(rad_set))

rad_set3 = rad_set.union(rad_set2)
print(rad_set3)

even_rad = {e for e in rad_set if e%2 == 0}
print(even_rad)
