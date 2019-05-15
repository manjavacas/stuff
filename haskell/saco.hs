
type Saco a = [(a,Integer)]

add :: Eq a => a -> Saco a -> Saco a
add a [] = (a,1):[]
add a ((b,c):s) = if a==b then ((b,c+1):s) else ((b,c):add a s)

remove :: Eq a => a -> Saco a -> Saco a
remove a [] = []
remove a ((b,c):s) = if a==b then ((b,c-1):s) else ((b,c):remove a s)

isEmpty :: Saco a -> Bool
isEmpty [] = True
isEmpty (_:_) = False

saco = [('a',3), ('b', 2), ('c',1), ('d',5)]
