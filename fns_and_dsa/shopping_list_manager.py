def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

    def main():
        shopping_list =[]
        while True:
            display_menu()
            user_choice = input("Enter your choice(1-4): ")

        if user_choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f" '{item}' has been added to the list.")
        elif user_choice == "2":
            item = input("Enter the item to remove")
            if item in shopping_list:
                shopping_list.remove(item)
            print(f"'{item}' has been removed from the list.")
        else:
            print(f" '{item}' was not found")
        elif user_choice == "3":
            print(" Current shopping List:")
            if shopping_list:
            for index, item in enumerate(shopping_list, start=1):
                print (f"{index} .{item}")

            else:
                print ("THe shopping list is empty")
        elif user_choice == "4":
            print("Goodbye"

                  break

         else:
            Print("invalid code")
if __name__ =="__main__":
                  main()


