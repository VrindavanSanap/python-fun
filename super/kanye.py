class Portishead:
  def __init__(self):
    print(f"Portishead")


class KanyeWest(Portishead):
  def __init__(self):
    print('Kanye West')
    #Portishead.__init__(self)
    super().__init__()

class ASAPRockey(Portishead):
  def __init__(self):
    print('A$AP Rocky')
    super().__init__()

class ASAPSebby(ASAPRockey, KanyeWest):
  def __init__(self):
    print('A$AP Sebby')
    super().__init__()

sebby = ASAPSebby()

# Using super() solves the diamond problem
