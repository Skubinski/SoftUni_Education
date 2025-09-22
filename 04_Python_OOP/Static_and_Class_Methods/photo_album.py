class PhotoAlbum:
    MAX_PHOTOS = 4
    def __init__(self, pages):
        self.pages = pages
        self.photos = self.__init_photos(pages)

    def __init_photos(self, pages):
        result = []
        for _ in range(pages):
            result.append([])
        return result

    @classmethod
    def from_photos_count(cls, photos_count):
        pages = photos_count // cls.MAX_PHOTOS
        return cls(pages)

    def add_photo(self, label):
        for i in range(len(self.photos)):
            if len(self.photos[i]) < PhotoAlbum.MAX_PHOTOS:
                self.photos[i].append(label)
                return f"{label} photo added successfully on page {i + 1} slot {len(self.photos[i])}"
        return "No more free slots"

    def display(self):
        result = f"-----------\n"
        for page in self.photos:
            for photo in page:
                if len(photo) > 0:
                    result += f"[] "
            result += "\n"
            result += f"----------\n"
        return result

album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())