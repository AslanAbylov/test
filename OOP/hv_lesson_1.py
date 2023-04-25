class Person:
    def __init__(self, fullname, age, is_married):
        self.fullname = fullname
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        print(f'Меня зовут {self.fullname} мне {self.age} я {self.is_married}')

class Students(Person):
    def __init__(self, fullname, age, is_married, **marks):
        super().__init__(fullname, age, is_married)
        self.marks = marks

    def mind_mark(self):
        print(f'Средняя оценка студента {self.marks / len(self.marks)}')

class Teacher(Person):
    salary = 10000
    def __init__(self, fullname, age, is_married, experience):
        super().__init__(fullname, age, is_married)

        self.experience = experience

    def bonus(self):
        print(f'Бонус учителя {self.fullname} состовляет: {self.salary * self.experience}')

teacher_one = Teacher(fullname='Aleksey', age=30, is_married='не женат', experience=10)
teacher_one.introduce_myself()
teacher_one.bonus()


sudent_one = Students(fullname='aslan', age=17, is_married='не женат')
sudent_one.introduce_myself()
