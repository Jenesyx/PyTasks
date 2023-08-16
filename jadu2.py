string = "Whiskey Hotel Four Tango Dash Alpha Romeo Three Dash Yankee Oscar Uniform Dash Sierra One November Kilo India November Golf Dash Four Bravo Zero Uniform Seven"

answer = []
words = string.split(' ')

numbers = {'One' : "1", 'Two' : "2", 'Three' : "3", 'Four' : "4", 'Five' : "5",'Seven' : "7", 'Zero' : "0", 'Dash' : "_"}

for w in words:
    if w in numbers:
        print(numbers[w], end="")
    else:
        print(w[0], end="")