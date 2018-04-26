global count

def ap(get_fullname):
   def func_wrapper(*args, **kwargs):
       return "{} lives in 205".format(get_fullname(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self, name, family):
        self.name = name
        self.family = family

    @ap
    def get_fullname(self):
        return self.name+" "+self.family

my_person1 = Person("Jose", "Danieel")

my_person2 = Person("Diego", "Barreto")

my_person3 = Person("Alexandre", "Liberal")

print (my_person1.get_fullname())
print (my_person2.get_fullname())
print (my_person3.get_fullname())
