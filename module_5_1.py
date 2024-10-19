
# Реализуйте класс House, объекты которого будут создаваться следующим образом:
# House('ЖК Эльбрус', 30)
# Объект этого класса должен обладать следующими атрибутами:
# self.name - имя, self.number_of_floors - кол-во этажей
# Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
# Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
# Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".


class House:  # созданный класс(Hause)
    def __init__ (self, name, number_of_floors):  # метод(__init__) это конструктор, в нем создаются основные атрибуты

        self.name = name  # атрибут1 - название дома(Hause)
        self.number_of_floors = number_of_floors   # атрибут2 - количество этажей дома

    def go_to (self, new_floor):   # метод(goto) это переход(лифт) от 1 этажа до указанного значения(new_floor)
        self.new_floor = new_floor    # атрибут принимаемый значение при вызове функции(go_to)

        if new_floor >= self.number_of_floors or new_floor <= 1:   # условие1 внутри метода(go_to) сравнивает атрибуты из разных методов
            print("Такого этажа не существует")    # надпись если условие выполняется

        else:   # условие2 при котором перебирается принятое значение с первого элемента и выводится на печать, последовательно
            for i in range(1, new_floor + 1):
                print(i)

h1 = House('ЖК Горский', 18)  # добавление переменной1 в класс(Hause), с присвоением двух значений
h2 = House('Домик в деревне', 2)   # добавление переменной2 в класс(Hause)
print(h1.name, h1.number_of_floors)   #вызов переменной класса с атрибутами метода(__init__)
print(h2.name, h2.number_of_floors)
h1.go_to(5)   # вызов метода(go_to) с присвоением значения(на како этаж надо)
h2.go_to(10)






