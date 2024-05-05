import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle

# st.title("Нужно придумать название сюда")
st.text_input("Введите длину балки в м:", help="London is a capital of great britan", placeholder="London")
st.image('edit.png', caption='Sunrise by the mountains')

# Создаем новый график
fig, ax = plt.subplots()

# Создаем прямоугольник с координатами (x, y), шириной width и высотой height
x = 0
y = 0
width = 3
height = 2
rectangle = Rectangle((x, y), width, height, edgecolor='r', facecolor='none')

# Создаем круг с центром в (x, y) и радиусом radius
x = 1
y = 1
radius = 0.1
circle = Circle((x, y), radius, edgecolor='b', facecolor='none')

# Добавляем прямоугольник на график
ax.add_patch(rectangle)

# Добавляем круг на график
ax.add_patch(circle)

# Устанавливаем пределы осей
plt.xlim(-1, 7)
plt.ylim(-1, 5)

# Показываем график
st.pyplot(plt)
