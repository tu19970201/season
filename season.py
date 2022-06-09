month = int(input('請輸入陽曆月份：'))
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
winter = [12,1,2]
if month in spring:
    print(month,'月是春天')
elif month in summer:
    print(month,'月是夏天')
elif month in autumn:
    print(month,'月是秋天')
elif month in winter:
    print(month,'月是冬天')
else:
    print('輸入錯誤，請重新輸入')