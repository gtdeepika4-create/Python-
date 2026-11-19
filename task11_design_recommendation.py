import json
from pathlib import Path

rate_card = {
    "base_rate": 30.00,
    "fat_step_value": 0.40,
    "snf_step_value": 0.30,
    "reference_fat": 3.5,
    "reference_snf": 8.5,
}
path = Path(__file__).with_name("rates.json")
path.write_text(json.dumps(rate_card, indent=2), encoding="utf-8")
loaded = json.loads(path.read_text(encoding="utf-8"))
print("Loaded rate card:")
for key, value in loaded.items():
    print(f"{key}: {value}")

print("\nRecommendation: use Decimal/integer paise for money, named or validated external rate data,")
print("input validation, reusable functions, automated tests and auditable records.")
print("At large scale, consider a database, access controls, transaction logs, backups and load tests.")
