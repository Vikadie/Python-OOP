class Album:

    def __init__(self, name: str, *args):
        self.name = name
        self.songs = list(args)
        self.published = False

    def add_song(self, song):
        if self.published:
            return f"Cannot add songs. Album is published."
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if song.name in map(lambda a: a.name, self.songs):
            return f"Song is already in the album."
        self.songs.append(song)
        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        if self.published:
            return "Cannot remove songs. Album is published."
        song_to_be_removed = [song for song in self.songs if song.name == song_name]
        if not song_to_be_removed:
            return "Song is not in the album."
        self.songs.remove(song_to_be_removed[0])
        return f"Removed song {song_name} from album {self.name}."

    def publish(self):
        if self.published:
            return f"Album {self.name} is already published."
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        info = [f"Album {self.name}"]
        song_lines = [f"== {song.get_info()}" for song in self.songs]

        return '\n'.join(info + song_lines) + '\n'