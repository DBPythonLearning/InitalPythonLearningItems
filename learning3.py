size = "L"
add_pepperoni = "Y"
extra_cheese = "N"
##########################
if size == "L" :
  sizetotal = 25
  if add_pepperoni == "Y":
        peptotal = 3
  else:
        peptotal = 0
elif size == "M":
  sizetotal = 20
  if add_pepperoni == "Y":
        peptotal = 3
  else:
        peptotal = 0
elif size == "S":
  sizetotal = 15
  if add_pepperoni == "Y":
        peptotal = 2
  else:
        peptotal = 0	
if extra_cheese == "Y":
    cheesetotal = 1
else:     
    cheesetotal = 0    
overall_total = sizetotal + peptotal + cheesetotal
overall_total2 = str(overall_total)
print("Your final bill is: $"+ overall_total2 +".") 

