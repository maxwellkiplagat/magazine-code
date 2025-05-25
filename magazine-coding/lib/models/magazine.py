from lib.db.connection import get_connection
from lib.models.author import Author

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE magazines SET name=?, category=? WHERE id=?", (self.name, self.category, self.id))
        else:
            cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
            self.id = cursor.lastrowid
        conn.commit()
        return self
    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE id=?", (id,))
        row = cursor.fetchone()
        return cls(id=row["id"], name=row["name"], category=row["category"]) if row else None

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE name=?", (name,))
        row = cursor.fetchone()
        return cls(id=row["id"], name=row["name"], category=row["category"]) if row else None

    @classmethod
    def find_by_category(cls, category):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM magazines WHERE category=?", (category,))
        rows = cursor.fetchall()
        return [cls(id=row["id"], name=row["name"], category=row["category"]) for row in rows]
    @classmethod
    def magazines_with_multiple_authors(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.*, COUNT(DISTINCT a.author_id) as author_count
            FROM magazines m
            JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id
            HAVING author_count >= 2
        """)
        return cursor.fetchall()
    @classmethod
    def article_counts(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT m.name, COUNT(a.id) as article_count
            FROM magazines m
            LEFT JOIN articles a ON m.id = a.magazine_id
            GROUP BY m.id
        """)
        return cursor.fetchall()
    @classmethod
    def top_author(cls):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT author_id, COUNT(*) as article_count
            FROM articles
            GROUP BY author_id
            ORDER BY article_count DESC
            LIMIT 1
        """)
        row = cursor.fetchone()
        if row:
            return Author.find_by_id(row["author_id"])
        return None
    def articles(self):
        from lib.models.article import Article
        return Article.find_by_magazine(self.id)

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
        return [row["title"] for row in cursor.fetchall()]
