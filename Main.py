#Address Book
book = []

name = input("What is the name?: ").title()
numb = input("What is the number: ")
addr = input("What is the address?: ").title()

names = []
numbs = []
addrs = []

def contact():
    var = name, numb, addr
    book.append(var)
    print(var)
    print(book)
    redo = input("Would you like to add another contact?: ")
contact()

#testing git, yet again, again, again
#testing git again of prior lapious carppious
#testing on pycharm

