def binary_search(sorted_list, target_id):
    """
    Implements the binary search algorithm to find a target_id in a sorted list.

    Args:
        sorted_list: A list of unique integer student IDs, sorted in ascending order.
        target_id: The student ID to search for.

    Returns:
        A tuple: (True, index) if target_id is found, where index is its position.
                  (False, -1) if target_id is not found.
    """
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        mid_id = sorted_list[mid]

        if mid_id == target_id:
            # Target ID found at the middle index
            return True, mid
        elif mid_id < target_id:
            # Target ID is in the upper half, adjust low boundary
            low = mid + 1
        else:
            # Target ID is in the lower half, adjust high boundary
            high = mid - 1
    
    # Target ID not found in the list
    return False, -1

# Input Data
student_ids = [101, 105, 112, 118, 123, 130, 135, 140, 145, 150]

print(f"Original List of Student IDs: {student_ids}\n")

# Perform Searches
# Search 1: Target ID that exists
target_id_1 = 123
found_1, index_1 = binary_search(student_ids, target_id_1)
print(f"Searching for Target ID: {target_id_1}")
if found_1:
    print(f"Result: Found! Index: {index_1}")
else:
    print(f"Result: Not Found.")
print("-" * 30)

# Search 2: Target ID that does not exist
target_id_2 = 110
found_2, index_2 = binary_search(student_ids, target_id_2)
print(f"Searching for Target ID: {target_id_2}")
if found_2:
    print(f"Result: Found! Index: {index_2}")
else:
    print(f"Result: Not Found.")
print("-" * 30)

# Search 3: Target ID at the beginning
target_id_3 = 101
found_3, index_3 = binary_search(student_ids, target_id_3)
print(f"Searching for Target ID: {target_id_3}")
if found_3:
    print(f"Result: Found! Index: {index_3}")
else:
    print(f"Result: Not Found.")
print("-" * 30)

# Search 4: Target ID at the end
target_id_4 = 150
found_4, index_4 = binary_search(student_ids, target_id_4)
print(f"Searching for Target ID: {target_id_4}")
if found_4:
    print(f"Result: Found! Index: {index_4}")
else:
    print(f"Result: Not Found.")
print("-" * 30)