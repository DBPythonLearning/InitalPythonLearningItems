#Initial method for the letter count challenge
holder1 = "cotedazur"
holder2 = "Tinet"
holder3 = "oranes"
holder4 = "Apples"

# List of holders
holders = [holder1, holder2, holder3, holder4]

# Letters to count (both uppercase and lowercase)
letters_to_count = ["A", "Z", "U", "R", "E", "T", "a", "z", "u", "r", "e", "t"]

# Initialize a dictionary to store counts for each holder
holder_counts = {}

# Loop through each holder
for holder in holders:
    count = 0
    # Loop through each character in the current holder
    for t in holder:
        if t in letters_to_count:
            count += 1
    # Store the count in the dictionary with the holder's name as the key
    holder_counts[holder] = count

# Print the counts for each holder
for holder in holders:
    print(f"Count for {holder}: {holder_counts[holder]}")
