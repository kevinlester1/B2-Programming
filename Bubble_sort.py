def bubble_sort(capitals):
  """
  Sorts a list of items using the Bubble Sort algorithm.

  Args:
    capitals: A list of items to be sorted.
              The items are compared using the '>' operator.
  """
  n = len(capitals)

  # Traverse through all array elements
  for i in range(n - 1):
    # Last i elements are already in place, so we don't need to check them
    for j in range(n - i - 1):
      # Traverse the array from 0 to n-i-1
      # Swap if the element found is greater than the next element
      if capitals[j] > capitals[j + 1]:
        capitals[j], capitals[j + 1] = capitals[j + 1], capitals[j]

# Example usage:
if __name__ == "__main__":
  my_capitals = ["Tokyo", "London", "Paris", "Berlin", "Rome", "Washington D.C."]
  print(f"Original list: {my_capitals}")

  bubble_sort(my_capitals)
  print(f"Sorted list: {my_capitals}")

  numbers = [64, 34, 25, 12, 22, 11, 90]
  print(f"\nOriginal numbers: {numbers}")
  bubble_sort(numbers)
  print(f"Sorted numbers: {numbers}")
