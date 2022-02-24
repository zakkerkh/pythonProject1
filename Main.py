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

def redoing():
    redo = input("Would you like to add another contact?: ")
    def invalid():
        if redo not in alist:
            print("Invalid Entry")
            stop = input("Would you like to quit?: ")
            if stop in nrlist:
                redoing()
            elif stop in rlist:
                quit()
            elif stop not in alist:
                invalid()
    invalid()


contact(input("What is the name?: ").title(), input("What is the number: "), addr = input("What is the address?: ").title())
redoing()

#testing git, yet again, again, again
#testing git again of prior lapious carppious
#testing on pycharm

