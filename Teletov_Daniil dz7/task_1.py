class Matrix:
    def __init__(self, matr_list):
        self.matr_list = matr_list

    def __str__(self):
        for el in self.matr_list:
            for element in el:
                print(f"{element:4}", end="")
            print()
        return ""

    def __add__(self, other):
        for number in range(len(self.matr_list)):
            for number_2 in range(len(other.matr_list[number])):
                self.matr_list[number][number_2] = self.matr_list[number][number_2] + other.matr_list[number][number_2]
        return Matrix.__str__(self)


matric = Matrix([[-5, 2, 3], [-6, 3, 1], [1, 4, -9], [1, 3, -1]])
new_matric = Matrix([[-8, 5, 2], [-7, 4, 2], [1, 1, -2], [2, 2, -10]])
print(matric.__add__(new_matric))
