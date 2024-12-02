import turtle
import argparse

def koch_curve(t, order, size):
    """
    Рекурсивна функція для побудови кривої Коха
    
    """
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order-1, size/3)
            t.left(angle)

def koch_snowflake(order, size=300):
    """
    Створення сніжинки Коха
    
    """
    # Налаштування вікна
    window = turtle.Screen()
    window.setup(width=800, height=600)
    window.title(f'Сніжинка Коха (рівень {order})')
    
    # Створення черепахи
    t = turtle.Turtle()
    t.speed(0)  # Максимальна швидкість
    t.penup()
    t.goto(-size/2, size/3)
    t.pendown()
    
    # Малювання сніжинки
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)
    
    # Завершення
    window.mainloop()

def main():
    # Парсинг аргументів
    parser = argparse.ArgumentParser(description='Генерація сніжинки Коха')
    parser.add_argument('order', type=int, 
                        help='Рівень рекурсії для сніжинки')
    parser.add_argument('-s', '--size', type=float, 
                        default=300, help='Розмір сніжинки')
    
    args = parser.parse_args()
    koch_snowflake(args.order, args.size)

if __name__ == '__main__':
    main()