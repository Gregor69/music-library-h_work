from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository


def save(album):
    sql = f"INSERT INTO albums(title, artist, genre, id) VALUE (%s, %s, %s, %s) RETURNING *"
    values = [album.title, album.artist, album.genre, album.id]
    results = (sql,values)
    id = results[0]
    album.id = id
    return album



def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)


def select(id):
    album = None
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        album = Album(result['title'], result['artist'], result['genre'], result ['id'])
    return album


def select_all():
    albums = []
    sql = "SELECT * FROM albums"
    results = run_sql(sql)
    for row in results:
        album = Album(row["title"], row["artist"], row['genre'], row['id'])
        albums.append(album)
    return album


# Extensions

# def delete(id):
#     sql = "DELETE FROM albums WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(album):
#     sql = "UPDATE alsbums SET (description, artist_id, duration, completed) = (%s, %s, %s, %s) WHERE id = %s"
#     values = [task.description, album.artist.id, album.genre, album.id]
#     run_sql(sql, values)
