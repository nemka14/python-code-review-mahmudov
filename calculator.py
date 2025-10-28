def add(a, b):
    """Складывает два числа"""
    return a + b

def subtract(a, b):
    """Вычитает второе число из первого"""
    return a - b

def multiply(a, b):
    """Умножает два числа"""
    return a * b

def divide(a, b):
    """Делит первое число на второе"""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b

def main():
    """Основная функция с консольным интерфейсом"""
    while True:
        print("\nПростой калькулятор")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Выход")
        
        choice = input("Выберите операцию (1-5): ")
        
        if choice == '5':
            print("Пока!")
            break
        
        if choice not in ['1', '2', '3', '4']:
            print("Неверный выбор, попробуйте снова")
            continue
        
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
        except ValueError:
            print("Ошибка: введите числовые значения")
            continue
        
        try:
            if choice == '1':
                result = add(a, b)
                print(f"Результат: {a} + {b} = {result}")
            elif choice == '2':
                result = subtract(a, b)
                print(f"Результат: {a} - {b} = {result}")
            elif choice == '3':
                result = multiply(a, b)
                print(f"Результат: {a} * {b} = {result}")
            elif choice == '4':
                result = divide(a, b)
                print(f"Результат: {a} / {b} = {result}")
        except ValueError as e:
            print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
