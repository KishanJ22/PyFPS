import pyglet  # imports the pyglet library
from pyglet.window import key

window = pyglet.window.Window(fullscreen=True)  # creates a window
label = pyglet.text.Label('Python First Person Shooter',
                          font_name="Arial",
                          font_size=30,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')  # this specifies the text being shown, font name, text size and position of the text
enemy_image = pyglet.image.load('Images/tommy.png')  # assigns an image in the folder to the variable 'image'
enemy = pyglet.sprite.Sprite(enemy_image, x=0, y=0) # takes enemy_image, makes it a sprite and gives it a starting location
enemy.dx = 10.0 # the number of pixels the sprite will move per second

def update(dt):
    enemy.x += enemy.dx * dt
pyglet.clock.schedule_interval(update, 1/60.0) # the sprite updates at 60Hz

pyglet.clock.get_fps()
fps_display = pyglet.window.FPSDisplay(window=window)


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
    enemy.draw() # displays the enemy sprite
    fps_display.draw() # displays the live frames per second of the game


pyglet.app.run()  # runs the program
