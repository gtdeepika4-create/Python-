import math

BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
REFERENCE_FAT = 3.5
REFERENCE_SNF = 8.5

def rate_per_litre(fat, snf, step_method=round):
    fat_steps = step_method((fat - REFERENCE_FAT) / 0.1)
    snf_steps = round((snf - REFERENCE_SNF) / 0.1)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return fat_steps, snf_steps, round(rate, 2)

for fat in (4.2, 3.1):
    print("fat =", fat)
    for name, method in (("round", round), ("int", int), ("floor", math.floor)):
        fs, ss, rate = rate_per_litre(fat, 8.5, method)
        print(name, "fat_steps =", fs, "rate =", f"{rate:.2f}")

print("(4.2 - 3.5) / 0.1 =", (4.2 - 3.5) / 0.1)
print("round((4.2 - 3.5) / 0.1) =", round((4.2 - 3.5) / 0.1))
print("-2**2 =", -2**2, "(-2)**2 =", (-2)**2)
print("int(-2.7) =", int(-2.7), "floor(-2.7) =", math.floor(-2.7))
fat = 4.2
print("fat in range:", 2.0 <= fat <= 7.0)
