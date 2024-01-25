def leap_year(year):
    
    if year % 4 == 0 and ( year % 400 == 0  or year % 100 != 0):
        return True
    else:
        return False
    
def dayOfProgrammer(year):
    # Write your code here
    dias = 215
    if leap_year(year):
        dias += 29
    else:
        dias += 28
    return str(256 - dias)+ ".09." + str(year)

print(dayOfProgrammer(1700))
