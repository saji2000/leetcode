def obj_diff(obj1, obj2):
    diff = {}

    # Collect all unique keys from both dictionaries
    keys = set(obj1.keys()).union(obj2.keys())

    for key in keys:
        if key in obj1 and key in obj2:
            # Check if values are different
            if obj1[key] != obj2[key]:
                diff[key] = [obj1[key], obj2[key]]
        elif key in obj1:
            diff[key] = [obj1[key], None]
        else:
            diff[key] = [None, obj2[key]]

    return diff


# Example usage
obj1 = {
  "a": 1,
  "v": 3,
  "x": [],
  "z": {
    "a": None
  }
}
obj2 = {
  "a": 2,
  "v": 4,
  "z": {
    "a": 2
  }
}

diffs = obj_diff(obj1, obj2)
print(diffs)
