class cat_Node:

    def __init__(self, perv = None, next = None, name = None):
        self.prev = prev
        self.next = next
        self.name = name

    def __str__(self):
        return self.name

class cat_LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __str__(self):
        pass

    def add(self, cat_name):
        #Мы создаем переменную, в которой будем хранить ссылку на новый созданный узел. При его создании 
        
        newCat = cat_Node(cat_name)
        
        #Если указатель head для списка - пустой, то мы указываем нашу ссылку newCat в качестве указателя (строки 25, 26)
        if self.head is None:
            self.head = newCat
        #Иначе, если указатель уже есть, мы объявляем переменную current  и храним в нем ссылку на "Голову" нашего списка. Затем перебираем все элементы списка до тех пор, пока указатель на след. элемент не станет пустым. И добавляем в качестве пустого ссылку на новый элемент.
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newCat

CATS = cat_LinkedList()

CATS.add("Барсик")
CATS.add("Соня")
CATS.add("Гуманойд")
CATS.add("Мятка")
CATS.add("Zovich")

print(CATS.head)