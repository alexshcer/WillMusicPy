import pyglet


def music():
    # Loading Music
    sound = pyglet.media.load('https://assound.netlify.app/willmusicpy/2.mp3')
    sound.play()
