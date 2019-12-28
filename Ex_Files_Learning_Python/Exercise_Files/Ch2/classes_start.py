#
# Example file for working with classes
#
class myClass():
  def method1(self): #self argument refers to the object itself (like 'this' in java)
    print ("myClass method1")

  def method2(self, someString):
    print ("myClass method2" + someString)


class anotherClass(myClass): #inherit from myClass
  def method1(self): #self argument refers to the object itself (like 'this' in java)
    myClass.method1(self) #calls super class method1 and need to pass 'self' for this to run
    print ("anotherClass method1")

  def method2(self, someString):
    print ("anotherClass method2")

def main():
  c = myClass() #instantiate the object
  c.method1() #do not need to give it the self variable
  c.method2(" this is a string")

  c2 = anotherClass()
  c2.method1() #calls method1 of anotherClass 'class'
  c2.method2("poop")

if __name__ == "__main__":
  main()
