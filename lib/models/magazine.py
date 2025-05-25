from db.connection import get_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category

    def contributors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT authors.* FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
        """, (self.id,))
        return cursor.fetchall()

    def article_titles(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT title FROM articles WHERE magazine_id=?", (self.id,))
        return [row['title'] for row in cursor.fetchall()]
