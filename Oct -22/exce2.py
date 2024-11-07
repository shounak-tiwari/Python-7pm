# import math

# # Function to check for floating-point errors
# def safe_add(a, b):
#     result = a + b
#     # Checking for a specific condition where we consider it an error
#     if math.isclose(result, 0.3, rel_tol=1e-9):
#         return result
#     else:
#         raise FloatingPointError("Floating-point error detected: result is not close to expected value.")

# # Using try-except to handle the error
# try:
#     a = 0.1 + 0.2
#     print(safe_add(a, 0))
# except FloatingPointError as e:
#     print(f"Error: {e}")

try:
    x = 1.8 *(10**(19))

    if x ==1.8:
        print(x)
    else:
        raise FloatingPointError

except FloatingPointError as e :
    print(e)
