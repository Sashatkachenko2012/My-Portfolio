


math_grade = [1.4, 1.7, 3.0, 2.4]


def calculate_grades(grades_list):
    total_sum = 0  # Initialize sum

    # --- Loop starts here (Indented) ---
    for grade in grades_list:
        total_sum = total_sum + grade  # Fix the typo (total_sum)
    # --- Loop ends here (No more indentation) ---

    # Calculations happen AFTER the loop finishes
    total_grades = len(grades_list)
    average = total_sum / total_grades

    # We return two values separated by a comma (a Tuple!)
    return average, total_grades


# --- Main Program Logic (Outside the function) ---

# We collect the two returned values (average and count)
final_average, total_count = calculate_grades(math_grade)

print(f"You have got {total_count} grades")
print(f"Your final average is {final_average:.2f}")  # Use '.2f' to format the number

