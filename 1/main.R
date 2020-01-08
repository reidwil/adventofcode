library(here)

# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.

# Create a calculating function
tester_function <- function(x) {
   return(floor(as.numeric(x / 3)) - 2)
}

# Source list of data to read in and map() the tester_function()
source(here('/1/data.R'))

# Map the function for each piece in the sourced list
sum(unlist(lapply(x, tester_function)))



# PART TWO


# So, for each module mass, calculate its fuel and add it to the total. 
# Then, treat the fuel amount you just calculated as the input mass and repeat the process, 
# continuing until a fuel requirement is zero or negative. 
# Create a while loop that writes the output of the code into a new variable (y) and then returns the output of the
# y value when the function reduces the initial number down to 0 or less
tester_pt_2 <- function(x) {
  y <- 0
  while(x > 0) {
  
    x <- tester_function(x)
  
    if(x > 0) {
      y <- y + x
    }
  }
  return(y)
}

# Test
lapply(100756, tester_pt_2)
# [1] 50346

# Expected outcome
sum(unlist(lapply(x, tester_pt_2)))
