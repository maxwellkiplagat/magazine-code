

from lib.models.author import Author
from lib.models.magazine import Magazine

def example_queries():
    
    TFA = Author.find_by_name("TFA")
    if TFA:
        print(f"{TFA.name}'s articles:")
        for article in TFA.articles():
            print(f"- {article.title}")

        
        print(f"\nMagazines {TFA.name} has contributed to:")
        for mag in TFA.magazines():
            print(f"- {mag['name']} ({mag['category']})")

        
        if hasattr(TFA, 'topic_areas'):
            print(f"\nTopic areas for {TFA.name}:")
            for cat in TFA.topic_areas():
                print(f"- {cat}")

    
    River = Magazine.find_by_name("Things Fall Apart")
    if River:
        print(f"\nContributors to {River.name}:")
        for author in River.contributors():
            print(f"- {author['name']}")

        
        print(f"\nArticle titles in {River.name}:")
        for title in River.article_titles():
            print(f"- {title}")

        
        if hasattr(River, 'contributing_authors'):
            print(f"\nAuthors with >2 articles in {River.name}:")
            for author in River.contributing_authors():
                print(f"- {author['name']}")

    
    if hasattr(Magazine, 'magazines_with_multiple_authors'):
        print("\nMagazines with articles by at least 2 different authors:")
        for mag in Magazine.magazines_with_multiple_authors():
            print(f"- {mag['name']}")

    
    if hasattr(Magazine, 'article_counts'):
        print("\nArticle counts per magazine:")
        for row in Magazine.article_counts():
            print(f"- {row['name']}: {row['article_count']} articles")

    
    if hasattr(Author, 'top_author'):
        top = Author.top_author()
        if top:
            print(f"\nAuthor with the most articles: {top.name}")

if __name__ == '__main__':
    example_queries()
