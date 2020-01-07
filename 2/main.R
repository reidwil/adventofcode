# Step One

# Read in data
x <- c(1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,9,1,19,1,9,19,23,1,23,5,27,2,27,10,31,1,6,31,35,1,6,35,39,2,9,39,43,1,6,43,47,1,47,5,51,1,51,13,55,1,55,13,59,1,59,5,63,2,63,6,67,1,5,67,71,1,71,13,75,1,10,75,79,2,79,6,83,2,9,83,87,1,5,87,91,1,91,5,95,2,9,95,99,1,6,99,103,1,9,103,107,2,9,107,111,1,111,6,115,2,9,115,119,1,119,6,123,1,123,9,127,2,127,13,131,1,131,9,135,1,10,135,139,2,139,10,143,1,143,5,147,2,147,6,151,1,151,5,155,1,2,155,159,1,6,159,0,99,2,0,14,0)

# Function - make sure I'm not using value 0
opcode_machine <- function(data) {
  
  i <- 1
  op <- data[i]
  while(op != 99) {
    
    seq1 <- data[data[i + 1] + 1]
    seq2 <- data[data[i + 2] + 1]
    pos  <- data[i + 3] + 1
    
    if(op == 1) {
      paste0()
      data[pos] <- seq1 + seq2
    } else if(op == 2) {
      data[pos] <- seq1 * seq2
    } else {
      break
    }
    
    i <- i + 4
    op <- data[i]
  }
  
  print(data)
  
}

# Test and make sure I've got the right answer
opcode_machine(x)


