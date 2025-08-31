



class LibraryItem: #Super class or the basic class of the items in the library

    def __init__(self,title,author):
        self.title = title #public attribute
        self.author = author#public attribute
    
    def display(self): #public method
        print(f"LibraryItem : title:{self.title},author:{self.author}")


class Book(LibraryItem): #sub class of LibraryItem

    def display(self): #override the method in the parent class
        print(f"Book: title:{self.title}, author:{self.author}")

class Magazine(LibraryItem):  #another subclass of the parent class - LibraryItem

    def __init__(self,title,author1,issue_frequency):
        super().__init__(title,author1)  # call the super class or parent's __init__method to construct the object
        self._issue_frequency = issue_frequency #it's an private attribute


    def display(self): #override the methods in the parent class, and just change part of it.
        print(f"Magazine:  title:{self.title}, author:{self.author}, issure_frequency:{self._issue_frequency}")        



#the class which is use to contain and manage all the items in the libary.
class Library:

    def __init__(self):
        self.__all_items = [] #it's an private attribute
    

    def _add_library_item(self,item:LibraryItem): #the method which we can use to add item into the libary
        self.__all_items.append(item)
    
    def _remove_library_item(self,item:LibraryItem):#the method which we can use to remove a specific item into the libary
        self.__all_items.remove(item)
    
    def display_all_items(self): # the method which we can call to display all the items in the library
        print("-------------------")
        print("Library--all-Items: ",)
        for item in self.__all_items:
            item.display()
        
        print("-------------------")





def main():
    book = Book("peace and war","tuoersitai")
    magazine = Magazine("fashion","zzz publish company","monthly")

    library = Library()

    library._add_library_item(book)
    library._add_library_item(magazine)

    library.display_all_items()
    library._remove_library_item(book)

    library.display_all_items()



if __name__ == "__main__":
    main()

