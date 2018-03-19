import time

def share_diagonal(x0, y0, x1, y1):
    """ Is (x0, y0) on a shared diagonal with (x1, y1)? """
    dy = abs(y1 - y0)        # Calc the absolute y distance
    dx = abs(x1 - x0)        # CXalc the absolute x distance
    return dx == dy          # They clash if dx == dy


def col_clashes(bs, c):
    """ Return True if the queen at column c clashes
         with any queen to its left.
    """
    for i in range(c):     # Look at all columns to the left of c
          if share_diagonal(i, bs[i], c, bs[c]):
              return True

    return False           # No clashes - col c has a safe placement.


def has_clashes(the_board):
    """ Determine whether we have any queens clashing on the diagonals.
        We're assuming here that the_board is a permutation of column
        numbers, so we're not explicitly checking row or column clashes.
    """
    for col in range(1, len(the_board)):
        if col_clashes(the_board, col):
            return True
    return False


def permutation(n):
    import random
    rng = random.Random()   # Instantiate a generator
    t0 = time.clock()
    bd = list(range(n))     # Generate the initial permutation
    num_found = 0
    tries = 0
    while num_found < 5:
       rng.shuffle(bd)
       tries += 1
       if not has_clashes(bd):
           t1 = time.clock()
           print("Found solution {0} in {1} tries. Solve in {2:.4f}".format(bd, tries, t1-t0))
           tries = 0
           num_found += 1

permutation(4)
permutation(12)
permutation(16)
