from db.connection import get_connection

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE authors SET name=? WHERE id=?", 
                         (self.name, self.id))
        else:
            cursor.execute("INSERT INTO authors (name) VALUES (?) RETURNING id",
                         (self.name,))
            self.id = cursor.fetchone()[0]
        conn.commit()
        return self

    def articles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id=?", (self.id,))
        return cursor.fetchall()

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT magazines.* FROM magazines
            JOIN articles ON magazines.id = articles.magazine_id
            WHERE articles.author_id = ?
        """, (self.id,))
        return cursor.fetchall()
