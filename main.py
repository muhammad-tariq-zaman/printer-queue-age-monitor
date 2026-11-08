"""Print jobs waiting too long in the queue.

Usage: python3 main.py jobs.csv
CSV columns: job,printer,age_minutes.
STUCK over 60 minutes, WAITING over 15, otherwise OK.
Oldest job first.
"""
import argparse, csv, sys

def monitor(rows):
    out = []
    for row in rows:
        age = int(row["age_minutes"])
        verdict = "STUCK" if age > 60 else ("WAITING" if age > 15 else "OK")
        out.append((row["job"], row["printer"], age, verdict))
    return sorted(out, key=lambda r: -r[2])

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path")
    args = parser.parse_args(argv)
    with open(args.path, newline="", encoding="utf-8") as f:
        for job, printer, age, verdict in monitor(list(csv.DictReader(f))):
            print(f"{job} on {printer}: {verdict} ({age} min)")
    return 0

if __name__ == "__main__":
    sys.exit(main())
