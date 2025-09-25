#!/usr/bin/env python3

class Calculator:
    def __init__(self):
        self.operators = ["+", "-", "*", "/", "//", "%", "**"]
        self.comparisons = ["==", "!=", ">", "<", ">=", "<="]
        self.logicalops = ["and", "or", "not"]
        self.bitwiseops = ["&", "|", "^", "~", "<<", ">>"]
        self.membershipops = ["in", "not in"]
        self.identityops = ["is", "is not"]

    def start(self):
        print("Терминальный калькулятор")
        while True:
            print("\nГлавное меню:")
            print("1. Арифметические операторы")
            print("2. Операторы сравнения")
            print("3. Логические операторы")
            print("4. Побитовые операторы")
            print("5. Операторы принадлежности")
            print("6. Операторы тождественности")
            print("0. Выход")
            
            choice = input("Выберите категорию: ")
            
            if choice == "0":
                print("Выход.")
                break
            elif choice == "1":
                self.arithmetic()
            elif choice == "2":
                self.comparison()
            elif choice == "3":
                self.logic()
            elif choice == "4":
                self.bitwise()
            elif choice == "5":
                self.membership()
            elif choice == "6":
                self.identity()
            else:
                print("Ошибка: неверный выбор")

    def arithmetic(self):
        print("\nАрифметические операторы:")
        print("1. [+] Сложение")
        print("2. [-] Вычитание")
        print("3. [*] Умножение")
        print("4. [/] Деление")
        print("5. [//] Целочисленное деление")
        print("6. [%]  Остаток от деления")
        print("7. [**] Возведение в степень")
        
        try:
            choice = int(input("Выберите операцию: "))
            if choice < 1 or choice > 7:
                print("Ошибка: неверный ввод")
                return
        except:
            print("Ошибка: неверный ввод")
            return
        
        first = self.number("Введите первое число: ")
        second = self.number("Введите второе число: ")
        
        try:
            if choice == 1:
                print(first + second)
            elif choice == 2:
                print(first - second)
            elif choice == 3:
                print(first * second)
            elif choice == 4:
                print(first / second)
            elif choice == 5:
                print(first // second)
            elif choice == 6:
                print(first % second)
            elif choice == 7:
                print(first ** second)
        except ZeroDivisionError:
            print("Ошибка: деление на ноль")
        except Exception:
            print("Ошибка: неверный ввод")

    def comparison(self):
        print("\nОператоры сравнения:")
        print("1. [==] Равно")
        print("2. [!=] Не равно")
        print("3. [>]  Больше")
        print("4. [<]  Меньше")
        print("5. [>=] Больше или равно")
        print("6. [<=] Меньше или равно")
        
        try:
            choice = int(input("Выберите операцию: "))
            if choice < 1 or choice > 6:
                print("Ошибка: неверный ввод")
                return
        except:
            print("Ошибка: неверный ввод")
            return
        
        first = self.number("Введите первое число: ")
        second = self.number("Введите второе число: ")
        
        if choice == 1:
            print(first == second)
        elif choice == 2:
            print(first != second)
        elif choice == 3:
            print(first > second)
        elif choice == 4:
            print(first < second)
        elif choice == 5:
            print(first >= second)
        elif choice == 6:
            print(first <= second)

    def logic(self):
        print("\nЛогические операторы:")
        print("1. [and] Логическое И")
        print("2. [or]  Логическое ИЛИ")
        print("3. [not] Логическое НЕ")
        
        try:
            choice = int(input("Выберите операцию: "))
            if choice < 1 or choice > 3:
                print("Ошибка: неверный ввод")
                return
        except:
            print("Ошибка: неверный ввод")
            return
        
        if choice == 3:
            first = self.boolean("Введите логическое значение (0/1/True/False): ")
            print(not first)
        else:
            first = self.boolean("Введите первое логическое значение (0/1/True/False): ")
            second = self.boolean("Введите второе логическое значение (0/1/True/False): ")
            
            if choice == 1:
                print(first and second)
            elif choice == 2:
                print(first or second)

    def bitwise(self):
        print("\nПобитовые операторы:")
        print("1. [&]  Побитовое И")
        print("2. [|]  Побитовое ИЛИ")
        print("3. [^]  Побитовое исключающее ИЛИ")
        print("4. [~]  Побитовое НЕ")
        print("5. [<<] Сдвиг влево")
        print("6. [>>] Сдвиг вправо")
        
        try:
            choice = int(input("Выберите операцию: "))
            if choice < 1 or choice > 6:
                print("Ошибка: неверный ввод")
                return
        except:
            print("Ошибка: неверный ввод")
            return
        
        if choice == 4:
            first = self.number("Введите число: ", asint=True)
            print(~first)
        elif choice in [5, 6]:
            first = self.number("Введите число: ", asint=True)
            shift = self.number("Введите величину сдвига: ", asint=True)
            if shift < 0:
                print("Ошибка: отрицательный сдвиг")
                return
            
            if choice == 5:
                print(first << shift)
            else:
                print(first >> shift)
        else:
            first = self.number("Введите первое число: ", asint=True)
            second = self.number("Введите второе число: ", asint=True)
            
            if choice == 1:
                print(first & second)
            elif choice == 2:
                print(first | second)
            elif choice == 3:
                print(first ^ second)

    def membership(self):
        print("\nОператоры принадлежности:")
        print("1. [in]     Принадлежность")
        print("2. [not in] Не принадлежность")
        
        try:
            choice = int(input("Выберите операцию: "))
            if choice < 1 or choice > 2:
                print("Ошибка: неверный ввод")
                return
        except:
            print("Ошибка: неверный ввод")
            return
        
        element = self.value("Введите элемент: ")
        container = self.value("Введите контейнер: ")
        
        try:
            if choice == 1:
                print(element in container)
            elif choice == 2:
                print(element not in container)
        except Exception:
            print("Ошибка: контейнер")

    def identity(self):
        print("\nОператоры тождественности:")
        print("1. [is]     Тождественно")
        print("2. [is not] Не тождественно")
        
        try:
            choice = int(input("Выберите операцию: "))
            if choice < 1 or choice > 2:
                print("Ошибка: неверный ввод")
                return
        except:
            print("Ошибка: неверный ввод")
            return
        
        first = self.value("Введите первый объект: ")
        second = self.value("Введите второй объект: ")
        
        if choice == 1:
            print(first is second)
        elif choice == 2:
            print(first is not second)

    def number(self, message, asint=False):
        while True:
            s = input(message)
            try:
                if asint:
                    return int(s)
                else:
                    return float(s)
            except Exception:
                print("Ошибка: неверный ввод")

    def boolean(self, message):
        while True:
            s = input(message).strip()
            if s in ["True", "1"]:
                return True
            elif s in ["False", "0"]:
                return False
            else:
                print("Ошибка: неверный ввод")

    def value(self, message):
        s = input(message)
        try:
            return eval(s)
        except Exception:
            return s

if __name__ == "__main__":
    Calculator().start()
