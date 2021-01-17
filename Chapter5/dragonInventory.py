def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item not in inventory:
            inventory.setdefault(item, 1)
        else:
            inventory[item] += 1
    return inventory

def displayInventory(inventory):
    print('Inventory:')
    totalItems = 0
    for k, v in inventory.items():
        totalItems += v
        print(str(v) + ' ' + k)
    print('Total number of items: ' + str(totalItems))

currentInventory = {'gold coin': 42, 'rope': 1,}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
currentInventory = addToInventory(currentInventory, dragonLoot)

displayInventory(currentInventory)