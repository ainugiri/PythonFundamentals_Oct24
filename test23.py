#FUNCTION IN PYTHON
# SET OF CODE 
# DEFINE -> DEF  FUNCTION NAME -> PARAMETER -> CODE -> RETURN
# CALL  -> FUNCTION NAME -> ARGUMENT -> RETURN  

def welcome(fname, lname, country = "Poland"):
    print("Thank you for joining us, " + fname + " " + lname + " from " + country)

welcome("Giri","Prasad", "India")
welcome("John","Doe", "USA")
welcome("Prabhakar","Vel", "India")
welcome("Michael", "Asif", "USA")
welcome("Mohammed","Arafat", "Bangladesh")
welcome("Steffen", "Friedrich", "Germany")
welcome("Sergio", "Ramos")

def quadratic(a,b,c):
    return b**2 - 4*a*c

x = quadratic(1,2,1)
y = quadratic(1,3,1)
z = quadratic(1,4,1)

print(x)
print(y)
print(z)
