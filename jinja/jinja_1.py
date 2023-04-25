from jinja2 import Template


cars = [
    {'model': 'audi', 'price': 32000},
    {'model': 'mers', 'price': 12000},
    {'model': 'bmw', 'price': 4000},
    {'model': 'maklaren', 'price': 8000},
    {'model': 'jiguli', 'price': 24000},
]

mpl = "Сумарная сумма всех авто {{ cs | sum(attribute='price') }}"
tm = Template(mpl)
msg = tm.render(cs=cars)
print(msg)




#
# data = '{%raw%} модуль jinja что то {{ name }} что то что то {%endraw%}'
#
# tm = Template(data)
# msg = tm.render(name='Федор')
# print(msg)






# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person_1 = Person('Федор', 28)
#
# tm = Template('привет мне {{ p.name }} лет меня зовут {{ p.age }}')
# msq = tm.render(p = person_1 )
# print(msq)