from db.run_sql import run_sql

from models.artist import Artist
from models.album import Album


def save(artist):
    sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
    values =[artist.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    artist.id = artist
    return artist


def delete_all():
    sql = "DELETE FROM artists"
    run_sql(sql)


def select(id):
    artist = None
    sql = "SELECT * FROM artists WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        artist = User(result['name'], result['id'])
    return artist

def select_all():
    artists = []
    sql = "SELECT * FROM artists"
    results = run_sql(sql)
    for row in results:
        artist = Artist(row["name"], row['id'])
        artists.append(artist)
    return artist


# Extensions


def albums(artist):
    albums = []

    sql = "SELECT * FROM albums WHERE user_id = %s"
    values = [user.id]
    results = run-sql(sql, values)

    for row in results:
        album = Album(row['description'], artist, row['genre'], row['id'])
        albums.append(album)
    return album


def delete(id):
    sql = "DELETE FROM artistsWHERE id = %s"
    values = [id]
    run_sql(sql, values)


def update(artist):
    sql = "UPDATE artists SET (name) = (%s) WHERE id = %s"
    values = [artist.name, artist.id]
    run_sql(sql, values)
