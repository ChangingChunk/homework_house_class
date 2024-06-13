class House:
  def __init__(self, name, number_of_floors):
    self.name = name
    self.number_of_floors = number_of_floors

  def go_to(self, new_floor):
    if new_floor <= self.number_of_floors and new_floor > 1:
      i =1
      while i <= int(new_floor):
        print(i)
        i += 1
    else:
      print(f'Этажа {new_floor} не существует')

elbrus = House('ЖК эльбрус', 10)
dream = House('ЖК мечта', 30)
elbrus.go_to(5)
elbrus.go_to(11)
elbrus.go_to(-7) 
dream.go_to(15)
dream.go_to(70)