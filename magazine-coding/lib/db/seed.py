from lib.models.author import Author
from lib.models.magazine import Magazine
from lib.models.article import Article

def seed():
    
    from lib.db.connection import get_connection
    conn = get_connection()
    conn.execute("DELETE FROM articles")
    conn.execute("DELETE FROM authors")
    conn.execute("DELETE FROM magazines")
    conn.commit()

    #----------place to add authors---------
    Chinua = Author(name="chinua achebe").save()
    Thiongo = Author(name="Ngungi wa Thiong'o").save()

    #----------place to add magazines-------------
    TFA = Magazine(name="Things Fall Apart", category="Fantasy").save()
    River = Magazine(name="The River Between", category="Science Fiction").save()

    # ----------place to add articles--------------
    Article(title="Let me see you hands up", author_id=Chinua.id, magazine_id=TFA.id).save()
    Article(title="Weep not child", author_id=Thiongo.id, magazine_id=River.id).save()
    print("Success!!!")

if __name__ == '__main__':
    seed()
