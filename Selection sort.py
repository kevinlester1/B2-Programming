def selection_sort(arr):
  """
  Sorts a list of items using the Selection Sort algorithm.

  Args:
    arr: A list of items to be sorted.
         The items are compared using the '>' operator.
  """
  n = len(arr)

  # Traverse through all array elements
  for i in range(n - 1):
    # Find the minimum element in the remaining unsorted array
    min_idx = i
    for j in range(i + 1, n):
      if arr[j] < arr[min_idx]:
        min_idx = j

    # Swap the found minimum element with the first element of the unsorted part
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Example usage:
if __name__ == "__main__":
  my_capitals = ["Tokyo", "London", "Paris", "Berlin", "Rome", "Washington D.C."]
  print(f"Original list: {my_capitals}")

  selection_sort(my_capitals)
  print(f"Sorted list: {my_capitals}")

  numbers = [64, 34, 25, 12, 22, 11, 90]
  print(f"\nOriginal numbers: {numbers}")
  selection_sort(numbers)
  print(f"Sorted numbers: {numbers}")