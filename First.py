# 1. temperatures = [42, 38, 45, 49, 36]

# for temp in temperatures:
#     if temp >= 50:
#         print("Experiment failed: Temperature threshold exceeded.")
#         break
#     else: 
#         print("Experiment completed successfully")


# value = 100
# threshold = 10
# iterations = 0

# while value >= threshold:
#     value /= 2
#     iterations += 1

# print(f"It took {iterations} iterations to drop below the threshold.")


def sum_arithmetic_series(a1, n, d):
    """Calculates the sum of an arithmetric series.
    a1: First term
    n: Number of terms
    d: Common difference
    """
    return (n / 2) * (2 * a1 + (n -1) * d)