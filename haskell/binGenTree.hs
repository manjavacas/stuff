
-- Implementacion de un arbol binario generico
-- Antonio.Manjavacas

data BinTree a = Nil | Leaf a | Node (BinTree a) a (BinTree a) deriving(Show,Eq)

tour :: BinTree a -> [a]
tour (Nil) = []
tour (Leaf a) = [a]
tour (Node l a r) = (tour l) ++ [a] ++ (tour r)

myTree :: BinTree Char
myTree = Node(Node (Leaf 'a') 'n' (Leaf 't')) 'o' (Node (Leaf 'n') 'i' (Leaf 'o'))
