# #func1
# def identification(name):
#     print("You are ")
#
#     if name == "Yu":
#         print("an author.")
#     else:
#         print("a student.")
#
#
# name = input("Enter your name: ")
# identification(name)

# #func2
# def identification(name):
#     print("You are ")
#
#     if name == "Yu":
#         result = "an author."
#     else:
#         result = "a student."
#     return result
#
#
# name = input("Enter your name: ")
# print(identification(name))

# func3
def identification(name):
    print("You are ")

    if name == "Yu":
        result = "an author."
    else:
        result = "a student."
    return result


def status(result):
    print(result)



user_name = input("Enter your name: ")
status(identification(user_name))