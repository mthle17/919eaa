class Article:
    def __init__(self, title):
        self.title = title
        self.sections = []
        self.authors = []
    
    def add_section(self, content):
        section = Section(content, self)
        self.sections.append(section)
    
    def add_author(self, author):
        if isinstance(author, Author):
            self.authors.append(author)
        else:
            raise TypeError("Author must be of type Author")
    
    def __str__(self):
        author_display = ", ".join(str(author) for author in self.authors)
        section_display = "\n\n".join(str(section) for section in self.sections)
        
        return f"{self.title} ({author_display})\n\n{section_display}"

class Section:
    def __init__(self, content, article):
        self.content = content
        self.article = article

    def __str__(self):
        return self.content 

class Author:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name 

    def __str__(self):
        return self.name 


aut1 = Author("John Doe")
aut2 = Author("Jane Doe")

art1 = Article("Associations in Python")
art1.add_author(aut1)
art1.add_author(aut2)
art1.add_section("This is a short story of associations in Python.")
art1.add_section("It shows a difference between aggregations and compositions.")

art2 = Article("Exceptions in Python")
art2.add_author(aut2)
art2.add_section("This is another short story.")

print("-" * 25)
print(art1)
print("-" * 25)
print(art2)
print("-" * 25)
