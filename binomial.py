import math

n = 4  # Number of trials
x = 4   # Number of successes
p = 1/7  # Probability of success

# Calculate the binomial coefficient (nCx)
nCx = math.comb(n, x)

# Calculate the probability using the binomial formula
probability = nCx * (p ** x) * ((1 - p) ** (n - x))

formatted_probability = "{:.8f}".format(probability * 100)

# Print the result
print("Probability: " + formatted_probability + "%")

print("1 in :" + str(1/probability))
