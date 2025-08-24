class Book:
    def __init__(self, title, page_count):
        # set title directly
        self.title = title  
        # use the setter for validation
        self.page_count = page_count  
        # start with no author set
        self._author = None  

    # -----------------------
    # title (simple property)
    # -----------------------
    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        # Title must always be a string
        if isinstance(value, str):
            self._title = value
        else:
            print("Title must be a string")

    # -----------------------
    # page_count (must be int)
    # -----------------------
    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    # -----------------------
    # author (must be str)
    # -----------------------
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if isinstance(value, str):
            self._author = value
        else:
            print("Author must be a string")

    # -----------------------
    # turn_page method
    # -----------------------
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")
