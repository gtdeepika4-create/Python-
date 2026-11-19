from decimal import Decimal
from time import perf_counter

def total_float(values):
    total = 0.0
    for value in values:
        total += float(value)
    return total

def total_decimal(values):
    total = Decimal("0.00")
    for value in values:
        total += Decimal(value)
    return total

for count in (300, 6000, 150000):
    values = ["33.40"] * count
    start = perf_counter()
    ftotal = total_float(values)
    ftime = perf_counter() - start
    start = perf_counter()
    dtotal = total_decimal(values)
    dtime = perf_counter() - start
    print(f"n={count}")
    print(f"float total={ftotal:.2f}, time={ftime:.6f}s")
    print(f"Decimal total={dtotal:.2f}, time={dtime:.6f}s\n")

amounts = [Decimal("0.005")] * 10
round_each = sum((x.quantize(Decimal("0.01")) for x in amounts), Decimal("0.00"))
round_final = sum(amounts, Decimal("0.00")).quantize(Decimal("0.01"))
print("Round each:", round_each, "Round final:", round_final)
