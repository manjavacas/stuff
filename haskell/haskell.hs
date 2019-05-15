
-- Ejercicios Haskell
-- Antonio.Manjavacas

{- Abrir interprete con el comando ghci y cargar programa con el comando :l <fichero.hs> -}

{- Contador de digitos -}
count :: Int -> Int
count 0 = 0
count n = 1 + count(div n 10)

{- Suma los digitos de un numero -}
digits :: Int -> Int
digits 0 = 0
digits n = (mod n 10) + digits(div n 10)

{- Factorial -}
factorial :: Int -> Int
factorial 0 = 1
factorial n = n * factorial(n - 1)

{- Pertenencia de un entero a una lista -}
among :: Int -> [Int] -> Bool
among a [] = False
among a (x:xs)
    | a == x = True
    | otherwise = among a xs

{- Repetir n veces una cadena -}
repetir :: Int -> String -> String
repetir 0 s = []
repetir n s = s ++ repetir (n-1) s

{- Comprobar si un numero es multiplo de otro -}
esMultiplo :: Int -> Int -> Bool
esMultiplo n m
    | (mod m n) == 0 = True
    | otherwise = False

{- Sumar desde un numero hasta otro -}
sumDesdeHasta :: Int -> Int -> Int
sumDesdeHasta n m
    | n == m = n
    | otherwise = n + sumDesdeHasta (n+1) m

{- Rotar lista -}
rotar :: [Int] -> [Int]
rotar l = tail l ++ [head l]

{- Rango de una lista -}
rango :: [Int] -> [Int]
rango l = [minimum l, maximum l]

{- Reconocimiento de palindromos -}
esPalindromo :: [Int] -> Bool
esPalindromo l = l == reverse l

{- Obtener los elementos interiores de una lista -}
interiores :: [Int] -> [Int]
interiores l = tail (init l)

{- Suma de dos numeros racionales -}
formaReducida :: (Int,Int) -> (Int,Int)
formaReducida (a,b) = (a `div` c, b `div` c)
    where c = gcd a b

sumaRacional :: (Int,Int) -> (Int,Int) -> (Int,Int)
sumaRacional (a,b) (c,d) = formaReducida (a*d+b*c, b*d)

{- Sumar cuadrados de los n primeros numeros -}
sumaCuadrados :: Int -> Int
sumaCuadrados n
    | n == 0 = 0
    | otherwise = n^2 + sumaCuadrados (n-1)

{- Replicar n veces un elemento devolviendo una lista -}
replica :: Int -> a -> [a]
replica n x
    | n == 0 = []
    | otherwise = x : replica (n-1) x

{- Sumar los n primeros numeros -}
suma :: Int -> Int
suma n = sum[1..n]

{- Devuelve la linea n de un triangulo aritmetico -}
linea :: Int -> [Int]
linea n = [suma (n-1) + 1..suma n]

{- Suma de todos los multiplos de 3 o 5 menores que n -}
sumMult :: Int -> Int
sumMult n = sum[x | x <- [1..n-1], mod x 3 == 0 || mod x 5 == 0]

{- Devuelve la lista de numeros impares de una lista -}
impares :: [Int] -> [Int]
impares [] = []
impares (x:xs)
    | (mod x 2) /= 0 = x : impares xs
    | otherwise = impares xs

{- Obtener los cuadrados de los impares de una lista -}
imparesC :: [Int] -> [Int]
imparesC [] = []
imparesC (x:xs)
    | (mod x 2) /= 0 = x^2 : imparesC xs
    | otherwise = imparesC xs

{- Obtener la suma de los cuadrados de los impares de una lista -}
sumaImparesC :: [Int] -> Int
sumaImparesC [] = 0
sumaImparesC (x:xs)
    | (mod x 2) /= 0 = x^2 + sumaImparesC xs
    | otherwise = sumaImparesC xs

{- Devolver la lista de numeros entre dos dados -}
intervalo :: Int -> Int -> [Int]
intervalo a b = [a..b]

intervalo2 :: Int -> Int -> [Int]
intervalo2 a b
    | a > b = []
    | otherwise = a : intervalo2 (a+1) b

{- Obtener la lista de enteros dentro de un rango -}
entre :: Int -> Int -> [Int] -> [Int]
entre a b l = [x | x <- l, x >= a, x <= b ] 

{- Aproxima Pi -}
aproximaPi n = sqrt(6*sum[1/x^2 | x <- [1..n]])

{- Lista de elementos hasta el primero que no cumple una propiedad -}
takeWhile' :: (a -> Bool) -> [a] -> [a]
takeWhile' _ [] = []
takeWhile' p (x:xs)
    | p x = x : takeWhile' p xs
    | otherwise = []

{- Aplanar lista -}
aplanar :: [[a]] -> [a]
aplanar [] = []
aplanar (x:xs) = x ++ aplanar xs

{- Eliminar elemento de lista -}
elimina :: Eq b => b -> [b] -> [b]
elimina _ [] = []
elimina b (x:xs)
    | x /= b = x : elimina b xs
    | otherwise = elimina b xs

{- Suma de los cuadrados de los impares de una lista -}
sumaCuadradosImpares :: [Int] -> Int
sumaCuadradosImpares l = sum[x*x | x <- l, odd x]

sumaCuadradosImpares2 :: [Int] -> Int
sumaCuadradosImpares2 [] = 0
sumaCuadradosImpares2 (x:xs)
    | odd x = x*x + sumaCuadradosImpares2 xs
    | otherwise = sumaCuadradosImpares2 xs

{- Lista con los numeros entre m y n -}
entreL :: Int -> Int -> [Int]
entreL m n = [m..n]

{- Pertenencia a una lista -}
isMember :: Int -> [Int] -> Bool
isMember n [] = False
isMember n (x:xs)
    | n == x = True
    | otherwise = isMember n xs

{- Diferencia de dos listas -}
diferencia :: [Int] -> [Int] -> [Int]
diferencia [] _ = []
diferencia (x:xs) ys
    | isMember x ys = diferencia xs ys
    | otherwise = x : diferencia xs ys

{- Sumar impares menores que n -}
sumaImparesHasta :: Int -> Int
sumaImparesHasta 0 = 0
sumaImparesHasta n = sum[x | x <- [0..n], odd x]

{- Aplicar funcion f n veces a x -}
repiteFunc :: Int -> (a -> a) -> a -> a
repiteFunc 0 _ x = x
repiteFunc n f x = repiteFunc (n-1) f (f x)

{- Definicion de posicion y movimientos en el plano -}
type Pos = (Int,Int)
data Mov = Izq | Der | Arr | Abj

origen :: Pos
origen = (0,0)

movimiento :: Mov -> Pos -> Pos
movimiento Izq (x,y) = (x-1,y)
movimiento Der (x,y) = (x+1,y)
movimiento Arr (x,y) = (x,y+1)
movimiento Abj (x,y) = (x,y-1)

movimientos :: [Mov] -> Pos -> Pos
movimientos [] p = p
movimientos (m:ms) p = movimientos ms (movimiento m p)

{- Incremento o decremento de los elementos de una tupla -}
type Tupla = (Int,Int)
data Op = Inc | Dec

incremento :: Op -> Tupla -> Tupla
incremento Inc (x,y) = (x+1,y+1)
incremento Dec (x,y) = (x-1,y-1)

{- Definicion de figuras -}
data Figura = Rectangulo Float Float | Circulo Float | Triangulo Float Float

cuadrado :: Float -> Figura
cuadrado n = Rectangulo n n

area :: Figura -> Float
area (Circulo r) = pi*r^2
area (Rectangulo m n) = m*n
area (Triangulo b h) = b*h/2

{- Invertir lista -}
invertir :: [a] -> [a]
invertir [] = []
invertir (x:xs) = (invertir xs) ++ [x]

{- Borrar las ocurrencias de y en xs -}
borra :: Int -> [Int] -> [Int]
borra _ [] = []
borra y (x:xs)
    | y == x = (borra y xs)
    | otherwise = [x] ++ (borra y xs)

