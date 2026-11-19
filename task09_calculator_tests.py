from decimal import Decimal, ROUND_HALF_UP

BASE_RATE = Decimal("30.00")
FAT_STEP_VALUE = Decimal("0.40")
SNF_STEP_VALUE = Decimal("0.30")
REFERENCE_FAT = Decimal("3.5")
REFERENCE_SNF = Decimal("8.5")
CENT = Decimal("0.01")

def money(value):
    return value.quantize(CENT, rounding=ROUND_HALF_UP)

def payment(litres, fat, snf):
    litres, fat, snf = Decimal(str(litres)), Decimal(str(fat)), Decimal(str(snf))
    if litres < 0:
        raise ValueError("Litres cannot be negative")
    if not Decimal("2.0") <= fat <= Decimal("7.0"):
        raise ValueError("Fat must be between 2.0 and 7.0")
    if snf <= 0:
        raise ValueError("SNF must be positive")
    fat_steps = ((fat - REFERENCE_FAT) / Decimal("0.1")).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)
    snf_steps = ((snf - REFERENCE_SNF) / Decimal("0.1")).quantize(
        Decimal("1"), rounding=ROUND_HALF_UP)
    rate = BASE_RATE + fat_steps * FAT_STEP_VALUE + snf_steps * SNF_STEP_VALUE
    return money(litres * rate)

if __name__ == "__main__":
    cases = [
        ("above standard", 10, 4.0, 9.0, Decimal("335.00")),
        ("below standard", 5, 3.0, 7.5, Decimal("125.00")),
        ("standard", 10, 3.5, 8.5, Decimal("300.00")),
        ("minimum fat", 1, 2.0, 8.5, Decimal("24.00")),
        ("maximum fat", 1, 7.0, 8.5, Decimal("44.00")),
    ]
    for label, litres, fat, snf, expected in cases:
        actual = payment(litres, fat, snf)
        print(label, "expected =", expected, "actual =", actual,
              "PASS" if actual == expected else "FAIL")
    for label, args in [
        ("negative litres", (-1, 3.5, 8.5)),
        ("fat too low", (1, 1.9, 8.5)),
        ("fat too high", (1, 7.1, 8.5)),
    ]:
        try:
            payment(*args)
        except ValueError as exc:
            print(label, "PASS:", exc)
        else:
            print(label, "FAIL")
    entries = [(10, 4, 8), (5, 3, 7), (8, 5, 9), (6, 2, 8.5), (4, 7, 8.5)]
    total = sum((payment(*entry) for entry in entries), Decimal("0.00"))
    print("Five-entry total:", money(total))
    assert payment(10, 3.5, 8.5) == Decimal("300.00")
    print("Automated assertions passed.")
