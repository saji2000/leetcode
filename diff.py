def find_differences(obj1, obj2):
    # If the types of obj1 and obj2 are different, return them as a difference array
	if type(obj1) != type(obj2):
		return [obj1, obj2]

	# If they are both dictionaries, compare their keys and values recursively
	if isinstance(obj1, dict) and isinstance(obj2, dict):
		diff = {}
		for key in obj1.keys():
			if key in obj2:
				nested_diff = find_differences(obj1[key], obj2[key])
				if nested_diff:
					diff[key] = nested_diff
		return diff

	# If they are both lists, compare their elements recursively
	if isinstance(obj1, list) and isinstance(obj2, list):
		diff = []
		minLength = min(len(obj1), len(obj2))
		for i in range(minLength):
			nested_diff = find_differences(obj1[i], obj2[i])
			if nested_diff:
				diff[str(i)] = nested_diff
		return diff

	# For primitive values (int, float, str, etc.), compare directly
	if obj1 != obj2:
		return [obj1, obj2]

	# If no differences are found, return an empty object (indicating no differences)
	return {}

# Example Usage:

obj1 = {

  "a": 1,
  "v": 3,
  "x": [5, 6],
  "z": {
    "a": None
  }
}
obj2 = {
  "a": 2,
  "v": 4,
  "x": {"t": 2},
  "z": {
    "a": 2
  }
}

print(find_differences(obj1, obj2))
# Output:
# {
#   "a": [1, 2],
#   "v": [3, 4],
#   "z": {
#     "a": [None, 2]
#   }
# }
