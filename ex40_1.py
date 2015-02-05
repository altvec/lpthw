class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

putin_on_the_ritz = Song(["Why don't you go where fashion sits",
                          "Puttin' on the ritz."])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
putin_on_the_ritz.sing_me_a_song()

# See https://en.wikipedia.org/wiki/Putin_khuilo! for the reference
awesome_text = ["Putin khuilo", "la-la-la, la-la-la"]

pu_song = Song(awesome_text)
pu_song.sing_me_a_song()

