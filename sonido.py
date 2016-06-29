import winsound

def play(path):
        winsound.PlaySound(path, winsound.SND_FILENAME)

cancion = 'elcondorpasa.wav'
play(cancion)