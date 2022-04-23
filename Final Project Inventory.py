### Shaheer Ur Rehman
### 231451798
### COMP 111 (Section B)
### Final Project for Inventory Management System
####################################################

class Inventory:

    def __init__(self, name, Id):
        self.invName = name
        self.invId = Id
        self.items = {}
        self.manager = None

    def addItems(self, name, price, quantity):
        if name not in self.items.keys():
            self.items[name] = Items(name, price, quantity) # composition
        else:
            self.items[name].addItems(quantity) # uses Items class object

    def removeItems(self, item, quantity):
        # if condition for the case that the item is not in inventory
        if item not in self.items.keys():
            print("This item is not in inventory")
        else:
            self.items[item].removeItems(quantity)

    def discardItem(self, item):
        if item not in self.items.keys():
            print("This item is not in inventory")
        else:
            # everything related to that item, including name price and quantity will be removed from selected
            # inventory
            self.items.pop(item)
            print("Item discarded successfully. ")

    def popZeroQuantityItem(self):
        for key in self.items:
            obj = self.items.get(key)
            # to check that which object has zero quantity
            if obj.quantity == 0:
                self.items.pop(key)
                break

    def displayItems(self):
        if len(self.items) == 0:
            print("No item in inventory")
        else:
            for key in self.items:
                e = self.items.get(key)
                e.displayItems()

    def displayTotalItems(self):
        print("Number of different type of items in this inventory:", len(self.items))
        totalItems = 0
        for key in self.items:
            e = self.items.get(key)
            totalItems += e.getQuantity()
        print("Total number of items in this inventory:", totalItems)

    def setManager(self, mngr):
        self.manager = mngr

    def displayManager(self):
        if self.manager is not None:
            self.manager.displayManager()
        else:
            print("No Manager for this inventory. Assign a manager first. ")

    def info(self): # to be used in the inherited OutletShop class with polymorphic behaviour
        return self.invName + '-' + self.invId

class Items:

    def __init__(self, name, price, quantity):
        self.itemName = name
        self.price = price
        self.quantity = quantity

    def addItems(self, quantity):
        self.quantity += quantity

    def removeItems(self, quantity):
        if quantity <= self.quantity:
            self.quantity -= quantity
            print("Items removed. ")
        else:
            print('Not enough quantity of item')

    def displayItems(self):
        print("Item Name:", self.itemName)
        print("Item Price:", self.price)
        print("Item Quantity:", self.quantity)
        print("_______________________________")

    def getQuantity(self):
        return self.quantity

class Manager:

    def __init__(self, name, Id):
        self.mngName = name
        self.mngId = Id

    def displayManager(self):
        print("Manager name:", self.mngName)
        print("Manager ID:", self.mngId)

class OutletShop(Inventory): # inheritance

    def __init__(self, invName, invId,shopName, shopId):
        super().__init__(invName, invId)
        self.shopName = shopName
        self.shopId = shopId

    def info(self):   # polymorphism
        print("Shop Name:", self.shopName)
        print("Shop ID:", self.shopId)
        print("Respective Inventory:", super().info())

class Supplier:

    def __init__(self, name, Id):
        self.supName = name
        self.supId = Id

    def supInfo(self):
        print("Supplier Name:", self.supName)
        print("Supplier ID:", self.supId)

def main():
    obj = {} # a dictionary of inventory objects
    inv = ""
    shop = ""
    suppliers = {} # a dictionary of supplier objects
    user = -2
    while user != -1:
        input("Enter anything to continue") # this makes the program stop for the user to see output before
        # displaying menu again.
        print("-1: Exit the program") # when user enters -1, program finishes to execute.
        print("0: Create new inventory") # program asks for name and id of new inventory and names the object
        # by combining both name and id. Stores this name of object and its reference in obj dictionary.
        print("1: Select an inventory") # for options 2-11, user has to first have an inventory selected and
        # to select an inventory, it has to be created first.
        print("2: Add an item") # item with its name price and quantity will be stored in selected inventory
        print("3: Remove items") # program will prompt for the name and quantity of item to be removed.
        print("4: Discard whole stock of an item") # program will prompt for the name of item to be discarded
        # from selected inventory.
        print("5: Show all items with quantity and prices") # program will display these things in the selected
        # inventory.
        print("6: Show inventory information") # program will display total items and different types of items
        # in the selected inventory.
        print("7: Display manager for inventory")
        print("8: Assign manager to selected inventory")
        print("9: Remove zero quantity items") # program will discard items whose quantity is 0.
        print("10: Create an outlet shop") # an outlet shop will be created for the selected inventory.
        print("11: Show shop information")
        print("12: Add a supplier") # supplier will be added for every inventory.
        print("13: Show all suppliers") # all suppliers will be displayed.
        # exception handling for the cases when user inputs non-integer input or invalid integer input.
        # in both cases, print statement on line 286 will be executed and user will be prompted for input again.
        try:
            user = int(input("Choose an option: "))
        except ValueError:
            print(end='')
        if user == 0:
            name = input("Give name to inventory: ")
            Id = input("Give an ID to inventory: ")
            # naming the key(objName) for dictionary entry
            objName = name + '-' + Id
            # if key not in dict
            if objName not in obj:
                # dict[key] = value
                obj[objName] = Inventory(name,Id)
                print("Inventory", objName, "created successfully. ")
            else:
                print(objName, "inventory already exists. ")
        elif user == 1:
            # in case user wants to select an inventory before creating one
            if obj == {}:
                print("No existing inventory. Create an inventory first")
            else:
                # while loop checks if selected inventory is valid
                x = False
                while not x:
                    print("Following are the names-id of existing inventories.")
                    for keys in obj:
                        print(keys, end=" ")
                    print()
                    name = input("Name of inventory to select: ")
                    Id = input("ID of inventory to select: ")
                    inv = name + '-' + Id
                    if inv not in obj:
                        print("This inventory does not exist. Enter valid name and ID. ")
                    else:
                        x = True
                print("Inventory", inv, "selected. ")
                # a new shop can be created once an inventory is selected or reselected.
                shop = ""
        elif user == 2:
            if inv == "":
                print("Select an inventory first")
            else:
                print("If the item already exists then quantity will be updated however, price will remain same")
                print("To add an item of same name with different price, mention price with item name")
                item = input("Name of item: ")
                price = float(input("Price per item: "))
                quantity = int(input("Quantity of item: "))
                obj[inv].addItems(item, price, quantity)
                print("Item added. ")
        elif user == 3:
            if inv == "":
                print("Select an inventory first")
            else:
                item = input("Name of item: ")
                quantity = int(input("Quantity to be removed: "))
                obj[inv].removeItems(item,quantity)
        elif user == 4:
            if inv == "":
                print("Select an inventory first")
            else:
                item = input("Name of item: ")
                obj[inv].discardItem(item)
        elif user == 5:
            if inv == "":
                print("Select an inventory first")
            else:
                obj[inv].displayItems()
        elif user == 6:
            if inv == "":
                print("Select an inventory first")
            else:
                obj[inv].displayTotalItems()
        elif user == 7:
            if inv == "":
                print("Select an inventory first")
            else:
                obj[inv].displayManager()
        elif user == 8:
            if inv == "":
                print("Select an inventory first")
            else:
                name = input("Enter the name of manager: ")
                Id = input("Assign an ID: ")
                mng = Manager(name, Id)
                obj[inv].setManager(mng)
                print("Manager Assigned. ")
        elif user == 9:
            if inv == "":
                print("Select an inventory first")
            else:
                obj[inv].popZeroQuantityItem()
                print("Done. ")
        elif user == 10:
            if inv == "":
                print("Select an inventory first")
            else:
                invInfo = inv.split('-')
                invName = invInfo[0]
                invId = invInfo[1]
                name = input("Enter the name of shop: ")
                Id = input("Assign an ID: ")
                # a shop named object from class outlet shop will be created
                shop = OutletShop(invName, invId, name, Id)
                print("Shop", name + '-' + Id, "opened and linked to the selected", inv, "inventory. ")
        elif user == 11:
            if inv == "":
                print("Select an inventory first")
            elif shop == "":
                print("No shop created for this inventory. Create a shop first. ")
            else:
                # show shop info as well as inventory info using polymorphism
                shop.info()
        elif user == 12:
            name = input("Enter supplier's name: ")
            Id = input("Enter supplier's ID: ")
            sup = name + '-' + Id
            if sup not in suppliers:
                # Supplier is an association class
                suppliers[sup] = Supplier(name, Id)
                print("Supplier", sup, "added successfully. ")
            else:
                print(sup, "supplier already exists. ")
        elif user == 13:
            if suppliers == {}:
                print("No suppliers. Add supplier first. ")
            else:
                print("Following are the names-id of existing suppliers.")
                for keys in suppliers:
                    print(keys, end=" ")
                print()
        # in case, user enters integer but not a valid one.
        elif (user < -1) or (user > 10):
            print("That was not a valid number. Try again!")

if __name__ == '__main__':
    main()
