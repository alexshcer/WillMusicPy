import pyglet


def music():
    # Starting the mixer
    sound = pyglet.media.load('https://assound.netlify.app/willmusicpy/2.mp3')
    sound.play()