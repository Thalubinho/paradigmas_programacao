main :: IO ()
main = print (quickSort [9,1,8,2,5,7,3,6,4])

quickSort :: [Integer] -> [Integer]
quickSort [] = []
quickSort (x:xs) = quickSort maiores ++ pivo ++ quickSort menores 
    where
        menores = [y | y <- xs, even y && y <= x]
        maiores = [y | y <- xs, even y && y > x]
        pivo = [x | even x]
    