""" Grade Calculation """
#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: September 2023

import math  # Used for rounding grades with decimals (ex: exam1 = 62.5%)


def main():
    """Main function"""

    print("This program will determine your final grade\nPlease input your"
          + " 3 midterm grades and your final exam grade. Along with the "
          + "weight that each of these marks has on the final grade.")

    retry = True

    # The retry variable allows for the user to give improper input and retry
    while retry:
        retry = False
        # Makes sure the input is valid
        try:
            midterm1 = float(input("Midterm 1: "))
            midterm1_weight = float(input("Midterm 1 weight (0-100%): "))
            midterm2 = float(input("Midterm 2: "))
            midterm2_weight = float(input("Midterm 2 weight (0-100%): "))
            midterm3 = float(input("Midterm 3: "))
            midterm3_weight = float(input("Midterm 3 weight (0-100%): "))
            exam1 = float(input("Exam: "))
            exam1_weight = float(input("Exam 1 weight (0-100%): "))

            if not (midterm1_weight + midterm2_weight + midterm3_weight + exam1_weight == 100):
                print("Please make sure that the weights add up to 100%\n\n\n")
                retry = True
            else:
                # Checks if all the grades are from 0-100%
                if ((midterm1 >= 0 and midterm1 <= 100) and (midterm1_weight >= 0 and midterm1_weight <= 100) and (midterm2 >= 0 and midterm2 <= 100) and (midterm2_weight >= 0 and midterm2_weight <= 100) and (midterm3 >= 0 and midterm3 <= 100) and (midterm3_weight >= 0 and midterm3_weight <= 100) and (exam1 >= 0 and exam1 <= 100) and (exam1_weight >= 0 and exam1_weight <= 100)):
                    final_grade = float(midterm1 * midterm1_weight / 100 + midterm2 * midterm2_weight / 100 + midterm3 * midterm3_weight / 100 + exam1 * exam1_weight / 100)
                    print("\nYour final grade is ", final_grade)
                else:
                    print("Please input grades from 0-100% \n\n\n")
                    retry = True
        except Exception:
            print("Please input an actual grade\n\n\n")
            retry = True


if __name__ == "__main__":
    main()
