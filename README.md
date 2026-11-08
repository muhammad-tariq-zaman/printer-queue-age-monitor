# printer-queue-age-monitor

Watch the print queue: jobs waiting over 15 minutes are WAITING, over 60 are STUCK — oldest first, so a jammed queue is caught before users start re-printing.

## How to run

```sh
python3 main.py jobs.csv
```

## Example output

```
JOB-118 on HP-OfficeJet: STUCK (90 min)
JOB-121 on HP-OfficeJet: OK (5 min)
```

Standard library only. Run the tests with `python3 -m unittest discover`.
