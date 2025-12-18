class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration 

    def __repr__(self):
        return f"'{self.title}' - {self.artist} ({self.duration}s)"

class Playlist:
    def __init__(self):
        self.songs = []

    def add_song(self, song):
        self.songs.append(song)

    def sort_by_title(self):
        self.songs.sort(key=lambda x: x.title)
        print("Đã xếp theo tên bài hát.")

    def sort_by_duration(self):
        self.songs.sort(key=lambda x: x.duration)
        print("Đã xếp theo thời lượng.")

    def show(self):
        for s in self.songs:
            print(s)
pl = Playlist()
pl.add_song(Song("Lac Troi", "Son Tung", 250))
pl.add_song(Song("Em cua ngay hom qua", "Son Tung", 230))
pl.add_song(Song("Cat Bui", "Trinh Cong Son", 300))

print("--- Danh sách gốc ---")
pl.show()

print("\n--- Xếp theo tên ---")
pl.sort_by_title()
pl.show()

print("\n--- Xếp theo thời lượng ---")
pl.sort_by_duration()
pl.show()