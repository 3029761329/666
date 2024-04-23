class Dog:
    name='unknown'

    def __init__ (self):
        self.is_walked= False

    def walk(self):
        print('walked')
        self.is_walked=True

class DogSpike(Dog):
    name='Spike'

class DogMike(Dog):
    name='Mike'
my_dog= DogSpike()
friends_dog= DogMike()
print ('my dog name Spike')
print ('friend dog name Mike')

class Dog:
       name = 'unknown'
       def__init__(self, breed, speed):
        self.is_walked = False
          self.breed = breed
          self.speed = speed
       
       def walk(self):
           print(f'dog {self.name} walks')
           self.is_walked = True

class DogSpike(Dog):
    name = 'Spike'

class DogMike(Dog):
    name = 'Mike'

my_dog = DogSpike( 'bulldog', 12)
       
