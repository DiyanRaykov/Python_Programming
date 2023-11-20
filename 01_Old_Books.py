# # # Variant 1
# # target_book = input()
# # counter = 0
# # command = input()
# # while command != "No More Books":
# #     current_book = command
# #     if current_book == target_book:
# #         break
# #     counter += 1
# #     command = input()
# # if command == "No More Books":
# #     print("The book you search is not here!")
# #     print(f"You checked {counter} books.")
# # else:
# #     print(f"You checked {counter} books and found it.")
#
# # # Variant 2
target_book = input()
counter = 0
command = input()
while command != "No More Books":
    counter += 1
    if command == target_book:
        break
    command = input()

if command == "No More Books":
    print("The book you search is not here!")
    print(f"You checked {counter} books.")
else:
    print(f"You checked {counter -1} books and found it.")

#
# # Variant 3
# target_book = input()
# counter = 0
# is_book_found = False
# command = input()
# while command != "No More Books":
#     if command == target_book:
#         is_book_found = True
#         break
#     counter += 1
#     command = input()
#
# if not is_book_found:
#     print("The book you search is not here!")
#     print(f"You checked {counter} books.")
# else:
#     print(f"You checked {counter} books and found it.")
