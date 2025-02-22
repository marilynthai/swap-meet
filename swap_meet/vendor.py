from pickle import FALSE

class Vendor:
    def __init__(self,inventory = None):
        if inventory is None:
            inventory = []
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return FALSE
    
    def get_by_category(self,category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items
    
    
    def swap_items(self,other_vendor,my_item,their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.add(other_vendor.remove(their_item))
            other_vendor.add(self.remove(my_item))
            return True
        return False

    
    def swap_first_item(self,other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        else:
            self.inventory.insert(0,other_vendor.inventory.pop(0))
            other_vendor.inventory.insert(0,self.inventory.pop(1))
            return True
    

    def get_best_by_category(self,category):
        if self.inventory:
            category_included = False
            for item in self.inventory:
                if item.category == category:
                    category_included = True
            if category_included == True:
                return max(self.get_by_category(category), key=lambda item: item.condition)
    
    def swap_best_by_category(self,other,my_priority,their_priority):
        if self.get_best_by_category(their_priority) and other.get_best_by_category(my_priority):
            self.swap_items(other,self.get_best_by_category(their_priority),other.get_best_by_category(my_priority))
            return True
        return False
    
    def get_newest(self):
        return max(self.inventory, key=lambda item: item.year_created)

    def swap_by_newest(self,other):
        self.swap_items(other,self.get_newest(),other.get_newest())

        
    