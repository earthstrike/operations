#!/usr/bin/env python3

EXPR_HEADER = "global y;"
global y


class Graph:
    def __init__(self, x_space, y_space):
        self.x_space = x_space
        self.y_space = y_space
        self.inner_list = []

        for i in range(x_space):
            self.inner_list.append(["."] * y_space)

    def __getitem__(self, item):
        return self.inner_list[item]

    def display(self):
        refor = []
        for i in range(self.x_space):
            refor.append(list(map(lambda x: x[i], self.inner_list)))

        refor = refor[::-1]
        wideboiness = 1
        for index, a in enumerate(refor):
            print(str(len(refor) - 1 - index) + ":\t", end="")
            for b in a:
                print(str(b) + " " * (wideboiness + len(str(b)) - 1), end="")
            print()


def plot(expression: str, space: [int, int], start: int, end: int, step: int):
    x_space, y_space = space
    graph = Graph(x_space, y_space)
    for x in range(start, end, step):
        global y
        exec(EXPR_HEADER + expression)
        try:
            if int(y) != y:
                continue
            graph[x][int(y)] = "/"
        except IndexError:
            pass  # Doesn't matter
    graph.display()


expression = input("Graph Equation: ")
dim_x, dim_y = input("Graph Size: ").replace(" ", "").split(",")
dim_x = int(dim_x)
dim_y = int(dim_y)
start = int(input("Start: "))
end = int(input("End: "))
step = int(input("Step: "))
plot(expression, (dim_x, dim_y), start, end, step)
