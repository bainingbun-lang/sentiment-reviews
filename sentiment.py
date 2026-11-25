import sys
import re

POSITIVE = {
    "bueno", "buena", "excelente", "genial", "encanta", "encantó", "recomiendo",
    "rápido", "rapido", "calidad", "perfecto", "perfecta", "feliz", "contento",
    "great", "good", "love", "excellent", "fast", "recommend", "happy", "nice",
}
NEGATIVE = {
    "malo", "mala", "pésimo", "pesimo", "horrible", "roto", "rota", "tarda",
    "lento", "lenta", "nunca", "decepcionado", "decepción", "defectuoso",
    "bad", "terrible", "broken", "slow", "awful", "worst", "poor", "never",
}
NEGATORS = {"no", "not", "nunca", "never", "ni"}


def score(text):
    words = re.findall(r"\w+", text.lower())
    total = 0
    for i, word in enumerate(words):
        value = 1 if word in POSITIVE else -1 if word in NEGATIVE else 0
        if value and any(w in NEGATORS for w in words[max(0, i - 2):i]):
            value = -value
        total += value
    return total


def label(value):
    if value > 0:
        return "positivo"
    if value < 0:
        return "negativo"
    return "neutro"


def main():
    if len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as f:
            lines = f.read().splitlines()
    else:
        lines = sys.stdin.read().splitlines()

    counts = {"positivo": 0, "negativo": 0, "neutro": 0}
    for line in lines:
        if not line.strip():
            continue
        value = score(line)
        tag = label(value)
        counts[tag] += 1
        print(f"{tag:<9} {value:>3}  {line}")

    total = sum(counts.values())
    print()
    for tag, n in counts.items():
        pct = (n / total * 100) if total else 0
        print(f"{tag:<9} {n:>3}  ({pct:.0f}%)")


if __name__ == "__main__":
    main()
