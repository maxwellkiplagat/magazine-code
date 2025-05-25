from lib.db.connection import get_connection

class Article:
    def __init__(self, id=None, title=None, author_id=None, magazine_id=None):
        self.id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id
#----------method for saving---------------
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()
        if self.id:
            cursor.execute("UPDATE articles SET title=?, author_id=?, magazine_id=? WHERE id=?", (self.title, self.author_id, self.magazine_id, self.id))
        else:
            cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", (self.title, self.author_id, self.magazine_id))
            self.id = cursor.lastrowid
        conn.commit()
        return self
#-----------method for finding by id ------------
    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE id=?", (id,))
        row = cursor.fetchone()
        return cls(id=row["id"], title=row["title"], author_id=row["author_id"], magazine_id=row["magazine_id"]) if row else None
#-----------method for finding by title ------------
    @classmethod
    def find_by_title(cls, title):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE title=?", (title,))
        rows = cursor.fetchall()
        return [cls(id=row["id"], title=row["title"], author_id=row["author_id"], magazine_id=row["magazine_id"]) for row in rows]
#-----------method for finding by author ------------
    @classmethod
    def find_by_author(cls, author_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE author_id=?", (author_id,))
        rows = cursor.fetchall()
        return [cls(id=row["id"], title=row["title"], author_id=row["author_id"], magazine_id=row["magazine_id"]) for row in rows]
#-----------method for finding by magazine -------------
    @classmethod
    def find_by_magazine(cls, magazine_id):
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM articles WHERE magazine_id=?", (magazine_id,))
        rows = cursor.fetchall()
        return [cls(id=row["id"], title=row["title"], author_id=row["author_id"], magazine_id=row["magazine_id"]) for row in rows]
