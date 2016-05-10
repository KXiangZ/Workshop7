from guitar import Guitar

counter=True
print("My guitars!")
guitar_list=[]
i=1
while counter==True:
    name=input("Name:")
    if name=="":
        break
    year=input("Year:")
    cost=input("Cost:")
    guitar=Guitar(name,year,cost)
    guitar_list.append(guitar)
    print(guitar)

for element in guitar_list:
    if element.is_vintage():
        vintage_string="(vintage)"
    else:
        vintage_string=""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(i, element.name, element.year, float(element.cost),vintage_string))
    i+=1