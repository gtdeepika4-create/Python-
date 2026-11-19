BASE_RATE = 30.00
FAT_STEP_VALUE = 0.40
SNF_STEP_VALUE = 0.30
REFERENCE_FAT = 3.5
REFERENCE_SNF = 8.5

def rate_per_litre(fat, snf):
    fat_steps = round((fat - REFERENCE_FAT) / 0.1)
    snf_steps = round((snf - REFERENCE_SNF) / 0.1)
    return round(BASE_RATE + fat_steps * FAT_STEP_VALUE
                 + snf_steps * SNF_STEP_VALUE, 2)

def payout(litres, fat, snf):
    return round(litres * rate_per_litre(fat, snf), 2)

def ten_day_total(payments):
    return round(sum(payments), 2)

payments = [
    payout(10, 4.0, 8.5),
    payout(5, 3.5, 8.5),
    payout(8, 3.1, 8.3),
]
print("Payments:", payments)
print("Ten-day total:", f"{ten_day_total(payments):.2f}")
