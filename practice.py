#v1
try:
    my_file = open("my_file.txt", "w")
    try:
        my_file.write("hello world")
    except Exception as e:
        print(e)
    finally:
        my_file.close()
except Exception as e2:
    print(e2)

