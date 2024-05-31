name1="Angela Yu"
name2="Cleopatra"
import re
cleaned_name1 = re.sub(r'[^a-zA-Z0-9]', '', name1)
cleaned_name2 = re.sub(r'[^a-zA-Z0-9]', '', name2)
namelong = cleaned_name1 + cleaned_name2
total_count1 = 0
total_count2 = 0
letters_to_count1 = ["T", "R", "U", "E", "t", "r", "u", "e"]
namus_counts = {}
for namus in namelong:
    count = 0
    for t in namus:
        if t in letters_to_count1:
            count += 1
    namus_counts[namus] = count
    total_count1 += count
letters_to_count2 = ["L", "O", "V", "E", "l", "o", "v", "e"]
for namus in namelong:
    count2 = 0
    for t in namus:
        if t in letters_to_count2:
            count2 += 1
    namus_counts[namus] = count2
    total_count2 += count2
ztot1 = str(total_count1)
ztot2 = str(total_count2)
ztot3 = str(ztot1 + ztot2)
ztot4 = int(ztot3)
z = ztot3
if ztot4 < 10:
    print("Your score is "+z+", you go together like coke and mentos.")
elif ((ztot4 > 40)&(ztot4 < 50)):
    print("Your score is "+z+", you are alright together.")
elif ztot4 > 90:
    print("Your score is "+z+", you go together like coke and mentos.")
else:
    print("Your score is "+z+".")