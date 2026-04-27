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
