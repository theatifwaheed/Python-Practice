# This was Quiz 2 AI Question.

# Array to Derivative...
Array = [2, 3, 4, 6, 1, 4, 77, 9, 2, 5, 8, -6]

# Getting length.
length = len(Array)

Derivative = []

# Applying Loop.
# J Starts from 1 and Goes to total length - 1
for j in range(1, length):
    # i Will start from 0 and Goes to Total - 2
    i = j - 1
    num = Array[j] - Array[i]
    Derivative.append(num)

print("Original: ")
print(Array)
print("Derivative: ")
print(Derivative)






