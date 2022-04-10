#global variables and functions


x=5                     #global variable declared

#a function myfn is defined below. it is not executed until called
def myfn():
    y=6                 # y is a local variable
    print(x+y)          # global variable used inside a function


myfn()                  #function call which gives actual output
#print(y)               it is not possible to use local variable outside the function

############################################################################

nm='satheesh'                   #global variable nm declared

def names():
    nm='vanitha'                #local variable nm declared
    print('Hi my name is'+nm)    #local value of nm printed inside function

names()

print("my husband's name is "+nm)#global value of nm printed outside function
    

############################################################################

nm='satheesh'                   #global variable nm declared

def names():
    global nm                   #global variable is declared inside function
    nm='vanitha'                #global declaration is done before value assignment
    print('Hi my name is'+nm)    #local value of nm printed inside function

names()

print("my husband's name is "+nm)#global value of nm printed outside function

########################################################################

def nmfn(fnm,lnm):
    print('my name is '+fnm+" "+lnm)

nmfn('satheesh','kumar')

def mycounty(county):
    print('my ountry is '+county)

mycounty('india')

###########################################################################

#any data types of argument to a function
#(string, number, list, dictionary etc.)

def fruitlst(frts):
    for x in frts:
        print(x)
fruits=['apple','banana','lemon']
fruitlst(fruits)

###########################################################################

print('##########################')
#default arguments
def mycounty(county='india'): #default value defined
    print('my country is '+county)

mycounty('america')
mycounty()                  #function passes no parameter
mycounty('china')

########################################################################
print('##########################')
#key=value or keyword arguments
def nmfn(fnm,lnm):
    print('my name is '+fnm+" "+lnm)

nmfn(fnm='satheesh',lnm='kumar')

#key=value arguments
def nmfn(lnm,fnm): #interchanged arguments
    print('my name is '+fnm+" "+lnm)

nmfn(fnm='satheesh',lnm='kumar')

#key=value arguments
def nmfn(a,b,c): #interchanged arguments
    print(pow(a+b,c))

nmfn(c=4,a=3,b=2)

##########################################################################

print('##########################')
#arbitrary arguments *args
def studs(*studnames): #fn receives tuple of arguments
    n=len(studnames)
    print('no of students received is ',n)
    print(studnames[0])
    print(studnames[1])
    print(studnames[2])
studs('satheesh','pranav','vanitha')

def studs(*studnames): #fn receives tuple of arguments
    n=len(studnames)
    print('no of students received is ',n)
    for x in studnames:
        print(x)
studs('sa','pra','va')

#########################################################################

print('##########################')
#arbitrary keyword arguments **args
def studs(**studnames): #fn receives dictionary of arguments
    n=len(studnames)
    print('ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZzz')
    for x in studnames:
        print(x)
    print('no of students received is ',n)
    print(studnames['ee01'])
    print(studnames['ee02'])
    print(studnames['ee03'])
studs(ee01='satheesh',ee02='pranav',ee03='vanitha')

#arbitrary keyword arguments **kwargs
def studs(**studnames): #fn receives dictionary of arguments
    n=len(studnames)
    print('no of students received is ',n)
    for x in studnames: #x holds key name
        print(x)        #prints key name
        print(studnames[x]) #prints value of key
studs(ee01='satheesh',ee02='pranav',ee03='vanitha')

#########################################################################
def powr(x,y):
    p=1
    for z in range(y):
        p*=x
    return(p)
print(powr(2,3))
v=powr(3,4)
print(v)
