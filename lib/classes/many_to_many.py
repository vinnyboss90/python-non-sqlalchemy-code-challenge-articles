class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Invalid article title")
        self._author = author
        self._magazine = magazine
        self._title = title
        author.articles().append(self)
        magazine.articles().append(self)

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))


class Magazine:
    def __init__(self, name, category):
        assert isinstance(name, str) and 2 <= len(name) <= 16
        assert isinstance(category, str) and len(category) > 0
        self.name = name
        self.category = category
        self.articles_published = []

    def articles(self):
        return self.articles_published

    def contributors(self):
        authors = [article.author for article in self.articles_published]
        return list(set(authors))

    def article_titles(self):
        return [article.title for article in self.articles_published]

    def contributing_authors(self):
        author_counts = {}
        for article in self.articles_published:
            author_name = article.author.name
            author_counts[author_name] = author_counts.get(author_name, 0) + 1
        return [author for author, count in author_counts.items() if count > 2]