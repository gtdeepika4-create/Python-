BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
REFERENCE_FAT = 3.5
REFERENCE_SNF = 8.5
MIN_FAT = 2.0
MAX_FAT = 7.0

RATE_CARD = {"base": BASE_RATE, "fat": FAT_STEP_VALUE, "snf": SNF_STEP_VALUE}
print("Rate card:", RATE_CARD)

value = 10
print(value, type(value).__name__)
value = "ten"
print(value, type(value).__name__)

a, b = 6, 9
print("Before swap:", a, b)
a, b = b, a
print("After swap:", a, b)
