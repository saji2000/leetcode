import math

n = 14  # Number of trials
x = 11   # Number of successes
p = 0.0526  # Probability of success

# Calculate the binomial coefficient (nCx)
nCx = math.comb(n, x)

# Calculate the probability using the binomial formula
probability = nCx * (p ** x) * ((1 - p) ** (n - x))

formatted_probability = "{:.11f}".format(probability * 100)

# Print the result
print("Probability: " + formatted_probability + "%")

print("1 in :" + str(1/probability))
