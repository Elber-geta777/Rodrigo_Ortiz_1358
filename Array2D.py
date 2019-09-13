#Array2D
"""
Array2D(rows, cols)
get_num_rows()
get_num_cols()
clearing(valor)
set_item(r, c, valor)
get_item(r, c)
"""
class Array2D:
    def __init__(self, rows, cols):
        self.__data = []
        self.__row=rows
        self.__col=cols
        for row in range(rows):
            tmp=[]
            for col in range(cols):
                tmp.append(None)
            self.__data.append(tmp)

    def to_string(self):
        print(self.__data)

    def get_num_rows(self):
        return self.__row

    def get_num_cols(self):
        return self.__col

    def get_item(self, index):
        if index >=0 and index < len(self.__data):
            return self.__data[index]
        else:
            print("Out of range")

    def clearing (self, valor):
        for row in range(self.__row):
            for col in range(self.__col):
                self.__data[row][col]=valor

    def set_item(self, r, c, value):
        if (r >= 0 and r < self.__row) and (c >= 0 and c < self.__col):
            self.__data[r][c]=value


def main():
    arreglo = Array2D(5,5)
    arreglo.to_string()
    print(f"El numero de renglones: {arreglo.get_num_rows()}")
    print(f"El numero de columnas: {arreglo.get_num_cols()}")
    arreglo.clearing(1)
    arreglo.to_string()
    arreglo.set_item(1,3,10)
    arreglo.to_string()
    

main()
