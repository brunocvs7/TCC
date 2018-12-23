source('rapzero.R')

#U <- 250
#A <- 1.61
#Teq <- 375
#Tef <- 280
#Cpq <- 2090
#Cpf <- 4180
#Ff <- 0.201/1000
#Fq<- 0.5/800
#pf <- 1000
#pq <- 800
#f <- Ff*Cpf*pf
#q <- Fq*Cpq*pq
#e <- q*Teq + f*Tef

#f <- expression(Tsf - Tef - (U*A/f)*((((e - f*Tsf)/q - Tef) - (Teq - Tsf))/log(((e - f*Tsf)/q - Tef)/(Teq - Tsf))))


#funcao <- expression(Tsf - Tef - (U*A/f)*((((e - f*Tsf)/q - Tef) - (Teq - Tsf))/log(((e - f*Tsf)/q - Tef)/(Teq - Tsf))))

funcao <- expression(Tsf - 280 - (250*1.61/840.18)*((((627125.4 - 840.18*Tsf)/1045 - 280) - (375 - Tsf))/log(((627125.4 - 840.18*Tsf)/1045 - 280)/(375 - Tsf))))

Temp <- rapzero(funcao, 360, 10^-4)
