a <- 10
a <- a* 9
a <- a %/% 9
nome  <- 'Júlio'

nomes <- list("Nome 10",1)

nome_escolhido = nomes[[1]]

bool <- FALSE
bool <- NA


idades <- c(12,14,11,23,23,24,25,11,10)

media <- function(numeros){
  soma <- 0
  for (i in seq_along(numeros)){
    soma <- soma + numeros[i]
  }
    return (soma / length(numeros))
}

media(idades)

mean(idades, na.rm = TRUE)
sd(idades, na.rm  =TRUE)
median(idades, na.rm = TRUE)
