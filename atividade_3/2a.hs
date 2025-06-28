main :: IO ()
main = print (situacaoAluno 0.74 10 10)

situacaoAluno :: Double -> Double -> Double -> String
situacaoAluno freq u1 u2
    | freq < 0.75  = "Reprovado por falta!"
    | media >= 7 = "Aprovado por media!"
    | media >= 4 = "Na final!"
    | media < 4 = "Reprovado por nota!"
    where media = (u1 + u2)/2

