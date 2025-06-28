require(ggplot2) #install.packages("ggplot2") #para gráficos de IC
require(plyr) #install.packages("plyr") #agrupamento, nos gráficos de IC
#função que calcula intervalo de confiança para média
ic_media <- function(x, alpha) {
  x_barra = mean(x) #media amostral
  s = sd(x) #desvio padrão
  n = length(x) #tamanho da amostra
  if (n >= 30) {
    #usa-se normal
    z = qnorm(1-(alpha/2))
    erro = z*s/sqrt(n)
  } else {
    #usa-se t student, com n-1 graus de liberdade
    t = qt(1-(alpha/2), df = n-1)
    erro = t*s/sqrt(n)
  }
  c1 = x_barra-erro
  c2 = x_barra+erro
  return(data.frame(c1, c2, y=x_barra))
}
#função que gera gráficos de intervalo de confiança com alpha igual a 5%
gera.grafico.ic.exibir <- function(nome_imagem, dados, atributo.a.comparar, atributo.a.analisar){
    print(ggplot(ddply(dados, atributo.a.comparar, function(df) ic_media(df[,atributo.a.analisar], alpha=.05)),
               aes_string(x=atributo.a.comparar))
        + geom_errorbar(aes(ymax=c2, ymin=c1), size=0.8) #definindo limites
        + geom_point(aes(y=y), size=3.5) #definindo ponto central
        + ylab(atributo.a.analisar) #especificando label do eixo y
        + ggtitle(nome_imagem) #especificando titulo
  )
}

# Carregar os dados de cada jogador
jog1_data <- read.table("jog1", header = T)
jog2_data <- read.table("jog2", header = T)
jog3_data <- read.table("jog3", header = T)
dados = rbind(jog1_data, jog2_data, jog3_data)
View(dados)
dados$jogador = as.factor(dados$jogador)
gera.grafico.ic.exibir("yICs - Atividade PP 2025.1", dados, "jogador", "pontuacao")
boxplot(dados$pontuacao ~ dados$jogador)
