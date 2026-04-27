# #v1
# try:
#     my_file = open("my_file.txt", "w")
#     try:
#         my_file.write("hello world")
#     except Exception as e:
#         print(e)
#     finally:
#         my_file.close()
# except Exception as e2:
#     print(e2)

#v2
# with open("hello_1.txt", "w") as test_file:
#     test_file.write("hello worldddd")
#
# with open("hello_1.txt", "a") as test_file:
#     test_file.write("\nhello worldik")
#
# with open("hello_1.txt", "a") as test_file:
#     test_file.write("\nhwwwwwwwwwwk")

# with open("hello_1.txt", "r") as myfile:
    #1
    #print(test_read_file.read()) - вариант если файл маленький и мало читать.
    #2
    # result = myfile.readline()
    # print(result)
    # result2 = myfile.readline(5) - read by lines
    # print(result2)
    #3
    # result = myfile.readlines() - вывод всего содержимого в массив
    # print(result)
    #4
    # for line in myfile:
    #     print(line, end="") построчно читаем циклом файл
    #5
    # line = myfile.readline()
    # while line:
    #     print(line, end="")
    #     line = myfile.readline() тоже с циклом просто ридлайн функция

##########################
# FILENAME = 'notes.txt'
# NOTES_COUNT = 3
#
# notes = []
#
# for i in range(NOTES_COUNT):
#     notes.append(input(f"Enter note {i+1}: ").strip())
#
# with open(FILENAME, "a") as file:
#     for i in range(NOTES_COUNT):
#         file.write(f"{i + 1}. {notes[i]}\n")
#
# with open(FILENAME, "r") as file:
#     print(file.read())

####
# import pickle
# FILENAME = "notes.dat" #сохранение файла в байтовый код
#
# users = [
#     ["John", "123456789"],
#     ["Peter", "987654321"],
#     ["Vasya", "1568654156"]
# ]
#
#
# with open(FILENAME, "wb") as file: #запись байтов с помощью 'wb'
#     pickle.dump(users, file)  # серіалізація (процесс переделывания объекта в байткод)
#
#
# with open(FILENAME, "rb") as file: #читание байтов
#     users_from_file = pickle.load(file)  # десеріалізація (переворачиваем байткод в приемлемый для человека)
#     for user in users_from_file:
#         print(f"Name: {user[0]} Phone: {user[1]}")

#
# import shelve
#
# FILENAME = "notes"
#
# with shelve.open(FILENAME) as users:
#     users["John"] = "123456789"
#     users["Peter"] = "987654321"
#     users["Vasya"] = "1568654156"
#
# with shelve.open(FILENAME) as users:
#     users["Petya"] = "12312341234123"
#     print(users["Petya"])
#     print(users["John"])
#
#     for key in users:
#         print(f"{key} - {users[key]}")
#
#     print(users)
#     users.pop("John", "not found")
#
#     print("-" * 10)
#
#     for key in users:
#         print(f"{key} - {users[key]}")
#

# import csv
#
# FILENAME = "users.csv"
#
# users = [
#     {"name": "user1", "phone": "111"},
#     {"name": "user2", "phone": "222"},
#     {"name": "user3", "phone": "3333"},
# ]
#
# with open(FILENAME, "w", newline="") as csvfile:
#     columns = ["name", "phone"]
#     writer = csv.DictWriter(csvfile, fieldnames=columns, delimiter=";") #берем контент из словаря и записываем в формат csv
#     writer.writeheader() # названия колонок
#
#     writer.writerows(users) #сохраняет в себе словари (множество(
#
#     user: dict = {"name": "Kate", "phone": "+222333"}
#     writer.writerow(user) #одна строчка
#
# with open(FILENAME, "r", newline="") as csvfile:
#     reader = csv.DictReader(csvfile, delimiter=";")
#     for row in reader:
#         print(row["name"], " --> ", row["phone"])

##
##
# import os
# #
# # os.mkdir("test_folder") слздает папку
# #
# # os.rmdir("test_folder") удаляет папку
#
# file_name = "my_file.txt"
# if os.path.exists(file_name): #она вернет тру если файл есть, а если нет - фолс
#     os.remove(file_name)
#     print("File removed!")
# else:
#     print("File not found!")