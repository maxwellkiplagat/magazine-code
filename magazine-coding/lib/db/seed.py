from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed():
    # Clear existing data
    from lib.db.connection import get_connection
    conn = get_connection()
    conn.execute("DELETE FROM articles")
    conn.execute("DELETE FROM authors")
    conn.execute("DELETE FROM magazines")
    conn.commit()

    # Add authors
    jk = Author(name="J.K. Rowling").save()
    orwell = Author(name="George Orwell").save()

    # Add magazines
    wizard = Magazine(name="Wizarding World", category="Fantasy").save()
    dystopia = Magazine(name="Dystopian Review", category="Science Fiction").save()

    # Add articles
    Article(title="Hogwarts Legacy", author_id=jk.id, magazine_id=wizard.id).save()
    Article(title="1984 Analysis", author_id=orwell.id, magazine_id=dystopia.id).save()
    print("Seeded test data.")

if __name__ == '__main__':
    seed()
