# # import test_module
# # print(test_module.test)


# # import turtle
# from turtle import Turtle
# from turtle import Screen

# tommy = Turtle()
# print(tommy)
# tommy.shape("turtle")
# tommy.color("DarkOrchid2")
# tommy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Hello", [1,2,3,4,5,6,7,8,9,10])
table.add_column("world", [1,2,3,4,5,6,7,8,9,10])
table.align = "r"
print(table)

