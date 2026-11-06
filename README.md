# SQL Server Advanced Troubleshooting and Performance Tuning — Chapter Notes

Study materials generated from *SQL Server Advanced Troubleshooting and Performance Tuning*
by Dmitri Korotkevitch (O'Reilly Media, 2022).

## Single-page summary

**[`docs/chapter-01-summary/chapter-01-summary.html`](docs/chapter-01-summary/chapter-01-summary.html)**

One self-contained HTML file covering **Chapters 1 and 2** — 11 figures embedded as inline
base64 images (works offline, no server, no external assets) and 9 syntax-highlighted,
copyable T-SQL listings.

| Chapter | Topic | Book pages | Figures | Listings |
| --- | --- | --- | --- | --- |
| 1 | SQL Server Setup and Configuration | 1–26 | 1-1 … 1-5 | 1-1 … 1-5 |
| 2 | SQL Server Execution Model and Wait Statistics | 27–44 | 2-1 … 2-6 | 2-1 … 2-4 |

### Chapter 1 — Setup and Configuration

Hardware and OS considerations, then instance-level and database-level configuration.

- Figure 1-1 — Enabling IFI during SQL Server setup
- Figure 1-2 — Checking if instant file initialization is enabled
- Figure 1-3 — Nondefault server configuration options
- Figure 1-4 — Database layout for an eCommerce system
- Figure 1-5 — Server throughput with and without an active xEvents session
- Listing 1-1 — Checking IFI in old SQL Server versions
- Listing 1-2 — Checking the distribution of NUMA node schedulers (CPUs)
- Listing 1-3 — Detecting changes in server configuration settings
- Listing 1-4 — Analyzing the SQL Server error log
- Listing 1-5 — Creating an xEvents session to capture queries in the system

### Chapter 2 — Execution Model and Wait Statistics

How SQL Server schedules and runs work, and how to use wait statistics to find bottlenecks.

- Figure 2-1 — Major SQL Server components
- Figure 2-2 — Task lifecycle (RUNNING / RUNNABLE / SUSPENDED)
- Figure 2-3 — Example of `sys.dm_os_wait_stats` output
- Figure 2-4 — Typical Wait Statistics Analysis troubleshooting cycle
- Figure 2-5 — Dependencies and issues
- Figure 2-6 — Example Resource Governor configuration
- Listing 2-1 — Getting top wait types in the system (SQL Server 2012 and later)
- Listing 2-2 — Signal versus resource waits
- Listing 2-3 — Using the `sys.dm_exec_requests` view
- Listing 2-4 — NUMA node scheduler statistics

## Viewing it

Open the HTML file in any browser — no build step. To serve it locally:

```bash
cd docs/chapter-01-summary
python3 serve.py        # http://localhost:8000/
```

Figures and code listings are reproduced from the book for study and reference;
all rights remain with the author and publisher.
