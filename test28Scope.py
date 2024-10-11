# Local Scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

def tempFunc():
    x = 300             # x is local variables
    print(x)
    def subFunc():
        y = 200
        print(x*y)
    subFunc()

# print(x) : # This will cause an error because x is not defined outside of the function.
tempFunc()   # This will print 300, not an error, function can access x, because x is defined inside the function.
#Enclosing Scope: Variable created in the local scope of a function can be used in the local scope of the enclosing functions.

#Globale Scope: A variable created in the main body of the Python code is a global variable and belongs to the global scope.

abc = 121
def calArea():
    global abc
    abc = 100   
    print(abc)

calArea() 

print(abc) # This will print 121, not 100, because abc is defined outside the function.

print(len("Giri Prasad Pujar")) # This will print 17

#LEGBO Rule: Local, Enclosing, Global, Built-in
# If a variable is not defined in the local scope, the enclosing scope is checked, then the global and finally the built-in scope.
