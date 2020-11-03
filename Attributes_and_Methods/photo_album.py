import math


class PhotoAlbum:
    pages: int
    photos: [list]

    def __init__(self, pages: int):
        self.pages = pages
        self.photos = [ [] for _ in range(pages)]  # empty matrix with numer of sub_lists = len(self.pages)

    @classmethod
    def from_photos_count(cls, photos_count: int):
        pages = math.floor(photos_count / 4)
        return cls(pages)

    def add_photo(self, label: str):
        for page in range(self.pages):
            if len(self.photos[page]) < 4:
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {len(self.photos[page])}"
                break
        else:
            return "No more free spots"

    def display(self):
        output = f'{"-" * 11}\n'
        for page in range(self.pages):
            output += f'{" ".join(["[]" for _ in range(len(self.photos[page]))])}\n{"-"*11}\n'
        return output


album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())
