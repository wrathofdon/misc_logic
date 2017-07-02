primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

noSumOfPrimes = [True] * 198
rejectedProducts = set()
possibleReject = set()
redundantProducts = []
possibleProducts = {}
factorDict = {}

def findFactors(product):
  if product in factorDict:
    return(factorDict[product])
  pairs = []
  good = 0
  bad = 0
  for ii in range(2, int(product ** .5) + 1):
    if not product % ii:
      pairs.append((ii, int(product / ii)))
      sum = ii + int(product / ii)
      if noSumOfPrimes[ii + int(product / ii)]:
        good += 1
      else:
        bad += 1
  factorDict[product] = (pairs, good, bad)
  return(pairs, good, bad)

def findPairs(total):
  pairs = []
  products = []
  for ii in range(2, int(total / 2) + 1):
    pairs.append([ii, total - ii])
    products.append(ii * (total - ii))
  return(pairs, products)

def checkGood(number):
  a, b, c = findFactors(number)
  return(b == 1 and c > 0)


for i in range(len(primes)):
  for j in range(i, len(primes)):
    rejectedProducts.add(primes[i] * primes[j])
    noSumOfPrimes[primes[i] + primes[j]] = False


for i in range(5, 199):
  possible = []
  if noSumOfPrimes[i]:
    pairs, products = findPairs(i)
    for j in range(len(pairs)):
      if checkGood(products[j]):
        possible.append(pairs[j])
    if len(possible) == 1:
      product = possible[0][0] * possible[0][1]
      total = possible[0][0] + possible[0][1]
      print("Answer: ", possible[0][0], possible[0][1])
      print("Product Sees: ", product)
      print("  which has possibilities of: ", findFactors(product)[0])
      print("Sum Sees: ", total)
      print("  which has possibilities of: ", findPairs(total)[0])
