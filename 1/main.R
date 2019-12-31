library(here)

# Fuel required to launch a given module is based on its mass. 
# Specifically, to find the fuel required for a module, take its mass, divide by three, round down, and subtract 2.
# 
# For example:
#   
# For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
# For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
# For a mass of 1969, the fuel required is 654.
# For a mass of 100756, the fuel required is 33583.


# Create a calculating function
tester_function <- function(x) {
   return(floor(as.numeric(x / 3)) - 2)
}

# Test

tester_function(100756)
# [1] 33583


# Source list of data to read in and map() the tester_function()
source(here('/1/data.R'))

# Map the function for each piece in the sourced list
sum(unlist(lapply(x, tester_function)))

# SUCCESS



# PART TWO


# So, for each module mass, calculate its fuel and add it to the total. 
# Then, treat the fuel amount you just calculated as the input mass and repeat the process, 
# continuing until a fuel requirement is zero or negative. For example:
#   
# A module of mass 14 requires 2 fuel. This fuel requires no further fuel 
# (2 divided by 3 and rounded down is 0, which would call for a negative fuel), 
# so the total fuel required is still just 2.
# At first, a module of mass 1969 requires 654 fuel. 
# Then, this fuel requires 216 more fuel (654 / 3 - 2). 216 then requires 70 more fuel, which requires 21 fuel, 
# which requires 5 fuel, which requires no further fuel. 
# So, the total fuel required for a module of mass 1969 is 654 + 216 + 70 + 21 + 5 = 966.
# The fuel required by a module of mass 100756 and its fuel is: 33583 + 11192 + 3728 + 1240 + 411 + 135 + 43 + 12 + 2 = 50346.


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
