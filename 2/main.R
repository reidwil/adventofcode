x <- c(1,0,0,1,99)

for(i in 1:length(x)) {
  
  if(i == 1) {
    if(x[i] == 1) {
      opcode <- function(one, two) {
        return(one + two)
      }
    }
    if(x[i] == 2) {
      opcode <- function(one, two) {
        return(one * two)
      }
    }
    if(x[i] == 99) {
      stop('end')
    }
    adjustment_position <- x[i + 3] + 1
    if((x[i + 1]) == 0) {
      pos1 <- 1
    } else {
      pos1 <- x[i + 1]
    }
    if(x[i + 2] == 0) {
      pos2 <- 1
    } else {
      pos2 <- x[i + 2]
    }
    x[adjustment_position] <- opcode(x[pos1], x[pos2])
  }
}
