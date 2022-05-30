# from time import sleep
#
# class TrafficLight:
#     __collor = ['Красный','Желтый','Зеленый']
#     def running(self):
#         i = 0
#         while i !=3:
#             print(TrafficLight.__collor[i])
#             if i == 0:
#                 sleep(120)
#             elif i == 1:
#                 sleep(2)
#             elif i == 2:
#                 sleep(5)
#             i += 1
# t = TrafficLight ()
# t.running()
############################################
# class Road:
#     def __init__(self, lenght, width):
#         self._length = lenght
#         self._width = width
#         self.width = 25
#         self.height = 5
#     def asphalf_mass(self):
#         asphalf_mass = self._length * self._width * self.width * self.height / 1000
#         print(f'ДЛЯ распила нужно {round(asphalf_mass)} тон асфальта')
# r = Road(5000, 20)
# r.asphalf_mass()
# ################################################
#
# class Worker:
#     name: str
#     surname: str
#     position: str
#     _income: dict = {"wage": 0.0, "bonus": 1.0}
#
#     def __init__(self, name: str, surname: str, position: str, income: dict = {"wage": 0, "bonus": 1.0}) -> None:
#         self.name = name
#         self.surname = surname
#         self.position = position
#         self._income = income
#
#
# class Position(Worker):
#
#     def __init__(self, name: str, surname: str, position: str, income: dict = {"wage": 0, "bonus": 1.0}) -> None:
#         super().__init__(name, surname, position, income)
#
#     def get_full_name(self):
#         return f"{self.surname} {self.name}"
#
#     def get_total_income(self):
#         return self._income["wage"] * self._income["bonus"]