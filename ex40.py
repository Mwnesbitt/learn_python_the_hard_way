class Song(object):
  def __init__(self, lyrics): #lyrics is a list with each item being a line of the song. 
    self.lyrics = lyrics
  
  def sing_me_a_song(self):
    for line in self.lyrics:
      print(line)

happy_bday = Song(["Happy birthday", "line 2", "third and final line"])

bulls_on_parade = Song(["Something line 1", "Something line 2"])

happy_bday.sing_me_a_song()
print(happy_bday.lyrics)

bulls_on_parade.sing_me_a_song()
print(bulls_on_parade.lyrics)