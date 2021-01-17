def displayInventory(inventory):
    print('Inventory:')
    totalItems = 0
    for k, v in inventory.items():
        totalItems += v
        print(str(v) + ' ' + k)
    print('Total number of items: ' + str(totalItems))

currentInventory = {'arrow': 12, 'gold coin': 42, 'rope': 1, 'torch':6, 'dagger': 1}

displayInventory(currentInventory)