
def add_tuples(a, b):
  return tuple(a[x]+b[x] for x in range(len(a)))

def subtract_tuples(a,b):
  return tuple(a[x]-b[x] for x in range(len(a)))

