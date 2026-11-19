from decimal import Decimal, ROUND_HALF_UP

CENT = Decimal("0.01")
REFERENCE_FAT = Decimal("3.50")
REFERENCE_SNF = Decimal("8.50")
SNF_STEP_VALUE = Decimal("0.30")
BONUS_PER_LITRE = Decimal("0.50")

def rounded_steps(value, reference):
    return ((value - reference) / Decimal("0.1")).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)

def rate_per_litre(fat, snf, seasonal=False):
    base = Decimal("32.00") if seasonal else Decimal("30.00")
    fat_step_value = Decimal("0.45") if seasonal else Decimal("0.40")
    fat_steps = rounded_steps(Decimal(str(fat)), REFERENCE_FAT)
    snf_steps = rounded_steps(Decimal(str(snf)), REFERENCE_SNF)
    return base + fat_steps * fat_step_value + snf_steps * SNF_STEP_VALUE

def ten_day_payment(entries, seasonal=False):
    litres_total = sum(Decimal(str(entry[0])) for entry in entries)
    base_total = sum(
        Decimal(str(litres)) * rate_per_litre(fat, snf, seasonal)
        for litres, fat, snf in entries
    )
    bonus = litres_total * BONUS_PER_LITRE if litres_total > 500 else Decimal("0.00")
    return (base_total.quantize(CENT, rounding=ROUND_HALF_UP),
            bonus.quantize(CENT, rounding=ROUND_HALF_UP))

if __name__ == "__main__":
    sample = [(10, "3.75", "8.70")]
    for seasonal in (False, True):
        base, bonus = ten_day_payment(sample, seasonal)
        print("Seasonal rates:", seasonal, "base payment:", base,
              "bonus:", bonus, "total:", base + bonus)
    for litres in (500, 501):
        bonus = Decimal(litres) * BONUS_PER_LITRE if litres > 500 else Decimal("0.00")
        print(f"{litres}-litre bonus:", bonus.quantize(CENT))
