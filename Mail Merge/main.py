# Reading names of from txt file
with open("../Mail Merge/Input/Names/invited_names.txt") as names:
    invited_names = names.readlines()

# Reading data from starting letter docx
with open("../Mail Merge/Input/Letters/starting_letter.docx") as file:
    data = file.read()

# a new list being made so that elements could be stripped
new_ls = []
for i in invited_names:
    new_ls.append(i.strip('\n'))

print(new_ls)

for i in new_ls:
    with open(f"../Mail Merge/Output/ReadyToSend/letter_for_{i}.txt", mode="w") as details:
        new_data = data.replace("[name]", i)
        details.write(new_data)
