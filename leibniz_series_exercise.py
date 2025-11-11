def approximate_pi(n_terms):
    schum = 0
    for _ in  range(n_terms):
      function = ((-1)** _) / ((2* _)+1)
      schum += function 
    pi = 4* schum
    return pi
