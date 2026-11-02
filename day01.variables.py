birth_year=2004
current_year=2026
age=current_year-birth_year
print(age)
#第二题
first='Fu'
middle='zhuo'
last='yang'
print("my full name is:"+first+" "+middle+" "+last)
#number
#第一题
length=92
width=48.8
totalarea=length*width
print(totalarea)
#第二题
number=9
each_costs=1.49
Give_money=20
total_Give_money=number*each_costs
Back_money=Give_money-total_Give_money
print(Back_money)
#第三题
length=5.5
width=5.5
area=length*width
each_costs=500
Cost=area*each_costs
print(Cost)
#第四题
print(bin(17))
#string
#第一题
street="diwujun"
city="dalian"
country='china'
address=street+"\n"+city+"\n"+country
print('address using+operator:',address)
address=f'{street}\n{city}\n{country}'
print("Address using f-string:",address)
#第二题
text="Earth revolves around the sun"
print(text[6:14])
print(text[-3:])
#第三题
unm_fruits=10
unm_vegetables=5
print(f"I eat{unm_vegetables}veggies and {unm_fruits}fruits daliy")
#第四题
s='maine 200 banana khaye'
s=s.replace('banana','samosa')
s=s.replace('200','10')
print("using two line replace:",s)

s='maine 200 banana khaye'
s=s.replace('banana','samosa').replace('200','10')
print("Using single line:",s)
