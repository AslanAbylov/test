class Car:
    wheels = 4 #атрибут класса
    #констпуктор
    def __init__(self, the_model, the_color, the_year, penalties=0.00): #входяшие параметры
        self.model = the_model #атрибуты
        self.color = the_color
        self.year = the_year
        self.penalties = penalties

    def go_to_drive(self, sity):
        print(f'{self.model} driving to {sity}')

    def change_color(self, new_color):
        self.color = new_color

bmw_car = Car('x6', 'bleck', 2020)
honda_civic = Car(the_model='civic', the_year=2018, the_color='red', penalties=20000)
print(f'model: {honda_civic.model}  color: {honda_civic.color}  {honda_civic.penalties}, year: {honda_civic.year}, wheels: {honda_civic.wheels}')
print(f'model: {bmw_car.model}  color: {bmw_car.color}  year: {bmw_car.year}  penalties: {bmw_car.penalties} wheels: {bmw_car.wheels}')
bmw_car.go_to_drive('osh')
honda_civic.change_color('white')
honda_civic.wheels = 5
print(f'model: {honda_civic.model}  color: {honda_civic.color}  {honda_civic.penalties}, year: {honda_civic.year}, wheels: {honda_civic.wheels}')
