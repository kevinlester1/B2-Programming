# Function to display the current state of the queue
def display_queue(queue):
    """
    Prints the current state of the customer support queue.
    If the queue is empty, it indicates that.
    """
    if not queue:
        print("Queue: [] (The queue is empty)")
    else:
        print(f"Queue: {queue}")

# Function to add a customer to the queue
def customer_submits_inquiry(queue, customer_id):
    """
    Adds a customer to the end of the queue and displays the updated queue.
    """
    print(f"\n--- Event: Customer '{customer_id}' submits an inquiry ---")
    queue.append(customer_id) # Add customer to the end of the list (queue)
    print(f"'{customer_id}' has been added to the queue.")
    display_queue(queue)

# Function for an agent to process an inquiry
def agent_processes_inquiry(queue):
    """
    Removes the first customer from the queue (if any) and displays the updated queue.
    Handles the case where the queue is empty.
    """
    print("\n--- Event: An agent becomes free and processes an inquiry ---")
    if queue:
        processed_customer = queue.pop(0) # Remove customer from the front of the list (queue)
        print(f"Agent processed inquiry from '{processed_customer}'.")
    else:
        print("No customers in the queue to process.")
    display_queue(queue)

# --- Simulation Start ---
print("Simulating the Happy Customer Support Queue:")

# Initialize the empty queue
customer_queue = []
display_queue(customer_queue) # Show initial empty queue

# 1. Customer "Alice" submits an inquiry.
customer_submits_inquiry(customer_queue, "Alice")

# 2. Customer "Bob" submits an inquiry.
customer_submits_inquiry(customer_queue, "Bob")

# 3. An agent becomes free and processes an inquiry.
agent_processes_inquiry(customer_queue)

# 4. Customer "Charlie" submits an inquiry.
customer_submits_inquiry(customer_queue, "Charlie")

# 5. An agent becomes free and processes an inquiry.
agent_processes_inquiry(customer_queue)

# 6. Customer "David" submits an inquiry.
customer_submits_inquiry(customer_queue, "David")

print("\n--- Simulation End ---")