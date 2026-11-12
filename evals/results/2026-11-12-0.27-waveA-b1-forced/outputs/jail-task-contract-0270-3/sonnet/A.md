I haven't shipped the contract, because the five files aren't where I can reach them.

`/tmp/fhlive-_s7c2cos` is empty, so none of `Report_Q3.PDF`, `Invoice-0042.PDF`, `NOTES.txt`, `Budget2026.XLSX` or `ReadMe.MD` exist there. The skill fails closed here: I won't write a contract, or rename anything, on a guess.

**Blocking unknown (field 7, inputs available):** where are the files? Please give me the directory path, or tell me the files live somewhere I can't reach. Mentioning that matters because a rename can't happen without access.

**Assumptions I've marked, which you can overrule:**
- **Target names (field 3):** the full name is lowercased, extension included: `report_q3.pdf`, `invoice-0042.pdf`, `notes.txt`, `budget2026.xlsx`, `readme.md`. This would change if you only want the extension lowercased, or the name part only.
- **Collisions (field 11):** if any lowercase target already exists, I'll stop and ask rather than overwrite it.
- **Method (field 14):** a plain `mv` with no overwrite (`mv -n`). It touches only these five files and is reversible by renaming back, so I'd treat it as low-risk. I'll still list the exact five `old → new` pairs for your approval before running anything.
- **Completion check (field 13):** after the renames, `ls` shows exactly the five lowercase names and none of the original-case names. That check fails if any file was missed or misnamed.

Once you tell me the path, I'll issue the full 14-field contract and wait for your approval before renaming.