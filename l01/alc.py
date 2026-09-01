def error(x, y):
    x_64 = float(x)
    y_64 = float(y)
    return abs(x_64 - y_64)

def error_relativo(x, y):
    x_64 = float(x)
    y_64 = float(y)

    error_relativo = abs(x_64 - y_64)/ abs(x_64)
    return error_relativo

def matricesIguales(A, B):
    error_tolerado = 1e-7
    if len(A) != len(B):
        return False
    else:
      filas = len(A)
      for fila in range(filas):
          if len(A[fila]) != len(B[fila]):
            return False
          for columna in range(len(A[fila])):
              if abs(A[fila][columna] - B[fila][columna]) > error_tolerado:
                    return False
      return True