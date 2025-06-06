# Global Data
# TAX_RATE is a global variable, accessible from anywhere in the program.
TAX_RATE = 0.15  # Represents a 15% tax rate

def calculate_employee_pay(hourly_wage, hours_worked, bonus_amount=0):
    """
    Calculates the net pay for a single employee based on their wage, hours, and optional bonus.
    Demonstrates local variable scope and access to global variables.

    Parameters:
        hourly_wage (float): The employee's base hourly wage.
        hours_worked (float): The total hours worked by the employee.
        bonus_amount (float, optional): An additional bonus amount for the employee. Defaults to 0.

    Returns:
        float: The employee's net pay after tax deduction.
    """
    # These variables (gross_pay, tax_deduction, net_pay) are local to this function.
    # They are created when the function is called and destroyed when it finishes.
    gross_pay = hourly_wage * hours_worked + bonus_amount
    tax_deduction = gross_pay * TAX_RATE  # Accessing the global TAX_RATE
    net_pay = gross_pay - tax_deduction

    print(f"\n--- Inside calculate_employee_pay() ---")
    print(f"Hourly Wage: ${hourly_wage:.2f}, Hours Worked: {hours_worked}, Bonus: ${bonus_amount:.2f}")
    print(f"Gross Pay (local): ${gross_pay:.2f}")
    print(f"Tax Deduction (local): ${tax_deduction:.2f}")
    print(f"Net Pay (local): ${net_pay:.2f}")
    # Demonstrating access to the global variable TAX_RATE from within the function.
    print(f"TAX_RATE (global, accessible here): {TAX_RATE * 100:.0f}%")
    print(f"------------------------------------")

    return net_pay

def main_payroll_system():
    """
    Manages the overall payroll calculations for multiple employees.
    Demonstrates local variable scope and calls to other functions.
    """
    # total_payroll is a local variable to main_payroll_system().
    # It exists only within the execution of this function.
    total_payroll = 0.0

    print(f"\n--- Inside main_payroll_system() ---")
    # Demonstrating access to the global variable TAX_RATE from within this function.
    print(f"TAX_RATE (global, accessible here): {TAX_RATE * 100:.0f}%")

    # Sample Employee Data Sets
    # Employee 1
    employee1_wage = 20.0
    employee1_hours = 40.0
    employee1_bonus = 100.0
    employee1_net_pay = calculate_employee_pay(employee1_wage, employee1_hours, employee1_bonus)
    print(f"Summary: Employee 1 Final Net Pay: ${employee1_net_pay:.2f}")
    total_payroll += employee1_net_pay

    # Employee 2 (no bonus)
    employee2_wage = 25.0
    employee2_hours = 35.0
    employee2_net_pay = calculate_employee_pay(employee2_wage, employee2_hours) # bonus_amount defaults to 0
    print(f"Summary: Employee 2 Final Net Pay: ${employee2_net_pay:.2f}")
    total_payroll += employee2_net_pay

    # Employee 3
    employee3_wage = 18.0
    employee3_hours = 45.0
    employee3_bonus = 50.0
    employee3_net_pay = calculate_employee_pay(employee3_wage, employee3_hours, employee3_bonus)
    print(f"Summary: Employee 3 Final Net Pay: ${employee3_net_pay:.2f}")
    total_payroll += employee3_net_pay

    print(f"\n--- End of main_payroll_system() ---")
    print(f"Total Company Payroll (local to main_payroll_system): ${total_payroll:.2f}")

    # --- Attempting to access local variables from calculate_employee_pay() ---
    # The following line would cause a 'NameError' because 'gross_pay' is a local variable
    # defined inside 'calculate_employee_pay()' and is not visible or accessible
    # in the scope of 'main_payroll_system()'.
    # Uncomment the line below to see the error.
    # print(f"Attempting to access gross_pay from main_payroll_system: {gross_pay}")
    # Explanation for failure: 'gross_pay' is a local variable of 'calculate_employee_pay'.
    # Its scope is limited to that function. Once 'calculate_employee_pay' finishes execution,
    # 'gross_pay' no longer exists.

# --- Main execution block ---
# This ensures that main_payroll_system() is called only when the script is executed directly.
if __name__ == "__main__":
    print(f"--- Program Start ---")
    # Demonstrating access to the global variable TAX_RATE from the global scope.
    print(f"TAX_RATE (global, accessible here): {TAX_RATE * 100:.0f}%")

    main_payroll_system()

    print(f"\n--- Outside any function (Global Scope) ---")
    # Demonstrating access to the global variable TAX_RATE from the global scope after function calls.
    print(f"TAX_RATE (global, still accessible): {TAX_RATE * 100:.0f}%")

    # --- Attempting to access local variables from other functions (from global scope) ---
    # The following lines would cause 'NameError' because 'gross_pay' is local to 'calculate_employee_pay'
    # and 'total_payroll' is local to 'main_payroll_system'. They are not accessible from the global scope.
    # Uncomment the lines below to see the error.
    # print(f"Attempting to access gross_pay from global scope: {gross_pay}")
    # print(f"Attempting to access total_payroll from global scope: {total_payroll}")
    # Explanation for failure: Variables defined inside functions (like 'gross_pay' in
    # 'calculate_employee_pay' and 'total_payroll' in 'main_payroll_system') have local scope.
    # They are only visible within the function where they are defined.
    # Once the function completes, these local variables are deallocated.
    print(f"--- Program End ---")
