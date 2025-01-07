def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the name of the item to add to shopping list: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to shopping list")
    else:
        print("Item name can't be empty")

def remove_item(shopping_list):
    item = input("Enter the name of the item to remove from shopping list: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from shopping list")
    else:
        print(f"'{item}' is not in shopping list")

def view_list(shopping_list):
    if shopping_list:
        print("Current shopping list:")
        for number, item in enumerate(shopping_list, start=1):
             print(f"{number}. {item}")
    else:
        print("Shopping list is currently empty")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            remove_item(shopping_list)
        elif choice == '3':
            view_list(shopping_list)
        elif choice == '4':
            print("Exit the shopping list manager")
            break
        else:
            print("Invalid choice ensure choice is between (1-4)")
if __name__ == '__main__':
    main()

