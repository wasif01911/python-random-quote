import random
def primary():
  # print("Keep it logically awesome.")

  user_input = input('Add new quotes: ')
  with open('quotes.txt', 'a') as f:
    f.write("\n" + user_input)


  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  last = len(quotes) - 1
  rndone = random.randint(0, last)
  rndtwo = random.randint(0, last)
  print(quotes[rndone], end='')
  print(quotes[rndtwo], end='')

if __name__== "__main__":
  primary()
