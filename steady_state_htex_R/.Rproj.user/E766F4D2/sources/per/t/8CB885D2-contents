
rapzero <- function (f,chute, tol) {

   dif_funcao <- D(f, "Tsf")
  xn = c()
  xq = c()
  
  
  tol  <- tol

  i = 1
  
  xn[i] <- chute
  xq[i] <- (627125.4 - 840.18*xn[i])/1045
  
  while (abs(eval(funcao, list(Tsf = xn[i]))) > tol)
    
    {
    
    xn[i+1] <- xn[i] - ((eval(funcao, list(Tsf = xn[i]))/eval(dif_funcao, list(Tsf = xn[i]))))
    
    i = i+1
    
    xq[i] <- (627125.4 - 840.18*xn[i])/1045
    
    t <-list(xn, xq)
    
    }
  
  return (t)
}






