import pyglet  # imports the pyglet library
from pyglet.window import key

window = pyglet.window.Window()  # creates a window
label = pyglet.text.Label('Hello World',
                          font_name="911 Porscha condensed italic",
                          font_size=30,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')  # this specifies the text being shown, font name, text size and position of the text
enemy_image = pyglet.image.load('tommy.png')  # assigns an image in the folder to the variable 'image'
enemy = pyglet.sprite.Sprite(enemy_image, x=40, y=50)

@window.event
def on_key_press(symbol, mofidiers):
    if symbol == key.W:
        print("The 'W' key was pressed.")
    elif symbol == key.A:
        print("The 'A' key was pressed.")
    elif symbol == key.S:
        print("The 'S' key was pressed.")
    elif symbol == key.D:
        print("The 'D' key was pressed.")
# date: 17/09/21 - I have used Pyglet documentation to get keyboard controls working. 

@window.event
def on_draw():
    window.clear()  # displays the window
    label.draw()  # displays the text in the window
    enemy.draw()


pyglet.app.run()  # runs the program
