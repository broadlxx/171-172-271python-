class Dog():
   age = 0
   name = ""
   weight = 0

   def bark(self):
       print("Woof says",self.name)

myDog = Dog()

myDog.name = "Spot"
myDog.weight = 20
myDog.age = 3

myDog.bark()


class Person():
      __surname = 'Allen'

      def setName(self, name):
            self.name = name

      def getName(self):
            return self.name
      def getSurname(self):
          return self.__surname

      def __secretmessage(self):
            print('I can’t tell my name, it is ' + self.name + ' ' + self.__surname)

      def _semi_secret(self):
           print('I have not told you my name.')

      def public_message(self):
          print('The secret message is: ')
          self.__secretmessage()
x = Person()

x.setName('John')
print(x.getName())
x.public_message()
print(x.getSurname())



class Filter():
    def __init__(self):
       self.blocked = []

    def filter(self, sequence):
    	return [x for x in sequence if x not in self.blocked]

class SPAMFilter(Filter): # SPAMFilter is a subclass of Filter
    def __init__(self):
      	Filter.blocked = ['SPAM']

f = Filter()
print(f.filter([1, 2, 3]))

s = SPAMFilter()
print(s.filter(["SPAM","SPAM","eggs","bacon","SPAM","SPAM"]))


class Bird():
   def __init__(self):
       self.hungry = True

   def eat(self):
       if self.hungry:
          print ('Aaaahh…' )
       else:
         print ('No thanks!')
class SongBird(Bird):   # subclass of Bird
    def __init__(self):
        self.sound = 'Squwark!'
        Bird.__init__(self)

    def sing(self):
        print(self.sound)

sb = SongBird()
sb.sing()
sb.eat()

