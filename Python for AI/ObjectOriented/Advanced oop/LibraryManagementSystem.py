class Book :
    def __init__(self, title, author, price):
            self.title = title
            self.author = author
            self.price = price
            self.is_checked_out = False

    def checking_out(self):
          if not self.is_checked_out:
                self.is_checked_out = True
                return True
          return False

    def return_book(self) :
          if self.is_checked_out:
                self.is_checked_out = False
                return True
          return False
    
    def __str__(self):
          status = "checked out " if self.is_checked_out else "Available"
          return f"{self.title} is {status}"
    

class Library :
      def __init__(self,name,address) :
            self.name = name
            self.address = address
            self.books = []

      def addbooks(self, bname) :
            self.books.append(bname)
            

      def removeBook(self, bname) :
            self.books.remove(bname)

      def availableBooks(self) :
        return [b for b in self.books if not b.is_checked_out]
      
      def find_book(self, title) :
            for book in self.books:
                  if book.title == title:
                        return f"{book.title} is in {self.name} Library"

            return "Not found"      
      
Harverd = Library("Harvard", "NYC")
book1 = Book("Kafka on the shore", "Haraki murakami", 456.56)    
book2 = Book("Dancing with the shadows", "Mary A", 674.56)  

Harverd.addbooks(book1)
Harverd.addbooks(book2)

print("Available books:")
for book in Harverd.availableBooks():
    print(book)

book1.checking_out()
print("After checking out:")
for book in Harverd.availableBooks():
    print(book)

print(Harverd.find_book("Dancing with the shadows"))    




                  




    
    
                        
        