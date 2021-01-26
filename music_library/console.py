import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

# album_repository.delete_all()
# artist_repository.delete_all()


artist1 = Artist("The Clash")
artist_repository.save(artist1)

album1 = Album("London Calling", artist1, "punk")
album_repository.save(album1)

# res = artist_repository.select_all()

# print(res)

# res = album_repository.select_all()

# print(res)



pdb.set_trace()
