from dog import Dog
from person import Person

if __name__ == "__main__":
  luffy = Dog('luffy')
  zoro = Dog('zoro')
  nami = Dog('nami')
  person = Person('jp', 26, [luffy, zoro, nami])
  print(person.dogs[0].name)
    