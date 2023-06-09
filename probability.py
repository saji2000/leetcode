import math

n = 77430
log_p = 0.0

for i in range(0, 7):
    log_p += math.log(1/n)

p = math.exp(log_p)

print("p = {:.10f}".format(p))