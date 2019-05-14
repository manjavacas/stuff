
-- Implementacion de arbol n-ario de enteros y operaciones sobre este
-- Antonio.Manjavacas

data Arbol = Nil | Nodo Int [Arbol] deriving(Show,Eq)

-- Sumar valores de los nodos
sumar :: Arbol -> Int
sumar (Nil) = 0
sumar (Nodo n l) = n + sumarLista l

sumarLista :: [Arbol] -> Int
sumarLista [] = 0
sumarLista (x:xs) = sumar x + sumarLista xs

-- Ocurrencia de elemento en el arbol
buscar :: Int -> Arbol -> Bool
buscar e (Nil) = False
buscar e (Nodo n l) = e == n || buscarLista e l

buscarLista :: Int -> [Arbol] -> Bool
buscarLista e [] = False
buscarLista e (x:xs) = buscar e x || buscarLista e xs

-- Numero de hojas del arbol
numHojas :: Arbol -> Int
numHojas (Nil) = 0
numHojas (Nodo n []) = 1
numHojas (Nodo n (x:xs)) = numHojasLista (x:xs)

numHojasLista :: [Arbol] -> Int
numHojasLista [] = 0
numHojasLista (x:xs) = numHojas x + numHojasLista xs

-- Numero de nodos del arbol
numNodos :: Arbol -> Int
numNodos (Nil) = 0
numNodos (Nodo n []) = 0
numNodos (Nodo n (x:xs)) = 1 + numNodosLista (x:xs)

numNodosLista :: [Arbol] -> Int
numNodosLista [] = 0
numNodosLista (x:xs) = numNodos x + numNodosLista xs

-- Profundidad del arbol
prof :: Arbol -> Int
prof (Nil) = 0
prof (Nodo n l) = 1 + profLista l

profLista :: [Arbol] -> Int
profLista [] = 0
profLista (x:xs) = max (prof x) (profLista xs)

-- Recorrido preorden
preorden :: Arbol -> [Int]
preorden (Nil) = []
preorden (Nodo n l) = n : preordenLista l

preordenLista :: [Arbol] -> [Int]
preordenLista [] = []
preordenLista (x:xs) = (preorden x) ++ (preordenLista xs)

-- Recorrido postorden
postorden :: Arbol -> [Int]
postorden (Nil) = []
postorden (Nodo n l) = postordenLista l ++ [n]

postordenLista :: [Arbol] -> [Int]
postordenLista [] = []
postordenLista (x:xs) = (postordenLista xs) ++ (postorden x)

-- Menor valor
menor :: Arbol -> Int
menor (Nil) = error("Null")
menor (Nodo n l) = minimum (preorden (Nodo n l))

-- Mayor valor
mayor :: Arbol -> Int
mayor (Nil) = error("Null")
mayor (Nodo n l) = maximum (preorden (Nodo n l))

-- Arbol de ejemplo
miArbol :: Arbol
miArbol = Nodo 5 [
            Nodo 2 [ 
                Nodo 9 [] 
            ],
            Nodo 3 [
                Nodo 0 [], Nodo 4 [], Nodo 6 [], Nodo 1 []
            ],
            Nodo 1 [ 
                Nodo 7 [], Nodo 4 [], Nodo 1 [] 
            ]
        ]

