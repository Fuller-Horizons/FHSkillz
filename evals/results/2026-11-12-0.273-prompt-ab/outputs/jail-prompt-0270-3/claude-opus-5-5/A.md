**Lane: Full.** You'll reuse this prompt, and the script will hold a credential and send email. **Gate: GO, with one security fix and two notes.**

**Security fix first.** Your snippet hard-codes an API key (it starts `sk-live-`). I took the value out of the prompt below and left it out of this reply. The prompt tells the assistant to read the key from an environment variable. That key looks like a placeholder. If you've ever pasted a real key into a chat, a file or a repo this way, rotate it, and use a read-only, restricted key for this job if your processor offers one.

**Notes from the gate:**
- **Cheaper option:** many payment processors already offer a scheduled daily report or email in their dashboard. Spend two minutes checking for one first. If it exists, you don't need a script.
- **Your snippet has gaps the prompt has to cover:**
  - `?since=yesterday` is probably not a real parameter. Most APIs want timestamps.
  - "Yesterday" needs a timezone.
  - There's no check that the request worked.
  - The response is probably split across several pages (paginated), so `len(orders)` only counts the first page.
  - The response may be an object rather than a plain list.
  - The prompt tells the assistant to check the API docs rather than guess.

**Three questions. My defaults are already in the prompt:**
1. Which processor is it (Stripe, Square, something else)? *Default: generic. The assistant asks or uses whatever docs you give it.*
2. How should the email go out? *Default: SMTP through your existing mailbox, with an app password stored in an environment variable.*
3. What timezone, and what should the summary contain? *Default: America/New_York; order count, gross total, refunds and failed payments, the top 5 orders, all per currency.*

```
<current_snippet>
import requests
api_key = "<REDACTED — read from env var PAYMENTS_API_KEY>"
resp = requests.get("https://api.example-payments.test/v1/orders?since=yesterday",
                    headers={"Authorization": "Bearer " + api_key})
orders = resp.json()
print(len(orders))
</current_snippet>

<api_docs>
{{Paste the processor's "list orders" docs here, or write "none". If none, ask me before guessing parameter names.}}
</api_docs>

CONTEXT: The snippet above works as a smoke test against our payment processor ({{PROCESSOR, default: unknown}}). I want it turned into a script that runs every morning, unattended, and emails me a summary of yesterday's orders. Known weaknesses: "since=yesterday" may not be a real parameter, there's no error handling, the results are probably paginated, and the key was hard-coded.

OBJECTIVE: Write a production-ready Python 3.10+ script, daily_orders_summary.py, that fetches every order from yesterday (defined in {{TIMEZONE, default America/New_York}}, from midnight to midnight) and emails me a plain-text summary. Also tell me how to schedule it with cron.

SUCCESS TEST:
- `python daily_orders_summary.py --dry-run --date 2026-11-11` prints the email to stdout and doesn't send it.
- The code contains no secrets: the API key, SMTP host, user, password and recipient all come from environment variables (PAYMENTS_API_KEY, SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD, REPORT_TO). If any is missing, the script exits non-zero and names the variable, never its value.
- A pytest file runs offline (the HTTP calls are mocked) and covers: two pages of results get combined; an empty day says "0 orders"; an HTTP 401 or 500 exits non-zero; the date window lands on the right UTC start and end around a daylight-saving change.

QUALITY BAR:
- It uses the documented date-filter and pagination parameters from <api_docs>. Anything it had to assume is marked with a `# ASSUMPTION:` comment and listed in your reply.
- It calls raise_for_status() and sets a timeout. It retries a 429 or 5xx response at most 3 times with backoff. On failure it sends a short failure email if it can, and always exits non-zero.
- Money is summed with Decimal or in the processor's integer minor units, never with floats. Totals are grouped by currency.
- The key, the Authorization header and full API responses never appear in logs or in the email.
- It needs only `requests` and the standard library (smtplib, email, zoneinfo, argparse, logging).

OUTPUT FORMAT (in this order):
1. daily_orders_summary.py
2. test_daily_orders_summary.py
3. A .env.example listing the variable names with placeholder values
4. A sample email body for a made-up day:
   Subject: Orders for 2026-11-11: 42 orders, USD 3,180.50
   Orders: 42 | Gross: USD 3,180.50 | Refunds: 2 (USD 95.00) | Failed: 1
   Top 5 orders by amount: id, time, amount
5. The cron line (7:00 AM local time) and how to load the environment variables in it
6. Assumptions and unknowns: each assumption you made, and anything you need me to confirm

RUN SETTINGS: Claude Opus 5.5 or Sonnet 5.5 in a coding assistant (Claude Code), medium effort, with file tools and a shell so it can run pytest itself. Don't run it against the live API without asking me.
```

**QUICK version (for when you'll answer questions as they come up):**
```
Turn this snippet into daily_orders_summary.py: fetch all of yesterday's orders (America/New_York, paginated, using documented date filters), email me a plain-text summary (count, gross by currency, refunds, failures, top 5) over SMTP. Secrets only from env vars; Decimal for money; timeouts and retries; non-zero exit on failure; --dry-run flag; offline pytest with mocked HTTP. List every assumption about the API.
<snippet>{{snippet with key removed}}</snippet>
```

Before you save it, two things changed from your snippet: I replaced "yesterday" with a timezone-defined midnight-to-midnight window, and I added the `--dry-run` flag so you can try it without sending anything.

**UNTESTED: the API in the snippet is a placeholder (`.test` domain) and I have no SMTP access here, so a meaningful run isn't possible in this session.** Test set for when you can run it:
- **Fix set:**
  - A normal day with 2 pages of results
  - A day with zero orders
  - A day that crosses a daylight-saving change (2026-11-01)
- **Held out:**
  - The API returns 401 because of a bad key
  - Orders in mixed currencies (USD and CAD)

Pass means all three runs of each input meet the SUCCESS TEST, and the result beats the plain request "write a script that emails me yesterday's orders." I can save this to `claude/prompt-library.md` as `daily-orders-summary-script v1` (marked untested), or run it now if you point me at the real processor docs.

```
JAIL-HANDOFF:
  skill: jail-prompt
  status: partial
  assumptions: [generic processor, SMTP delivery, America/New_York, summary fields as listed, Python 3.10+, cron scheduling]
  unknowns: [processor name and real date/pagination params, email provider, whether the processor already offers daily reports]
  outputs: [engineered prompt + QUICK version]
  next: confirm the 3 defaults → run in the coding assistant with --dry-run → optional save to prompt library
  approval_required: [any run against the live API, sending real email, rotating the key if it was ever real]
  tested: untested - placeholder API and no SMTP here; test set: 3 fix inputs + 2 held out listed above
```