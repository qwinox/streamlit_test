import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# st.title("Нужно придумать название сюда")


st.text_input("Введите длину балки в м:", help="London is a capital of great britan", placeholder="London")


st.image('edit.png', caption='Sunrise by the mountains')




# Создаем новый график
fig, ax = plt.subplots()

# Создаем прямоугольник с координатами (x, y), шириной width и высотой height
x = 1
y = 1
width = 3
height = 2
rectangle = Rectangle((x, y), width, height, edgecolor='r', facecolor='none')

# Добавляем прямоугольник на график
ax.add_patch(rectangle)

# Устанавливаем пределы осей
plt.xlim(0, 5)
plt.ylim(0, 5)

# Показываем график
plt.show()
