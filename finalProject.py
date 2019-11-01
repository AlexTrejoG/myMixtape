# -------------------------------------
#       Names: Denelis & Alex Trejo            
#    Filename: finalProject.py
#        Date: August 3, 2018
#
# Description: creates playlist based
# on genre that spells out user's name
#
# Attributions: http://paletton.com/
# --------------------------------------


import random
import webbrowser
from graphics import *

class Song:
    def __init__ (self, title, artist, url):
        self.title = title
        self.artist = artist
        self.url = "spotify:track:" + url

    def play(self):
        
        webbrowser.open(self.url)


    def print(self, y, win):
        title = Text(Point(220, 160 + 35 * y), self.title + "  ▶︎")
        title.setStyle("bold")
        title.draw(win)
        artist = Text(Point(220, 175 + 35 * y), self.artist)
        artist.setTextColor("#4D4D4D")
        artist.draw(win)
        self.playbutton = Rectangle(Point(title.getAnchor().getX() + 1.5*len(self.title), 165 + 35 * y), Point(title.getAnchor().getX() + 3* len(self.title) + 15,153 + 35 * y))       

def hipHopGenre():
    file = open("hipHopGenre.csv", "r")
    songParts = file.readlines()

    alpha_songs = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        alpha_songs[letter] = []


    for line in songParts:
        line = line.strip()
        line = line.split(",")

        song = Song(line[0], line[1], line[2])


        alpha_songs[song.title[0]].append(song)
    

    return alpha_songs

def altGenre():
    file = open("altGenre.csv", "r")
    songParts = file.readlines()

    alpha_songs = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        alpha_songs[letter] = []


    for line in songParts:
        line = line.strip()
        line = line.split(",")

        song = Song(line[0], line[1], line[2])


        alpha_songs[song.title[0]].append(song)
    
    return alpha_songs

def popGenre():
    file = open("popGenre.csv", "r")
    songParts = file.readlines()

    alpha_songs = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        alpha_songs[letter] = []


    for line in songParts:
        line = line.strip()
        line = line.split(",")

        song = Song(line[0], line[1], line[2])


        alpha_songs[song.title[0]].append(song)

    return alpha_songs

def latinGenre():
    file = open("latinGenre.csv", "r")
    songParts = file.readlines()

    alpha_songs = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        alpha_songs[letter] = []


    for line in songParts:
        line = line.strip()
        line = line.split(",")

        song = Song(line[0], line[1], line[2])


        alpha_songs[song.title[0]].append(song)

    return alpha_songs


def popPunkGenre():
    file = open("popPunkGenre.csv", "r")
    songParts = file.readlines()

    alpha_songs = {}
    for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        alpha_songs[letter] = []


    for line in songParts:
        line = line.strip()
        line = line.split(",")

        song = Song(line[0], line[1], line[2])


        alpha_songs[song.title[0]].append(song)

    return alpha_songs


def peterGenre():
    
    file = open("peter.csv", "r")
    songParts = file.readlines()

    alpha_songs = {}
    for letter in "PETRMDIOS":
        alpha_songs[letter] = []


    for line in songParts:
        line = line.strip()
        line = line.split(",")

        song = Song(line[0], line[1], line[2])


        alpha_songs[song.title[0]].append(song)

    return alpha_songs


        
def nameWindow():

    win = GraphWin("name", 440, 640)
    block = Image(Point(220,320), "background.gif")
    block.draw(win)

    text = Text(Point(220, 80), "Enter Name")
    text.setSize(18)
    text.setStyle("bold")
    text.draw(win)

    nameBar = Entry(Point(220,120), 35)
    nameBar.setFill("white")
    nameBar.draw(win)

    
    while win.checkKey() != "Return":
        pass

    inputName = nameBar.getText()

    win.close()
    
    return inputName


def genreWindow():

    win = GraphWin("genre", 440, 640)
    block = Image(Point(220,320), "background.gif")
    block.draw(win)
    
    
    hipHop = Rectangle(Point(40,40), Point(200, 200))
    block = Image(Point(120,120), "hipHop.gif")
    block.draw(win)
    text = Text(Point(120, 120), "Hip-Hop")
    text.setSize(35)
    text.setFace("courier")
    text.setTextColor("white")
    text.draw(win)

    alt = Rectangle(Point(240,40), Point(400, 200))
    block = Image(Point(320,120), "alt.gif")
    block.draw(win)
    text = Text(Point(320, 120), "Alternative")
    text.setSize(30)
    text.setFace("times roman")
    text.setTextColor("white")
    text.draw(win)

    pop = Rectangle(Point(40,240), Point(200, 400))
    block = Image(Point(120,320), "pop.gif")
    block.draw(win)
    text = Text(Point(120, 320), "Pop")
    text.setSize(36)
    text.setFace("arial")
    text.setTextColor("white")
    text.draw(win)
    
    latin = Rectangle(Point(240, 240), Point(400, 400))
    block = Image(Point(320,320), "latin.gif")
    block.draw(win)
    text = Text(Point(320, 320), "Latin")
    text.setFace("helvetica")
    text.setStyle("italic")
    text.setTextColor("white")
    text.setSize(36)
    text.draw(win)

    popPunk = Rectangle(Point(40,440), Point(200, 600))
    block = Image(Point(120,520), "popPunk.gif")
    block.draw(win)
    text = Text(Point(120, 520), "Pop Punk")
    text.setSize(30)
    text.setStyle("bold")
    text.setTextColor("white")
    text.draw(win)

    pet = Rectangle(Point(240,440), Point(400, 600))
    block = Image(Point(320,520), "peter.gif")
    block.draw(win)
    text = Text(Point(320, 520), "Peter")
    text.setSize(36)
    text.setFace("times roman")
    text.setTextColor("white")
    text.draw(win)

    while (True):
        clickedPoint = win.checkMouse()
        if (clickedPoint != None):

            if (clickedPoint.getX() >= hipHop.getP1().getX() and
                clickedPoint.getX() <= hipHop.getP2().getX() and
                clickedPoint.getY() >= hipHop.getP1().getY() and
                clickedPoint.getY() <= hipHop.getP2().getY()):
                win.close()
                return hipHopGenre()
                
            elif (clickedPoint.getX() >= alt.getP1().getX() and
                clickedPoint.getX() <= alt.getP2().getX() and
                clickedPoint.getY() >= alt.getP1().getY() and
                clickedPoint.getY() <= alt.getP2().getY()):
                win.close()
                return altGenre()

            elif (clickedPoint.getX() >= pop.getP1().getX() and
                clickedPoint.getX() <= pop.getP2().getX() and
                clickedPoint.getY() >= pop.getP1().getY() and
                clickedPoint.getY() <= pop.getP2().getY()):
                win.close()
                return popGenre()

            elif (clickedPoint.getX() >= latin.getP1().getX() and
                clickedPoint.getX() <= latin.getP2().getX() and
                clickedPoint.getY() >= latin.getP1().getY() and
                clickedPoint.getY() <= latin.getP2().getY()):
                win.close()
                return latinGenre()
 
            elif (clickedPoint.getX() >= popPunk.getP1().getX() and
                clickedPoint.getX() <= popPunk.getP2().getX() and
                clickedPoint.getY() >= popPunk.getP1().getY() and
                clickedPoint.getY() <= popPunk.getP2().getY()):
                win.close()
                return popPunkGenre()

            elif (clickedPoint.getX() >= pet.getP1().getX() and
                clickedPoint.getX() <= pet.getP2().getX() and
                clickedPoint.getY() >= pet.getP1().getY() and
                clickedPoint.getY() <= pet.getP2().getY()):
                win.close()
                
                playlist = []
                name = "PETERMEDEIROS"
                song_list = peterGenre()

                for letter in name:
                    song = random.choice(song_list[letter])
                    song_list[letter].remove(song)
                    playlist.append(song)

                win = GraphWin("Playlist", 440, 640)
                block = Image(Point(220,320), "background.gif")
                block.draw(win)
                text = Text(Point(220,100), "PETER MEDEIROS")
                text.setFace("times roman")
                text.setSize(36)
                text.draw(win)
                text = Text(Point(220, 135), "PLAYLIST")
                text.setFace("courier")
                text.setSize(20)
                text.draw(win)
                line = Line(Point(172,142), Point(268,142))
                line.draw(win)
                for y in range(len(playlist)):
                    playlist[y].print(y, win)
                    
                while (True):
                    clickedPoint = win.checkMouse()
                    if (clickedPoint != None):
                        for song in playlist:
                            if (clickedPoint.getX() >= song.playbutton.getP1().getX() and
                            clickedPoint.getX() <= song.playbutton.getP2().getX() and
                            clickedPoint.getY() <= song.playbutton.getP1().getY() and
                            clickedPoint.getY() >= song.playbutton.getP2().getY()):
                                song.play()

def main():
    playlist = []
    name = nameWindow()
    no_space_name = name.replace(" ","")
    song_list = genreWindow()
    
    for letter in no_space_name.upper():
        song = random.choice(song_list[letter])
        song_list[letter].remove(song)
        playlist.append(song)

    #playlist window
    win = GraphWin("Playlist", 440, 640)
    block = Image(Point(220,320), "background.gif")
    block.draw(win)
    text = Text(Point(220,100), name.upper())
    text.setFace("times roman")
    text.setSize(36)
    text.draw(win)
    text = Text(Point(220, 135), "PLAYLIST")
    text.setFace("courier")
    text.setSize(20)
    text.draw(win)
    line = Line(Point(172,142), Point(268,142))
    line.draw(win)
    for y in range(len(playlist)):
        playlist[y].print(y, win)
        
    while (True):
        clickedPoint = win.checkMouse()
        if (clickedPoint != None):
            for song in playlist:
                if (clickedPoint.getX() >= song.playbutton.getP1().getX() and
                clickedPoint.getX() <= song.playbutton.getP2().getX() and
                clickedPoint.getY() <= song.playbutton.getP1().getY() and
                clickedPoint.getY() >= song.playbutton.getP2().getY()):
                    song.play()


main()
