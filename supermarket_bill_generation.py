"""project"""
from datetime import datetime

name=input("Enter your name =>")
#Lists of items

lists= '''
rice        Rs 20/kg
sugar       Rs 30/kg
salt        Rs 10/kg
oil         Rs 120/kg
paneer      Rs 150/kg
maggi       Rs 50/kg
boost       Rs 90/each
colgate     Rs 85/each
milk        Rs 55/liter
'''

#declaration
price=0
pricelist=[]
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]

# rates for items
items={'rice':20,'sugar':30,'salt':10,'oil':120,'paneer':150,'maggi':50,'boost':90,'colgate':85,'milk':55}
option=int(input("For lists of items press 1 =>"))
if option==1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if you wants to buy press 1 or press 2 for exit=>"))
    if inp1==2:
        break
    if inp1==1:
        item=input("Enter your items=>")
        quantity=int(input("Enter your quantity=>"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append(item,quantity,items,price)
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you enter item is not available")
    else:
        print("you enter worng item")
    inp=input("can i bill the items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"=barma supermarket",25*"=")
            print(28*" ","wanapzathy")
            print("name:",name,30*" ","date:",datetime.now())
            print(75*"_")
            print("sno",8*" ",'items',8*" ",'quantity',3*" ", 'price')
            for i in range(len(pricelist)):
                print(i,8*' ',8*' ',ilist[i],3*' ',qlist[i],plist[i])
            print(75*"_")
            print(50*" ",'totalamount:','Rs',totalprice)
            print("gst amount",50*" ",'Rs',gst)
            print(75*"_")
            print(50*" ",'fonalamount:','Rs',finalamount)
            print(75*"_")
            print(50*" ",'thanks for visiting')
            print(75*"_")
