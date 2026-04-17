close = [ 123, 345, 45, 43, 3 , 12, 33, 4, 2123, 27, 234, 23, 865, 37, 15, 436, 278, 123, 752, 385, 3856, 239]
ma3 = [ sum(close[i:i+3])/3 for i in range(len(close)-2)]

hot_days = [ i for i in range(len(ma3)) if ma3[i] > 100]
hot_value = [ma3[i] for i in range(len(ma3)) if ma3[i] > 100]
hot_value2 = [ma3[i] for i in hot_days]
print(ma3)
print(hot_days)
print(hot_value)
print(hot_value2)

