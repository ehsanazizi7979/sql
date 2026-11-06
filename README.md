# SQL Server Advanced Troubleshooting and Performance Tuning — Chapter Notes

Study materials generated from *SQL Server Advanced Troubleshooting and Performance Tuning*
by Dmitri Korotkevitch (O'Reilly Media, 2022).

## Single-page summary

**[`docs/chapter-01-summary/chapter-01-summary.html`](docs/chapter-01-summary/chapter-01-summary.html)**

One self-contained HTML file covering **Chapters 1 through 7** — 71 figures embedded as inline
base64 images (works offline, no server, no external assets) and 68 syntax-highlighted,
copyable T-SQL listings.

| Chapter | Topic | Book pages | Figures | Listings |
| --- | --- | --- | --- | --- |
| 1 | SQL Server Setup and Configuration | 1–26 | 1-1 … 1-5 | 1-1 … 1-5 |
| 2 | SQL Server Execution Model and Wait Statistics | 27–44 | 2-1 … 2-6 | 2-1 … 2-4 |
| 3 | Disk Subsystem Performance | 45–67 | 3-1 … 3-8 | 3-1 … 3-3 |
| 4 | Inefficient Queries | 69–103 | 4-1 … 4-9 | 4-1 … 4-10 |
| 5 | Data Storage and Query Tuning | 105–158 | 5-1 … 5-22 | 5-1 … 5-14 |
| 6 | CPU Load | 159–183 | 6-1 … 6-9 | 6-1 … 6-16 |
| 7 | Memory Issues | 185–218 | 7-1 … 7-12 | 7-1 … 7-16 |

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

### Chapter 3 — Disk Subsystem Performance

How SQL Server issues I/O, how to measure latency per file, and how checkpoint tuning
fixes the most common source of I/O bursts.

- Figure 3-1 — Reading a data page from disk: initiating the read
- Figure 3-2 — Reading a data page from disk: completing the read
- Figure 3-3 — Storage subsystem (network based)
- Figure 3-4 — Sample output from `sys.dm_io_virtual_file_stats`
- Figure 3-5 — Checkpoint and disk queueing
- Figure 3-6 — Sample `sys.dm_io_virtual_file_stats` with automatic checkpoint
- Figure 3-7 — Indirect checkpoint performance counters
- Figure 3-8 — Sample `sys.dm_io_virtual_file_stats` with indirect checkpoint
- Listing 3-1 — Using the `sys.dm_io_virtual_file_stats` view
- Listing 3-2 — Using the `sys.dm_os_performance_counters` view
- Listing 3-3 — Getting Page Life Expectancy in the system

### Chapter 4 — Inefficient Queries

How bad queries hurt, and the four detection techniques: plan cache statistics,
Extended Events, the Query Store, and third-party tools.

- Figure 4-1 — Partial output from the `sys.dm_exec_query_stats` view
- Figure 4-2 — Multiple plans with the same `query_hash` and `query_plan_hash`
- Figure 4-3 — Partial output of the `sys.dm_exec_procedure_stats` view
- Figure 4-4 — Query processing pipeline
- Figure 4-5 — Query Store reports in SSMS
- Figure 4-6 — Regressed Queries report
- Figure 4-7 — Top Resource Consuming Queries report
- Figure 4-8 — Overall Resource Consumption report
- Figure 4-9 — Query Store DMVs
- Listing 4-1 — Using the `sys.dm_exec_query_stats` view
- Listing 4-2 — The `query_hash` and `query_plan_hash` queries in action
- Listing 4-3 — `sys.dm_exec_query_stats` with `query_hash` aggregation
- Listing 4-4 — Using the `sys.dm_exec_procedure_stats` view
- Listing 4-5 — Execution plan and statistics for stored procedure statements
- Listing 4-6 — Capturing CPU- and I/O-intensive queries (xEvents)
- Listing 4-7 — Parsing collected xEvent data
- Listing 4-8 — Getting expensive queries from the Query Store
- Listing 4-9 — Queries with different context settings
- Listing 4-10 — Detecting queries with duplicated `query_hash` values

### Chapter 5 — Data Storage and Query Tuning

How row-store data is actually laid out, why a seek can cost the same as a scan, how
statistics drive cardinality estimation, and how to choose indexes and join types.

- Figure 5-1 — Internal table structure
- Figure 5-2 — B-Tree index
- Figure 5-3 — Index scan
- Figure 5-4 — Top and Index Scan operators
- Figure 5-5 — Index Seek operator
- Figure 5-6 — Composite indexes
- Figure 5-7 — Clustered and nonclustered indexes in the `Customers` table
- Figure 5-8 — Nonclustered index usage, part 1
- Figure 5-9 — Nonclustered index usage, part 2
- Figure 5-10 — Page split
- Figure 5-11 — Statistics output from `DBCC SHOW_STATISTICS`
- Figure 5-12 — Row mode execution: getting the first row
- Figure 5-13 — Row mode execution: getting the next row
- Figure 5-14 — Live Query Statistics
- Figure 5-15 — Inefficient index seek
- Figure 5-16 — Index Seek operator properties
- Figure 5-17 — Cardinality estimation error in a loop join
- Figure 5-18 — Incorrect cardinality estimation and excessive key lookups
- Figure 5-19 — Index with included columns
- Figure 5-20 — Indexing example: initial execution plan
- Figure 5-21 — Indexing example: plan with the index on the `Customers` table
- Figure 5-22 — Indexing example: final execution plan
- Listing 5-1 — The `Customers` table
- Listing 5-2 — Examining statistics with `DBCC SHOW_STATISTICS`
- Listing 5-3 — Analyzing statistics properties
- Listing 5-4 — Row mode execution: sample query
- Listing 5-5 — Using the `sys.dm_exec_query_statistics_xml` function
- Listing 5-6 — Index seek inefficiency
- Listing 5-7 — Sample query showing Seek Predicate vs. Predicate
- Listing 5-8 — Loop join algorithm (pseudocode)
- Listing 5-9 — Inner merge join algorithm (pseudocode)
- Listing 5-10 — Inner hash join algorithm (pseudocode)
- Listing 5-11 — Join performance: table creation
- Listing 5-12 — Join performance: test cases
- Listing 5-13 — Forcing join types
- Listing 5-14 — Selecting a list of a customer's orders

### Chapter 6 — CPU Load

Why CPU replaced I/O as the usual bottleneck, and the three levers: nonoptimized
queries, compilation/plan caching (parameter sniffing, parameterization), and parallelism.

- Figure 6-1 — Script output showing CPU load history
- Figure 6-2 — Script output showing CPU load per database
- Figure 6-3 — Execution plans of the queries (test 1)
- Figure 6-4 — Execution plans of the queries (test 2)
- Figure 6-5 — Execution plans of the queries (statement-level recompile)
- Figure 6-6 — Execution plan of the stored procedure: parameter-value independence
- Figure 6-7 — Ad-hoc versus parameterized workload throughput
- Figure 6-8 — Plan cache after auto-parameterization
- Figure 6-9 — Throughput with forced parameterization
- Listing 6-1 — Getting CPU load history
- Listing 6-2 — Per-database CPU load
- Listing 6-3 — Parameter-sensitive plans: table creation
- Listing 6-4 — Parameter-sensitive plans: stored procedure
- Listing 6-5 — Parameter-sensitive plans: calling the procedure (test 1)
- Listing 6-6 — Parameter-sensitive plans: calling the procedure (test 2)
- Listing 6-7 — Parameter-sensitive plans: statement-level recompile
- Listing 6-8 — Parameter-sensitive plans: `OPTIMIZE FOR UNKNOWN` hint
- Listing 6-9 — Parameter-value independence
- Listing 6-10 — Dynamic SQL implementation
- Listing 6-11 — Query that would not use filtered index
- Listing 6-12 — Identical queries
- Listing 6-13 — Ad-hoc versus parameterized workload
- Listing 6-14 — Auto-parameterization
- Listing 6-15 — Applying forced parameterization through a plan guide
- Listing 6-16 — Applying simple parameterization through a plan guide

### Chapter 7 — Memory Issues

How SQL Server allocates memory, the memory clerks that matter, query memory
grants and spills, and why a `CHAR(8000)` column can inflate a grant 470×.

- Figure 7-1 — Memory management components
- Figure 7-2 — Memory usage on one of the production servers
- Figure 7-3 — Plan cache content when Optimize for Ad-Hoc Workloads is disabled
- Figure 7-4 — Plan cache content when Optimize for Ad-Hoc Workloads is enabled
- Figure 7-5 — Plan cache content with parameterized query
- Figure 7-6 — Memory grant information in SSMS
- Figure 7-7 — Optimizing memory-intensive queries: query execution plan
- Figure 7-8 — Same plan after the index has been created
- Figure 7-9 — Execution plan with up-to-date statistics
- Figure 7-10 — Cardinality estimation error and memory grant
- Figure 7-11 — Memory grant after `UPDATE STATISTICS`
- Figure 7-12 — Memory grant with `VARCHAR` data type
- Listing 7-1 — Analyzing OS and SQL Server memory usage
- Listing 7-2 — The `sp_server_diagnostics_component_result` event (partial)
- Listing 7-3 — Analyzing memory usage
- Listing 7-4 — Buffer pool usage on a per-database basis
- Listing 7-5 — Running 1,000 ad-hoc queries and examining plan cache content
- Listing 7-6 — Running a parameterized query and examining plan cache content
- Listing 7-7 — Analyzing the plan cache
- Listing 7-8 — Memory grant information
- Listing 7-9 — Optimizing memory-intensive queries: table creation
- Listing 7-10 — Optimizing memory-intensive queries: test query 1
- Listing 7-11 — Optimizing memory-intensive queries: test query 2
- Listing 7-12 — Optimizing memory-intensive queries: outdating statistics
- Listing 7-13 — A hypothetical query (`MIN_GRANT_PERCENT` / `MAX_GRANT_PERCENT`)
- Listing 7-14 — Limiting the amount of memory for In-Memory OLTP
- Listing 7-15 — Analyzing memory consumption of memory-optimized tables
- Listing 7-16 — Detecting the 10 oldest In-Memory OLTP transactions

## Viewing it

Open the HTML file in any browser — no build step. To serve it locally:

```bash
cd docs/chapter-01-summary
python3 serve.py        # http://localhost:8000/
```

Figures and code listings are reproduced from the book for study and reference;
all rights remain with the author and publisher.
