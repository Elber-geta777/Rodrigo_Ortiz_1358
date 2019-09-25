#Array3D
"""
Array3D(rows, cols, depth)-> Constructor
get_num_rows()
get_num_cols()
get_num_depth()
set_item(r, c, d, value)
get_item(r, c, d)
clearing(value)
"""
class Array3D:
    def __init__(self, rows, cols, depth):
        self.__data = []
        self.__row = rows
        self.__col = cols
        self.__dept = depth
        for dept in range(depth):
            tmp = []
            for row in range(rows):
                tmp2 = []
                for col in range(cols):
                    tmp2.append(None)
                tmp.append(tmp2)
            self.__data.append(tmp)

    def to_string(self):
        print(self.__data)

    def get_num_rows(self):
        return self.__row

    def get_num_cols(self):
        return self.__col

    def get_num_depth(self):
        return self.__dept

    def set_item(self, r, c, d,  value):
        if (r>=0 and r<self.__row) and (c>=0 and c<self.__col) and (d >=0 and d < self.__dept):
            self.__data[d][r][c] = value
        else:
            print("Fuera de rango")

    def get_item(self, r, c, d):
        return self.__data[d][r][c]

    def clearing (self, value):
        for dept in range(self.__dept):
            for row in range(self.__row):
                for col in range(self.__col):
                    self.__data[dept][row][col] = value

    def lluvias(self, depth, row, col):
        data = []
        for anio in range(1985, 2019, 1):
            anio_lista = []
            archivo = xlrd.open_workbook(filename="./Precipitacion/" + str(anio) + 'Precip.xls')
            hoja = archivo.sheet_by_index(0)
            for estado in range(2, 3, 4):
                mes_lista = []
                for mes in range(1, 13):
                    mes_lista.append("%.2f" % hoja.cell_value(estado, mes))
                anio_lista.append(mes_lista)
            data.append(anio_lista)
        print(data)



