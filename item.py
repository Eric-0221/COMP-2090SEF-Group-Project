class Item:
    def __init__(self, item_id, name, category):
        self.__item_id = item_id
        self.__name = name
        self.__category = category
        self.__is_borrowed = False
        self.__borrower_id = None

    def get_item_id(self):
        return self.__item_id
    
    def get_name(self):
        return self.__name
    
    def get_category(self):
        return self.__category
    
    def is_borrowed(self):
        return self.__is_borrowed
    
    def borrow_item(self, student_id):
        if not self.__is_borrowed:
            self.__is_borrowed = True
            self.__borrower_id = student_id
            return True
        return False
    
    def return_item(self):
        if self.__is_borrowed:
            self.__is_borrowed = False
            self.__borrower_id = None
            return True
        return False
    
    def get_borrower(self):
        return self.__borrower_id
    
    def __str__(self):
        status = "Lent out" if self.__is_borrowed else "Can be borrowed"
        return f"ID: {self.__item_id} | {self.__name} | {self.__category} | status:{status}"