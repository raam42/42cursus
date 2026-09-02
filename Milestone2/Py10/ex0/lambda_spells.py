import sys
from typing import Any


try:
    from data_generator import FuncMagDataGenerator    #type:  ignore
except ImportError:
    print("[ERROR] Could not import 'data_generator.py'.\n"
          "Please ensure the file is extracted and in the same directory.")
    sys.exit(1)


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Sorts magical artifacts by power level in descending order."""
    return sorted(
        artifacts, key=lambda artifact: artifact['power'], reverse=True)


def power_filter(mages: list[dict[str, Any]], min_power: int
                 ) -> list[dict[str, Any]]:
    """Filters mages, returning only those with power >= min_power."""
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Adds a '*' prefix and ' *' suffix to a list of spell names."""
    return list(map(lambda spell: f"*{spell} *", spells))


def mage_stats(mages: list[dict]) -> dict:
   """Calculates max, min, and average power for a list of mages."""
   if not mages:
       return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

   max_p = max(mages, key=lambda m: m['power'])['power']
   min_p = min(mages, key=lambda m: m['power'])['power']

   total_power = sum(map(lambda m: m['power'], mages))
   avg_p = round(total_power / len(mages), 2)

   return {
       'max_power': max_p,
       'min_power': min_p,
       'avg_power': avg_p
   }


def main() -> None:
    print("      Lambda Sanctum QA Test Runner      \n"
          ("=" * 42 + "\n"))

    generator = FuncMagDataGenerator()
    artifacts = generator.generate_artifacts(4)
    mages = generator.generate_mages(5)
    spells = generator.generate_spells(4)

    # 2. Test Artifact Sorter (Matching the Subject's Expected Output)
    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)
    if len(sorted_artifacts) >= 2:
        first = sorted_artifacts[0]
        second = sorted_artifacts[1]
        print(f"{first['name']} ({first['power']} power) comes before "
              f"{second['name']} ({second['power']} power)")

    # 3. Test Power Filter
    print("\nTesting power filter (min_power = 75)...")
    strong_mages = power_filter(mages, 75)
    if strong_mages:
        for mage in strong_mages:
            print(f"- {mage['name']} ({mage['power']} power, {mage['element']} element)")
    else:
        print("- No mages met the power threshold this time!")

    # 4. Test Spell Transformer
    print("\nTesting spell transformer...")
    transformed_spells = spell_transformer(spells)
    print(" ".join(transformed_spells))

    # 5. Test Mage Stats
    print("\nTesting mage stats...")
    stats = mage_stats(mages)
    print(f"Max Power: {stats['max_power']}")
    print(f"Min Power: {stats['min_power']}")
    print(f"Avg Power: {stats['avg_power']}")


if __name__ == "__main__":
    main()