import pyglet  # imports the pyglet library

window = pyglet.window.Window()  # creates a window
label = pyglet.text.Label('Hello World',
                          font_name="911 Porscha condensed italic",
                          font_size=30,
                          x=window.width // 2, y=window.height // 2,
                          anchor_x='center',
                          anchor_y='center')  # this specifies the text being shown, font name, text size and position of the text
image = pyglet.resource.image('ps.png')  # assigns an image in the folder to the variable 'image'


@window.event
def on_draw():
    window.clear()  # displays the window
    label.draw()  # displays the text in the window
    image.blit(10, 10)  # displays the image with (x,y) sizing in the window


pyglet.app.run()  # runs the program
