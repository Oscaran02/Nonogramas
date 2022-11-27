# Hecho por Oscar Pacheco y Camilo Cruz

import sys
import time
from itertools import permutations

board = []
recursiones = 0


# Saca los datos del txt, de las filas y columnas
def importBoard():
    input_path = sys.argv[1]
    input_file = open(input_path, "r+")
    split_list = input_file.read().split('\n')
    # Leyendo los datos
    dimensions = []
    rows_array = []
    cols_array = []
    for number in split_list.pop(0).split():
        if len(number) > 0:
            dimensions.append(int(number))
        # end if
    # end for
    x = 0
    while x < dimensions[1]:
        rows_array.append((split_list.pop(0)))
        x = x + 1
    # end while
    rows_array = [list(map(int, row.split(" "))) for row in rows_array]
    x = 0
    while x < dimensions[0]:
        cols_array.append((split_list.pop(0)))
        x = x + 1
    # end while
    cols_array = [list(map(int, col.split(" "))) for col in cols_array]
    input_file.close()
    # Creando el tablero
    grid = [[0 for x in range(dimensions[0])] for y in range(dimensions[1])]
    return grid, rows_array, cols_array


# end func

# Funcion para transponer la matriz
def transpose(cols_array):
    m = len(cols_array)
    nMax = DimColum(cols_array)
    n = [0 for x in range(m)]
    columnas = [[0 for x in range(nMax)] for y in range(m)]
    for i in range(len(cols_array)):
        n[i] = len(cols_array[i])
    # end for
    for i in range(m):
        x = nMax - n[i]
        y = nMax - x
        z = 0
        for j in range(x):
            columnas[i][j] = " "
            z = j
        # end for
        aux = 0
        if (y > 0):
            while aux < y:
                if (y != nMax):
                    z = z + 1
                # end if
                columnas[i][z] = cols_array[i][aux]
                aux = aux + 1
                if (y == nMax):
                    z = z + 1
                # end if
            # end while

    for i in range(nMax):
        for j in range(m):
            print(columnas[j][i], '', end=" ")
            # end for
        print()


# end for

# Funcion para imprimir filas
def printFila(rows_array, i):
    print('|', rows_array[i], end="  ")


# end func

# Function dimensiones columnas
def DimColum(cols_array):
    max = 0
    for x in range(len(cols_array)):
        if (len(cols_array[x]) > max):
            max = len(cols_array[x])
        # end if
    # end for
    return max


# end func

# Imprimir tablero
def printBoard(rows_array, cols_array):
    transpose(cols_array)
    for x in range(len(board[0])):
        print("---", end="")
    print()
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == 1):
                print(' ', end="  ")
            elif (board[i][j] == 2):
                print('X', end="  ")
            elif (board[i][j] == 0):
                print('0', end="  ")
            # end if
        # end for
        printFila(rows_array, i)
        print()
    # end for
    for x in range(len(board[0])):
        print("---", end="")
    print()
    print()
    print()


# end func

# Encuentra la primera fila con una celda vacía, de lo contrario devuelve la altura del tablero
def findVacio():
    for i in range(len(board)):
        if board[i][0] == 0:
            return i
        # end if
    return len(board)
    # end for


# end func


# Valida si el tablero se completo correctamente
def validacionFinal(rows, cols):
    # Comprueba las columnas
    original_cols = []
    single_col = []
    for x in range(len(board[0])):
        prev_white = True
        for i in range(len(board)):
            if board[i][x] == 1:
                prev_white = True
            elif board[i][x] == 2:
                if prev_white:
                    single_col.append(1)
                else:
                    single_col[len(single_col) - 1] += 1
                # end if
                prev_white = False
            # end if
        original_cols.append(single_col.copy())
        single_col.clear()
        # end for
    # end for
    if cols != original_cols:
        return False
    # end if
    # Comprueba las filas
    original_rows = []
    single_row = []
    for x in range(len(board)):
        prev_white = True
        for i in range(len(board[0])):
            if board[x][i] == 1:
                prev_white = True
            elif board[x][i] == 2:
                if prev_white:
                    single_row.append(1)
                else:
                    single_row[len(single_row) - 1] += 1
                # end if
                prev_white = False
            # end if
        original_rows.append(single_row.copy())
        single_row.clear()
        # end for
    return False if rows != original_rows else True
    # end for


# end func


# Cuenta las celdas de color negro
def contarCasillasNegras():
    black = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:
                black += 1
            # end if
        # end for
    # end for
    return black


# end func


# n es el número entero a particionar, k es la longitud de las particiones, l es el tamaño mínimo del elemento de partición
def partition(n, k, l=1):
    if k < 1:
        raise StopIteration
    # end if
    if k == 1:
        if n >= l:
            yield (n,)
        # end if
        # end if
        return
    for i in range(l, n + 1):
        for result in partition(n - i, k - 1, i):
            yield (i,) + result
        # end for
    # end for


# end func

# valida todas las celdas de color en las columnas
def validacionVertical(cols, curr_board_height):
    block_height = 0
    block = 0
    row = 0
    for col in range(len(board[0])):
        while row <= curr_board_height:
            if block == len(cols[col]) and board[row][col] == 2:
                return False
            if board[row][col] == 2:
                block_height += 1
                if block_height > cols[col][block]:
                    return False
                row += 1
            elif board[row][col] == 1:
                if block_height == 0:
                    row += 1
                elif block_height == cols[col][block]:
                    block_height = 0
                    block += 1
                    row += 1
                else:
                    return False
                # end if
            elif board[row][col] == 0:
                row += 1
            # end if
        block_height = 0
        block = 0
        row = 0
        # end while
    return True
    # end for


# ennd func

# todas las combinaciones posibles de fila con índice idx
def permutacionFilas(board_length, rows, idx):
    row_elems = len(rows[idx])
    partitions_elems_size = row_elems + 1
    first_elem = True
    row_elems_size = 0
    for x in range(len(rows[idx])):
        if not first_elem:
            row_elems_size += 1
        # end if
        row_elems_size += rows[idx][x]
    # end for
    partitions_elems = board_length - row_elems_size - row_elems + 1

    partitions = []
    for i in partition(partitions_elems, partitions_elems_size, 0):
        partitions.append(i)
    # end for
    partition_permutations_set = set()
    for i in partitions:
        partition_permutations_set.update(permutations(i))
    # end for
    partition_permutations_list = [list(ele) for ele in partition_permutations_set]
    partition_permutations_list.sort()

    possible_rows = []
    for perm in partition_permutations_list:
        poss_row = []
        first_block = True
        for n in range(row_elems):
            for cell in range(perm[n]):
                poss_row.append(1)
            # end for
            if not first_block:
                poss_row.append(1)
            # end if
            first_block = False
            for cell in range(rows[idx][n]):
                poss_row.append(2)
            # end for
        # end for
        for cell in range(perm[len(perm) - 1]):
            poss_row.append(1)
        # end for
        possible_rows.append(poss_row)
    # end for
    return possible_rows


# end func

# función recursiva solución
def resolverNonograma(rows, cols):
    # Para solamente mostrar el resulltado del nanograma y no ver el proceso, comentar la linea de abajo
    # printBoard(rows, cols)
    global recursiones  # Guarda que tan profundo se fue la función recursiva (numero de iteraciones)
    recursiones += 1
    if findVacio() == len(board):
        return True
    # end if
    for idx in range(findVacio(), len(board)):
        for row in permutacionFilas(len(board[0]), rows, idx):
            board[idx] = row
            if validacionVertical(cols, idx):
                if resolverNonograma(rows, cols):
                    return True
                # end if
                for y in range(len(board[idx])):
                    board[idx][y] = 0
                # end for
            else:
                for y in range(len(board[idx])):
                    board[idx][y] = 0
                # end for
        return False
        # end for
    # end for


# end func

# main function
if __name__ == '__main__':
    board, rows, cols = importBoard()
    printBoard(rows, cols)
    start_time = time.time()  # Toma el tiempo que demora el programa ejecutandose
    resolverNonograma(rows, cols)
    printBoard(rows, cols)
    end_time = time.time() - start_time
    output_path = "performanceResult_" + sys.argv[1]
    if validacionFinal(rows, cols):  # Comprueba si se completo el tablero correctamente
        with open(output_path, 'w+') as output_file:
            print("Tiempo de ejecucion: %s s" % end_time, file=output_file)
            print("Numero de llamadas recursivas: %d" % recursiones, file=output_file)
            print(file=output_file)
        # end with
        output_file.close()
        print("El solucionador ha resuelto el nonograma :D")
        print("Se han agregado datos al archivo", output_path)
    else:
        print("Nonograma no se resolvió correctamente :(")
    # end if
    print()
# end funcS
