from threading import Thread

import pyglet

screen_window = pyglet.window.Window(900, 700)


def real_playsound():
    sound = pyglet.media.load('https://assound.netlify.app/willmusicpy/2.mp3')
    sound.play()


def playsound():
    global player_thread
    player_thread = Thread(target=real_playsound)
    player_thread.start()


if __name__ == '__main__':
    playsound()
    pyglet.app.run()
