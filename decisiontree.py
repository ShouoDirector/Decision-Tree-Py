import math


def entropy(data):
    """
    This function takes in a list of target values and calculates the entropy
    """
    total = len(data)
    counts = {}
    for val in data:
        if val not in counts:
            counts[val] = 0
        counts[val] += 1
    entropy = 0
    for val in counts:
        p = counts[val] / total
        entropy -= p * math.log2(p)
    return entropy

def attribute_entropy(data, attribute):
    """
    This function takes in the dataset and an attribute
    and calculates the entropy of the attribute over the available population
    """
    attribute_values = set(data[attribute])
    weighted_entropy = 0
    for value in attribute_values:
        subset = {key: [val[i] for i in range(len(val)) if data[attribute][i] == value] for key, val in data.items()}
        weight = len(subset[attribute]) / len(data[attribute])
        weighted_entropy += weight * entropy(subset[attribute])
    return weighted_entropy

def information_gain(data, attribute, target):
    """
    This function takes in the dataset, an attribute and the target variable
    and calculates the information gain for the given attribute
    """
    total_entropy = entropy(data[target])
    attribute_values = set(data[attribute])
    weighted_entropy = 0
    for value in attribute_values:
        subset = {key: [val[i] for i in range(len(val)) if data[attribute][i] == value] for key, val in data.items()}
        weight = len(subset[target]) / len(data[target])
        weighted_entropy += weight * entropy(subset[target])
    information_gain = total_entropy - weighted_entropy
    return information_gain


dataset = {
    "Outlook": ["Sunny", "Sunny", "Overcast", "Rain", "Rain", "Rain", "Overcast", "Sunny", "Sunny", "Rain", "Sunny", "Overcast", "Overcast", "Rain"],
    "Temperature": ["Hot", "Hot", "Hot", "Mild", "Cool", "Cool", "Cool", "Mild", "Cool", "Mild", "Mild", "Mild", "Hot", "Mild"],
    "Humidity": ["High", "High", "High", "High", "Normal", "Normal", "Normal", "High", "Normal", "Normal", "Normal", "High", "Normal", "High"],
    "Wind": ["Weak", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Weak", "Weak", "Strong", "Strong", "Weak", "Strong"],
    "Played Badminton": ["No", "No", "Yes", "Yes", "Yes", "No", "Yes", "No", "Yes", "Yes", "Yes", "Yes", "Yes", "No"]
}

attributes = list(dataset.keys())
num_attributes = len(attributes)

# Print empty line
print()

# Print the header row
print(" " * 6, end="")
for attribute in attributes:
    print(f"{attribute: <12}", end="")
print()

print()

# Print the rows
for i in range(len(dataset[attributes[0]])):
    print(f"{i+1: <6}", end="")
    for j in range(num_attributes):
        print(f"{dataset[attributes[j]][i]: <12}", end="")
    print()

print()

target = "Played Badminton"

print("\nInformation Gain:" + "\n")
for attribute in dataset:
    if attribute != target:
        info_gain = information_gain(dataset, attribute, target)
        print("  " + f"{attribute: <20}: {info_gain:.3f}")


print(" ")

# Print entropy of each attribute
print("\nEntropy:" + "\n")
for attribute in dataset:
    print("  " + f"{attribute: <20}: {entropy(dataset[attribute]):.3f}")
print("\n")

gains = [(information_gain(dataset, attribute, target), attribute) for attribute in dataset if attribute != target]
gains.sort(reverse=True)
ordered_columns = [attribute for _, attribute in gains]
print("Hierarchy | " + " > ".join(ordered_columns))
print("\n\n\n")