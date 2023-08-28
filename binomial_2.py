import math

n = 29  # Number of trials
x = 4  # Number of successes
p = 0.0526  # Probability of success

# Calculate the binomial coefficient (nCx)
nCx = math.comb(n, x)

# Calculate the probability using the binomial formula
probability = nCx * (p**x) * ((1 - p) ** (n - x))

formatted_probability = "{:.11f}".format(probability * 100)

# Print the result
print("Probability: " + formatted_probability + "%")

print("1 in :" + str(round(1 / probability)))

log = math.log(1 / probability, 2)

print("Similar to tossing a coin", round(log), "times and getting only heads")

log = math.log(1 / probability, 6)

print("Similar to tossing a dice", round(log), "times and getting only 6")
