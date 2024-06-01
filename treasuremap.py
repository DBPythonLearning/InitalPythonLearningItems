line1 = ["", "", ""]
line2 = ["", "", ""]
line3 = ["", "", ""]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = "a3"
#############################################
#take the input and split it
position2 = position.upper()
position3 = str(position2)
target1 = position2[:len(position3)//2]
target2 = int(position3[len(position3)//2:])
target2 = int(target2-1)
#Set the treasure    
Treasure = 'X'
# now the grid
# Give the cordinates now array settings
if target1 == "A":
    p1=0
elif target1 == "B":
    p1=1
elif target1 == "C":
    p1=2
if target2 == 0:
    line1[p1] = Treasure      
if target2 == 1:
    line2[p1] = Treasure    
if target2 == 2:
    line3[p1] = Treasure            
#Print array
print(f"{line1}\n{line2}\n{line3}")

