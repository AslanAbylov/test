class Adress:
    def __init__(self, city, street, street_num):
        self.__city = city
        self.__street = street
        self.__street_num = street_num

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

class Animals:
    birgh_year = 2022
    def __init__(self, name, age, adress):
        if isinstance(adress, Adress):
            self.__adress = adress
        else:
            raise AttributeError('Адпес должен быть типом Adress')
        self.name = name
        self.__age = age

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value

    def get_age(self):
        self.__age

    def set_age(self, value):
        if value > 0:
            self.__age = value
        else:
            print('возраст должен быть положительным')

    def info(self):
        self.__born()
        print(f'Имя: {self.name}, age: {self.__age}, birgh_year: {self.birgh_year - self.__age} ')

    def __born(self):
        print(f'Animal name with {self.name} was born!')

dog_adress = Adress('osh', 'osmonkunova', 45)
some_animals = Animals(name='Reks', age=5, adress=dog_adress)
some_animals.info()


