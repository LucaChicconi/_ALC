# Laboratorio 2 - Transformaciones lineales

Sea T .W -> V V,W espacios vectoriales
1. T(0) -> 0
2. T(V+W) = T(V)+T(W)  Aditividad
3. T($\alpha$ V) = $\alpha$ T(V) Homogeneidad

Podemos escribir **matrices** de una transformación lineal

La matriz de la TL se compone de la transformación aplicada a los vectores de la base B , como columnas.

Con la base canónica es así:

A = $[T(e_1)|T(e_1) | ... |T(e_n)]$

Entonces una TL queda 100% determinada por dónde manda a los vectores de la base.

Las TL preservan paralelismo, puntos medios y razones sobre un segmento, etc

También manda los paralelogramos a otros paralelogramos (posiblemente aplastados)

### Geométricamente

El cuadrado unidad ( generado por e1 y e2) tiene área 1. Al aplicar A, "estiramos" sus lados, que se convierten en las columnas de A y el cuadrado pasa a ser el paralelogramo que generan:

Área del paralelogramo = $det(A)$

det(A) es el factor de escalado de la transformación

### Transformaciones geométricas de $R^n$ en $R^n$

Es una función que mueve, rota ,escala o deforma los puntos del espacio (generalmente biyectiva)

**ojo no siempre es lineal**

Isometrías -> Semejanzas -> Afines -> Homografías

- Isometrías : Preservan ángulos y distancias
- Semejanzas : preservan ángulos y las distancias todas cambiadas por el mismo factor
- Afines : Preservan paralelismo
- Homografías: hay tres puntos que están alineados y permanecen alineados despues de la transformación


### Isometría lineal

$||T(v)|| = |v|$ para todo v -> se preservan los ángulos



#### Matriz rotación

```python

from math import sin,cos
def tranf_polares(theta):
    r = ([
            [cos(theta), - sen(theta)],
            [sen(theta), cos(theta)]
        ]
    )
    return r

```
La inversa es trasponer r


#### Matriz de escalamiento

Agrandar o achicar para todos los puntos


```python

def scale_matrix(s):
    esc = ([
            [s[0], 0],
            [0, s[1]]
        ]
    )
    return esc
```

esc preserva ángulos para cualquier s!=0 pero sólo preserva longitudes cuando |s| = 1


