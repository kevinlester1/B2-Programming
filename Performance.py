def selection_sort(scores):
    """
    Sorts a list of scores in ascending order using the Selection Sort algorithm.
    """
    n = len(scores)
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if scores[j] < scores[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element of the unsorted part
        scores[i], scores[min_idx] = scores[min_idx], scores[i]
    return scores

# Input Data
student_scores = [75, 92, 88, 65, 95, 70, 80, 60]

# Display original list
print("Original student scores:", student_scores)

# Sort the data using the implemented Selection Sort algorithm
sorted_scores = selection_sort(list(student_scores)) # Create a copy to keep original intact

# Display sorted list
print("Sorted student scores (ascending):", sorted_scores)