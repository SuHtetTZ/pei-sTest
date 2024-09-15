from home import sum

def test_sum():
  assert sum(2,2) == 4
  assert sum(-1,1) == 0
  assert sum(-3,1) == -2
