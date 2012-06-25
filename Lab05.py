def factorial (intput):
    
     if intput == 0:
         return 1
     else:
         return intput * factorial(intput-1)
        
print factorial(5)

        
def fibonacci (intput):
      MyList =[]
      a,b = 1,1
      for i in range(0,intput):
        MyList.append(a)
        print a
        a,b, = b,a+b
        MyList.append
      return MyList

    
print fibonacci(8)


def prime (n):
    n = abs(int(n))

    if n < 2:
        return False
    if n == 2:
        return True
    if not n & 1:
       return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def isPalindrome (x):
    y = x[::-1]
    if x==y:
        return True
    else:
        return False

def isSubstring(String1,String2):
     if String1 in String2:
          return True
     else:
          return False










    




