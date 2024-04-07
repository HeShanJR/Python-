year = eval(input('请输入要判断的年份'))
if(year % 100 !=0 and year % 4 == 0) or year % 400 == 0:
    print('{}年是闰年。'.format(year))
else:
    print('{}年是平年。'.format(year))