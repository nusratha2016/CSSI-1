students ={"10001578": "Jonathan",
           "10001576": "Elvis",
           "10001575": "Abigail",
           "10001574": "Nusrath",
           "10001573": "Olawale",
           "10001572": "Olivia",
           "10001571": "Rayona",
           "10001570": "Egide",
           "10001244": "Zanif",
           "10001557": "Rahid",
           "10012789": "Imran",}
print students.upper()
print students.lower()

name = raw_input("please enter a name")
def studentLookUp(students,name):
    for x in students:
        if students[x] == name:
            return x
    else:
        return "invaild name"
print studentLookUp(students,name)




'''
Letters = 'Capitalize'
print Letters.upper()
print Letters.lower()
i=""
for x in range(len(Letters)):
    if x % 2 == 0:
        i= i + Letters[x].upper()
    else:
        i= i + Letters[x].lower()
print i





for x in "google":
    print x

for i in ([1,2,3,4,5]):
    print i

def countUp():
    n=11
    while n > 1:
        n= n-1
        print(n)
    print"launch"

countUp()

def isEvenVerbose(x,verbose = False):
    i=x % 2 == 0
    if verbose==True:
     if i:
         print ("number",x,"is Even ")
     else:
         print ("number", x, "is odd")
    return i
    if x % 2 == 0:
        return True
    else:
        return False

print("please input number")
numbers=int(input())
print(isEvenVerbose(3))
'''
