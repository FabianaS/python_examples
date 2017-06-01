#! /usr/bin/python3
# ------------------------------------------------------------------------------
# Author: Pedro Guzman (pedro@subvertic.com)
# Date: 25/05/2017
# ------------------------------------------------------------------------------
from random import randint


class Matrix:
    
    # --------------------------------------------------------------------------
    # VARIABLES DE INSTANCIA 
    # --------------------------------------------------------------------------
    
    __matrix = []
    __rows = 0
    __columns = 0
    
    # --------------------------------------------------------------------------
    # CONSTRUCTOR DE LA CLASE MATRIX                                           
    # --------------------------------------------------------------------------
    # Crea instancias de la clase matrix e inicializa sus dimensiones con la 
    # cantidad de filas y columnas especificadas como parametros. 
    def __init__(self, columns, rows):
        if columns > 0 and rows > 0:
            self.__matrix = self.__create_matrix(columns, rows)
            self.__rows = rows
            self.__columns = columns
    
    # --------------------------------------------------------------------------
    # METHOD CREATE MATRIX
    # --------------------------------------------------------------------------
    # Inicializ la matriz interna y asigna valores aleatorios a todas sus 
    # coordenadas. 
    def __create_matrix(self,columns, rows):
        matrix = []
        for row in range(0, rows):
            matrix.append([])
            for column in range(0, columns):
                value = randint(0,9)
                matrix[row].append(value)
        return matrix
        
    # --------------------------------------------------------------------------
    # METHOD TRANSPOSE
    # --------------------------------------------------------------------------
    # Obtiene la matriz transpuesta de la matrix interna
    def __transpose(self):
        transposed = self.__create_matrix(self.__columns, self.__rows)
        for row in range(0, len(self.__matrix)):
            for column in range(0, len(self.__matrix[row])):
                transposed[column][row] = self.__matrix[row][column]
        return transposed
                
    
    # --------------------------------------------------------------------------
    # METHOD TEXTIFY                                           
    # --------------------------------------------------------------------------
    # Obtiene una representacion de la matrix como texto. 
    def __textify(self, matrix):
        text = ''
        for row in range(0, len(matrix)):
            text += str(matrix[row])
            text += '\n'
        return text
    
    # --------------------------------------------------------------------------
    # METHOD DESC DIAGONAL                                          
    # --------------------------------------------------------------------------    
    # Recorre la diagonal descendente y crea un lista con los elementos que la
    # componen
    def desc_diagonal(self):
        diagonal = []
        for coordenate in range(0, self.__rows):
            diagonal.append(self.__matrix[coordenate][coordenate])
        return diagonal
        
    # --------------------------------------------------------------------------
    # METHOD ASC DIAGONAL                                          
    # --------------------------------------------------------------------------     
    # Recorre la matrix y genera un lista con los elementos que forman parte
    # de la diagonal ascendente.
    def asc_diagonal(self):
        diagonal = []
        for coordenate in range(0, self.__rows):
            diagonal.append(self.__matrix[self.__columns - 1 - coordenate][coordenate])
        return diagonal

    # --------------------------------------------------------------------------
    # METHOD TRANSPOSED AS TEXT                                           
    # --------------------------------------------------------------------------     
    # Obtiene una representacion de la matriz interna como texto formateado. 
    def as_text(self):
        return self.__textify(self.__matrix)
        
    # --------------------------------------------------------------------------
    # METHOD TRANSPOSED AS TEXT                                           
    # --------------------------------------------------------------------------
    # obtiene una representacion de la matriz transpuesta con texto formateado. 
    def transposed_as_text(self):
        return self.__textify(self.__transpose())
    
m = Matrix(11,11)
print('Matriz generada...')
print(m.as_text())
print('-------------------------------------------------------------------------')
print('Matriz transpuesta...')
print(m.transposed_as_text())
print('-------------------------------------------------------------------------')
print('Diagonal descendente...')
print(m.desc_diagonal())
print('-------------------------------------------------------------------------')
print('Diagonal ascendente...')
print(m.asc_diagonal())
print('-------------------------------------------------------------------------')
