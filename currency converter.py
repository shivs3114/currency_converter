#Currency converter
with open("currency_con.txt") as f:
 a = f.readlines()
#print(a)
currdict={}
for line in a:
   parsed=line.split("\t")
   currdict[parsed[0]]=parsed[1]


 
amount=int(input("Enter amount:->\n"))
print("Enter the name of currency you want to convert this amount to!!!\n Available options\n")
[print(item) for item in currdict.keys()]
currency=input("Enter one of these values-->\n")
print(f"{amount} INR is equal to {amount * float(currdict[currency])} {currency}")

