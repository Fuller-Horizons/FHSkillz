**Lane: Lite.** The goal is clear and the stakes are modest. One security item and one cheaper-path check needed handling first, so I've noted my assumptions and put the prompt below.

## Two things to deal with before you use this

**1. There's a key written into your snippet.** It has a `sk-live-` prefix, so it's in the format of a production secret. I've left it out of the prompt and replaced it with an environment variable.
- If you've ever used a real key this way, **rotate it now**. It may already be in your shell history, in files where you saved the snippet, or in chat logs.
- Create a **restricted, read-only key** that can only read orders. A script that only reads should never hold a key that can also make changes.

**2. Check for a cheaper option first.** Most payment processors, including Stripe, Square and PayPal, can already email a daily summary or send a scheduled report from their dashboard. Check your processor's dashboard settings (look for reports or notifications) for about five minutes. If it already has this, you don't need a script.

**Verdict: GO, with those two notes.** A small script run each morning by a scheduler (cron) is the right tool. Asking an AI coding assistant to write it makes sense.

## Assumptions (edit the `[brackets]` before using)
- The script runs on one machine you control, scheduled with cron.
- The email is plain text and sent over SMTP with an app password. Plain text means order data can't run as HTML.
- "Yesterday" is a full calendar day in **your** timezone, not the server's.
- The summary shows only totals. It never includes customer names, emails or card details.

## The engineered prompt

```
METADATA: inputs: [processor API docs URL], existing snippet (below) · outputs: daily_orders_summary.py, test_daily_orders_summary.py, README section, crontab line · params: TIMEZONE=[America/New_York], SEND_HOUR=[7] · requires: none · produces: runnable script + passing tests

ROLE: Senior Python engineer who writes small, boring, well-tested ops scripts.

CONTEXT:
- I want a summary of yesterday's orders from my payment processor emailed to me every morning.
- Processor: [name]. API docs: [URL]. Read the docs for the real date-filter, pagination, and amount-unit conventions; do NOT trust my snippet's `?since=yesterday` parameter, which I guessed.
- My current test snippet (the starting point):
    import os, requests
    api_key = os.environ["PAYMENTS_API_KEY"]
    resp = requests.get("https://api.example-payments.test/v1/orders?since=yesterday",
                        headers={"Authorization": "Bearer " + api_key})
    orders = resp.json()
    print(len(orders))
- Known gaps in it: no timeout, no status check, no pagination, assumes the response is a bare list, server-local time.
- Runs on: [OS / server], Python [3.11+], scheduled by cron.

OBJECTIVE: Write a script that fetches every order created during yesterday (00:00:00 to 23:59:59 in TIMEZONE) and emails me a plain-text summary, plus tests that prove it.

SUCCESS TEST:
- `pytest -q` passes with zero network access (API and SMTP fully mocked).
- Tests cover: (a) zero orders → email still sent saying "0 orders"; (b) 3 pages of results → all counted exactly once; (c) an order at 23:59:59 local is included and one at 00:00:00 today is excluded, including across a DST change date; (d) HTTP 401/429/500 → non-zero exit and a clear error, no email claiming success; (e) an order field containing `<script>alert(1)</script>` and a line break plus `Bcc: x@evil.test` appears inert in the email and adds no headers.
- `grep -rnE "sk-(live|test)_|Bearer [A-Za-z0-9]" *.py` returns nothing.

PROCESS:
1) Read the API docs; state the exact endpoint, date filter, pagination scheme, and amount units you will use, citing the doc section.
2) Write the tests in the SUCCESS TEST first, then make them pass.
3) Compute the UTC window from TIMEZONE with zoneinfo; pass explicit timestamps to the API.
4) Paginate until exhausted; set request timeouts; retry 429/5xx with bounded backoff (max 3).
5) Build the summary: order count, gross total, refunds/failed count if available, top [N=5] products by revenue, currency-correct formatting (integer minor units → decimal).
6) Send via SMTP with STARTTLS using env-var credentials; plain-text body only.
7) Provide the crontab line and a README section listing every env var.

OUTPUT FORMAT: Email body shape:
    Orders for 2026-11-11 (America/New_York)
    Orders: 42 | Gross: $3,180.50 | Refunded: 2 ($85.00)
    Top products:
      1. Widget A — $1,200.00 (12)
    Generated 2026-11-12 07:00 EST
Then the code files, then the README section, then the crontab line.

CONSTRAINTS:
- Secrets only from env vars: PAYMENTS_API_KEY, SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, REPORT_TO. Fail fast with a clear message if any is missing; never print, log, or include them in exceptions.
- Assume a restricted read-only API key; the script must make GET requests only.
- No customer PII (names, emails, addresses, card data) in the email or logs.
- Plain-text email; no HTML rendering of API data; strip CR/LF from anything used in a header.
- Dependencies: requests + standard library only (tests may use pytest and responses).
- Single file, under ~200 lines excluding tests.

VERIFICATION PLAN:
- [AUTO] Run the timezone/DST boundary tests first; they are the most likely to fail.
- [AUTO] pytest -q; grep for secrets.
- [HUMAN] One live dry run with `--dry-run` (prints the email, sends nothing) against the real API using the restricted key; compare the count to the processor dashboard for the same day.
- [HUMAN] One real send to myself before enabling cron.

BEFORE RETURNING: Check each SUCCESS TEST item and report pass/fail. Score 1-5 on grounded (API details cited from docs) / verifiable / scoped / format-matched. Give confidence 0-100%. List any API behavior you assumed rather than confirmed in the docs. Offer 1-2 knobs (e.g., add a Slack webhook instead of email; add day-over-day comparison).
```

## Notes on the choices
- **The rewritten snippet inside the prompt** is your code with the key swapped for `os.environ`. The prompt also spells out its weak spots so the assistant doesn't copy them.
- **The boundary test is listed first in the verification plan.** Scripts like this most often fail quietly by using the wrong timezone, or by reading only the first page of results so a busy day comes back short. Both mistakes still produce a believable email.
- **`--dry-run` plus a check against your dashboard** catches a wrong-endpoint mistake that mocked tests can't catch.

I can save this prompt to the "Business Consulting Tools" project, or swap the placeholders for your processor's real API details if you tell me which processor you use.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: complete
  assumptions: [cron on a user-controlled machine, SMTP plain-text email, calendar day in user's timezone, totals-only summary with no PII]
  unknowns: [payment processor name and real API params, SMTP provider, timezone, whether processor already offers native daily email reports]
  outputs: [engineered prompt]
  next: check the processor's dashboard for built-in daily reports; if none, fill the [brackets] and run the prompt in the coding assistant
  approval_required: [rotate any key previously hardcoded, create restricted read-only API key, first live run against production API, enabling the cron job that sends email]
```