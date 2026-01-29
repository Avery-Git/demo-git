from model import predict

data = [-1, 0, 1, 2]
results = [predict(x) for x in data]
print(results)