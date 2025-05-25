from lib.db.connection import get_connection

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

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM authors WHERE name=?", (name,))
        row = cursor.fetchone()
        return cls(id=row["id"], name=row["name"]) if row else None


    def articles(self):
        from lib.models.article import Article
        return Article.find_by_author(self.id)

    def magazines(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.* FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        return cursor.fetchall()
    def add_article(self, magazine, title):
        from lib.models.article import Article
        return Article(title=title, author_id=self.id, magazine_id=magazine.id).save()
    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT DISTINCT m.category FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            WHERE a.author_id = ?
        """, (self.id,))
        return [row['category'] for row in cursor.fetchall()]
    def contributing_authors(self):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT authors.*, COUNT(articles.id) as article_count
            FROM authors
            JOIN articles ON authors.id = articles.author_id
            WHERE articles.magazine_id = ?
            GROUP BY authors.id
            HAVING article_count > 2
        """, (self.id,))
        return cursor.fetchall()


