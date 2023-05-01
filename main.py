from PIL import Image
import os
import csv

def z1():
    os.mkdir('obrabotka1.0')

    for filename in os.listdir("G:\лаба9"): #обход всех файлов
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image = Image.open(os.path.join("G:\лаба9", filename))
            filtered_image = image.convert("L")
            new_name = "obrabotka1.0/new3_" + filename
            filtered_image.save(new_name)


def z2():
    os.mkdir('obrabotka2.01')

    for filename in os.listdir("G:\лаба9"): #обход всех файлов
        if filename.endswith('.jpg'):
            image = Image.open(os.path.join("G:\лаба9", filename))
            filtered_image = image.convert("L")
            new_name = "obrabotka2.01/new3_" + filename
            filtered_image.save(new_name)


def z3():
    with open('G:\лаба9\data.csv') as file:
        reader = csv.reader(file)
        summ = 0
        print("Нужно купить:")
        for row in reader:
            product, number, price = row
            summ += int(number) * int(price)
            print(f"{product} - {number} шт. за {price} руб.")
        print(f"Итоговая сумма: {summ} руб.")

z1(),z2(),z3()