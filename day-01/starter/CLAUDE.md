# CLAUDE.md — <repo name>

<!-- Keep this under 200 lines. Spend the lines on the traps, not on things
     the agent can already see by reading the code. Delete every angle-bracket
     placeholder before you commit it. -->

## What this repo is
<One paragraph. What the service does, who uses it, what breaks if it's wrong.>

## Run it
```
<install>
<run tests — the exact command, and roughly how long it takes>
<start locally>
```

## The rules that are not negotiable
<These are the ones that cost you a production incident. Be specific — an agent
 cannot act on "follow best practice".>

- Every query that touches guest, reservation or folio data **must** filter by
  `property_id`. A caller scoped to one property must never see another's data.
- Money is decimal, never float. Rounding on a folio balance is a customer call.
- Never log guest name, email, phone, document number or card data. Use the
  house logger, not `print`.
- A missing record is a 404, not a 500.
- New endpoint → one integration test. New branch in logic → one unit test.
- Config comes from the environment. No hostnames, keys or secrets in code.

## How we write things here
- <language/framework conventions that differ from the obvious default>
- <error handling pattern — point at one real file as the example>
- <naming, module layout, where tests live>

## Traps — the things that have already bitten us
- <the legacy module that looks dead and isn't>
- <the migration that must run before the tests pass>
- <the endpoint whose auth works differently from every other one>

## Don't touch
- <generated files, vendored code, anything with its own pipeline>
