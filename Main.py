#Address Book
book = []

rlist = ["Yes", "yes", "y"]
nrlist = ["No", "no", "n"]
alist = nrlist + rlist

def contact(name, numb, addr):
    var = name, numb, addr
    book.append(var)
    print(var)
    print(book)
    redoing()

def redoing():
    redo = input("Would you like to add another contact?: ")
    if redo in rlist:
        name = input("What is the name?: ").title()
        numb = input("What is the number: ")
        addr = input("What is the address?: ").title()
        contact(name, numb, addr)
    elif redo in nrlist:
        print("Thank you!")
        quit()
    def invalid():
        if redo not in alist:
            print("Invalid Entry")
            stop = input("Would you like to quit?: ")
            if stop in nrlist:
                contact()
            elif stop in rlist:
                print("Thank you for using the ultimate contact book!")
                quit()
            elif stop not in alist:
                invalid()
    invalid()

name = input("What is the name?: ").title()
numb = input("What is the number: ")
addr = input("What is the address?: ").title()

contact(name, numb, addr)

#testing git, yet again, again, again
#testing git again of prior lapious carppious
#testing on pycharm

