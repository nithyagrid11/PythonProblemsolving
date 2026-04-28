
def get_movies(db, query, values):
    db.execute(query, values)
    return db.fetchall()

'''def get_featured_movies(db):
    db.execute("SELECT * FROM movies WHERE is_featured = TRUE")
    return db.fetchall()'''