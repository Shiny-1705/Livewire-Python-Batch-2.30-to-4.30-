# try:
#     a = int(input("Enter a:"))
#     b = int(input("Enter b:"))
#     result = a / b
#     print("Result:", result)
# except ZeroDivisionError:
#     print("Error: Cannot divide by zero!")


# try:
#     num = int(input("Enter a: "))
#     print("You entered:", num)
# except ValueError:
#     print("Error: Please enter a valid number!")

#
# try:
#     x = int(input("Enter number: "))
#     print(10 / x)
# except ValueError:
#     print("Something went wrong, program didn't crash!")


# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter divisor: "))
#     print(a / b)
# except ValueError:
#     print("Invalid input!")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")


# try:
#     num = int(input("Enter a number: "))
# except ValueError:
#     print("Invalid input!")
# else:
#     print("Square is:", num ** 2)

#
# try:
#     num = int(input("Enter number: "))
#     print(10 / num)
# except ValueError:
#     print("Error occurred!")
# finally:
#     print("This block always executes.")


# try:
#     num = int(input("Enter a positive number: "))
#     if num < 0:
#         raise ValueError("Negative number not allowed!")
#     print("Valid number:", num)
# except ValueError as e:
#     print("Error:", e)

#
# try:
#     age = int(input("Enter your age: "))
#     if age < 18:
#         raise Exception("You must be at least 18 years old!")
#     print("Access granted!")
# except Exception as e:
#     print("Error:", e)

#
# try:
#     a = int(input("Enter number: "))
#     b = int(input("Enter divisor: "))
#     print(a / b)
# except ValueError:
#     print("Invalid input! Enter numbers only.")
# except ZeroDivisionError:
#     print("Cannot divide by zero!")
# except Exception as e:
#     print("Other error:", e)

#
# try:
#     num = int(input("Enter a number: "))
#     try:
#         result = 10 / num
#         print("Result:", result)
#     except ZeroDivisionError:
#         print("Inner Error: Cannot divide by zero!")
# except ValueError:
#     print("Outer Error: Invalid input!")