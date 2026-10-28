
"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS ----

def cost_per_semester(annual_cost):
    """Give back what one semester costs."""
    return annual_cost / SEMESTERS_PER_YEAR


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    return annual_cost / MONTHS_PER_YEAR


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    semester_cost = cost_per_semester(annual_cost)
    return semester_cost / CLASS_DAYS_PER_SEMESTER


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    semester_cost = cost_per_semester(annual_cost)
    return semester_cost / credits


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    semester_cost = cost_per_semester(annual_cost)
    cs1430_cost = semester_cost * (CS1430_CREDITS / credits)
    return cs1430_cost / CS1430_MEETINGS_PER_SEMESTER


# ---- PROGRAM ----

def main():
    # Get the annual cost and semester credit load once.
    annual_cost = float(input("Enter the total cost for one year: $"))
    credits = int(input("Enter the credits you are taking this semester: "))

    while True:
        print("\n===== THE COST OF COLLEGE =====")
        print("1. Cost per semester")
        print("2. Cost per month")
        print("3. Cost per class day")
        print("4. Cost per credit")
        print("5. Cost per CS 1430 class period")
        print("6. Worth It?")
        print("Q. Quit")

        choice = input("Choose an option: ").strip().upper()

        if choice == "Q":
            print("Goodbye!")
            break

        elif choice == "1":
            result = cost_per_semester(annual_cost)
            print(f"Cost per semester: ${result:.2f}")

        elif choice == "2":
            result = cost_per_month(annual_cost)
            print(f"Cost per month: ${result:.2f}")

        elif choice == "3":
            result = cost_per_day(annual_cost)
            print(f"Cost per class day: ${result:.2f}")

        elif choice == "4":
            if credits > 0:
                result = cost_per_credit(annual_cost, credits)
                print(f"Cost per credit: ${result:.2f}")
            else:
                print("Credits must be greater than zero.")

        elif choice == "5":
            if credits > 0:
                result = cost_per_class(annual_cost, credits)
                print(f"Cost per CS 1430 class period: ${result:.2f}")
            else:
                print("Credits must be greater than zero.")

        elif choice == "6":
            result = cost_per_class(annual_cost, credits) if credits > 0 else 0
            print("\n===== WORTH IT? =====")
            print(f"Each CS 1430 class period costs ${result:.2f}.")
            print("Think about what you learn in class and how")
            print("that compares with the cost of attending.")

        else:
            print("Invalid choice. Please select 1-6 or Q.")



# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
