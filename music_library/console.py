import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

album_repository.delete_all()
artist_repository.delete_all()

artist1 = Artist("Jimmy Eat World")
artist_repository.save(artist1)

artist2 = Artist("Pinegrove")
artist_repository.save(artist2)

album1 = Album("Clarity", artist1, "Rock")
album_repository.save(album1)

album2 = Album("Skylight", artist2, "Country")
album_repository.save(album2)




pdb.set_trace()
