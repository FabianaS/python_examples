# Este archivo contiene algunos ejemplos de uso de estructuras de control en python
class InsaneMatrix:
    
    __matrix = []
    
    def __init__(self, columns, rows):
        if columns > 0 and rows > 0:
            self.__create_matrix(columns, rows)
        return
    
    def __create_matrix(self,columns, rows):
        for row in range(0, rows):
            self.__matrix.append([])
            for column in range(0, columns):
                self.__matrix[row].append(0)
        return
    
    def as_text(self):
        for row in range(0, len(self.__matrix)):
            print(self.__matrix[row])
        return
    
m = InsaneMatrix(8,8)
m.as_text()
