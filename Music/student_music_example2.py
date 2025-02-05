from microbit import *
import music

playtime = 0

while playtime < 4:
    for x in range(2):
        music.play(["G4:3", "G4:2", "G4:2", "G4:2", "A4:2", "A4:2", "G4:2", "F4:2", "E4:4"])
    for x in range(2):
        music.play(["E4:4", "E4:1", "E4:1", "E4:1"])
    for x in range(2):
        music.play(["D5:2", "D5:2", "B4:3", "A4:2"])
        playtime += 1