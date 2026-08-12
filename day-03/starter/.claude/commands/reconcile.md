# Reconcile the FX1 module output

Run the local reconciliation check.

```bash
python3 tools/reconcile-report.py modules/<mine>/OUTPUT-CONTRACT.json
```

Report every mismatch with the field name, expected value, actual value, and source path.

The command uses local files. The command records its result in the terminal.
