###### The {String} is the task! We have to understand what it is and deal with it

# We can see that there is a letter or symbol first and then a number
# So the number can be the position of that letter in a sentence!
# 

string = "T4 l16 _36 510 _27 s26 _11 320 414 {6 }39 C2 T0 m28 317 y35 d31 F1 m22 g19 d38 z34 423 l15 329 c12 ;37 19 h13 _30 F5 t7 C3 325 z33 _21 h8 n18 132 k24"

# We split the string to look like this!
## ==> ['T4', 'l16', '_36', '510', '_27', 's26', '_11', '320', '414', '{6', '}39', 'C2', 'T0', 'm28', '317', 'y35', 'd31', 'F1', 'm22', 'g19', 'd38', 'z34', '423', 'l15', '329', 'c12', ';37', '19', 'h13', '_30', 'F5', 't7', 'C3', '325', 'z33', '_21', 'h8', 'n18', '132', 'k24']
parts = string.split(" ")

# We create a loop with 40 start(*)
# why 40? Because the the numbers are 0 to 39!
answer = []
for i in range(40):
    answer.append('*')

# This is a funtion to set the answer in it
def print_range_item(s):
    print(''.join(s))

# The task of this for loop is to set the each part of the "parts" in p! So the position 0 of the p is the letter or symbole
# and the position 1 is the number and the answer is a string! so we set the "c" in the position of "i" in asnwer, for example the i is 15 and the letter of 15 is l and we set the l in position 15
for p in parts:
    c = p[0]
    i = int(p[1:])
    answer[i] = c
    print_range_item(answer)

print_range_item(answer)


