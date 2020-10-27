class Band:

    def __init__(self, name):
        self.name = name
        self.albums = []

    def add_album(self, album):
        if album.name in map(lambda a: a.name, self.albums):
            return f"Band {self.name} already has {album.name} in their library."
        self.albums.append(album)
        return f"Band {self.name} has added their newest album {album.name}."

    def remove_album(self, album_name: str):
        album_to_be_removed = None
        for album in self.albums:
            if album.name == album_name:
                album_to_be_removed = album
                break
        if album_to_be_removed:
            if album_to_be_removed.published:
                return "Album has been published. It cannot be removed."

            self.albums.remove(album_to_be_removed)
            return f"Album {album_name} has been removed."
        return f"Album {album_name} is not found."

    def details(self):
        return '\n'.join(
            [f"Band {self.name}"] +
            [a.details() for a in self.albums]
        ) + '\n'
        # info = f"Band {self.name}\n"
        # album_details = '\n'.join([f"{album.details()}" for album in self.albums])
        # return info + album_details