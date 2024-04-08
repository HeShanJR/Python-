year = eval(input('请输入要判断的年份：'))
if(year %100 != 0 and year % 4 == 0) or year % 400 == 0
   print(f'{year}年是闰年。')
else:
   print(f'{year}年是平年。')
