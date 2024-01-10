# Memoria Práctica 1 - FSI

***


- David Koschel Henríquez
- Pablo Nicolás Santana Hernández


***

### Desarrollo de la práctica

El desarrollo del código de la práctica lo fuimos haciendo a lo largo del curso. Trabajábamos en el código cada dos semanas, añadiendo lo aprendido en clase. Finalmente, a la hora de preparar la entrega rellenamos la tabla de comparaciones, copiamos el código al repositorio de GitHub y creamos este README. 

***

### Desarrollo del código

Lo primero de todo fue añadir al código base que se nos proporcionó el cálculo de nodos visitados y generados. Esto lo logramos añadiendo 2 variables, una para cada tipo de nodo.

```python
visited = 0
generated = 0
```

El valor de las variables va aumentando según se avanza en la exploración hacia el resultado. Cada vez que se visita un nodo, este se saca de la lista de estudio de posibles soluciones y se aumenta en 1 el valor de nodos visitados.

```python
node = fringe.pop()
visited += 1
```

Cuando se expande un nodo, el tamaño de la lista de nodos expandidos se suma a los nodos generados.

```python
# fringe.extend(node.expand(problem)) - Código original
expansion = node.expand(problem)
generated += len(expansion)
fringe.extend(expansion)
```


Después, se desarrolló el código para los dos nuevos algoritmos que se pedían en el enunciado de la práctica (Branch and Bound con y sin subestimación).

```python
def branch_and_bound_graph_search(problem):
    return graph_search(problem, OrderedPathList())


def branch_and_bound_subestimation_graph_search(problem):
    return graph_search(problem, OrderedSubestimationList(problem))
```

Para estos algoritmos lo único que había que programar son los dos contenedores que se iban a usar en la función principal. Para el Branch and Bound sin subestimación se creó el contenedor OrderedPathList. Este funciona igual que un stack, con la diferencia que al añadir un nodo se insertará según su **coste acumulado**, manteniendo el contenedor siempre en orden. 

```python
def append(self, item):
    for i in range(len(self.stack)):
        if item.path_cost > self.stack[i].path_cost:
            self.stack.insert(i, item)
            return
    self.stack.append(item)
```

Para el Branch and Bound con subestimación se creó el contenedor OrderedSubestimationList. Su implementación es idéntica al anterior. El único cambio es al ordenar el nodo a la hora de añadirlo, que se tiene en cuenta el coste acumulado y la **heurística** (en este caso la distancia euclídea al destino).
```python
def append(self, item):
    for i, node in enumerate(self.stack):
        if item.path_cost + self.problem.h(item) > node.path_cost + self.problem.h(node):
            self.stack.insert(i, item)
            return
    self.stack.append(item)
```

***

### Incidencias

No se presentó ninguna incidencia a lo largo del desarrollo de la práctica. La única duda que nos surgió fue si contabilizar los nodos generados que ya habían sido generados previamente, la cual resolvió el profesor durante el horario de práctica.

