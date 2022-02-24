monthconv = {
    "Jan": "January",
    "Feb": "Febraury",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
}

var1 = input("What Month:")
print(monthconv[var1])
print(monthconv.get("jing", "Not sehr gut entry"))