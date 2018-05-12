import csv
def loss(a, b):
  with open('./car_price.csv') as file:
    data = list(csv.reader(file))
    length = len(data)
    sumResult = 0
    result = 0
    for i in range(1, length):
      odometer = float(data[i][0])
      price = float(data[i][1])
      print((price - (a + b * odometer)) ** 2)
      sumResult += (price - (a + b * odometer)) ** 2
    result = sumResult / length
    return result
