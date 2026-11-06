# sql

A chapter-by-chapter study guide to **SQL Cookbook**, 2nd edition — Anthony Molinaro &
Robert W. de Graaf (O'Reilly, 2020). Plain-English summaries of all fourteen chapters **and both appendices**, the book's own code,
result sets, and page images cropped from the PDF.

**Open it:** [`sql-cookbook-study-notes.html`](sql-cookbook-study-notes.html)
(`index.html` redirects here.)

## Chapters covered

| Chapter | Topic | Recipes |
|---|---|---|
| 1 | Retrieving Records | 14 |
| 2 | Sorting Query Results | 6 |
| 3 | Working with Multiple Tables | 12 |
| 4 | Inserting, Updating, and Deleting | 17 |
| 5 | Metadata Queries | 7 |
| 6 | Working with Strings | 17 |
| 7 | Working with Numbers | 17 |
| 8 | Date Arithmetic | 7 |
| 9 | Date Manipulation | 13 |
| 10 | Working with Ranges | 5 |
| 11 | Advanced Searching | 12 |
| 12 | Reporting and Reshaping | 20 |
| 13 | Hierarchical Queries | 5 |
| 14 | Odds 'n' Ends | 13 |
| A | Window Function Refresher | 13 sections |
| B | Common Table Expressions | 3 sections |

Highlights per chapter:

- **1** — `SELECT`/`WHERE`, aliases and inline views, concatenation, `CASE`, row limiting,
  random rows, `NULL` handling, `LIKE`.
- **2** — `ORDER BY`, multi-column sorts, sorting by substrings, mixed alphanumeric data
  (`TRANSLATE` + `REPLACE`), placing `NULL`s, `CASE`-driven sort keys.
- **3** — set operations, equi-joins, `INTERSECT`, the `NOT IN` NULL trap, anti-joins,
  comparing two tables, Cartesian products, aggregates across joins, `FULL OUTER JOIN`.
- **4** — `INSERT` variants, `DEFAULT` vs explicit `NULL`, copying tables, multi-table
  inserts, scoped `UPDATE`, updating from another table in five dialects, `MERGE`, and the
  delete recipes (orphans, duplicates, referenced rows).
- **5** — catalog queries for tables, columns, indexes and constraints, finding foreign keys
  without indexes (an anti-join over the catalog), SQL that generates SQL, and Oracle's
  `DICTIONARY` / `DICT_COLUMNS`.
- **6** — walking a string one character at a time with the `T10`/`T100` counter tables,
  doubled quotes, counting occurrences by length difference, removing characters with
  `TRANSLATE` + `REPLACE`, separating letters from digits, the alphanumeric test, extracting
  initials, sorting by parts of a string, rows ⇄ delimited lists (`LISTAGG`, `GROUP_CONCAT`,
  `STRING_AGG`, `SYS_CONNECT_BY_PATH`), alphabetizing, parsing IP addresses, `SOUNDEX`, and
  finding text that does *not* match a regex.
- **7** — the five aggregates and what `GROUP BY` does to them, `COUNT(*)` vs `COUNT(col)`,
  the NULL-in-aggregates trap, running totals with `SUM() OVER`, running products via
  `ln`/`exp`, moving averages with `LAG`, mode (`DENSE_RANK`, Oracle's `KEEP`), median
  (`PERCENTILE_CONT`, `MEDIAN`), percentage of a total, trimmed means, the median absolute
  deviation, and Benford's law.
- **8** — adding days, months and years in five dialects, the days-between-two-dates idiom
  (two single-row inline views), business days via a `T500` expansion with a weekend `CASE`
  flag, months/years between, seconds/minutes/hours by multiplication, counting each weekday
  in a year (recursive CTE, `CONNECT BY`, `generate_series`, `T500`), and the gap to the next
  record with `LEAD` — including the tie problem and the `lead(date, cnt-rn+1)` fix.
- **9** — leap years by asking February how long it is, days in a year, extracting time units,
  first/last day of a month, every Friday in a year, first and last Monday of a month
  (`next_day(d-1,…)`), **a printable calendar** built by pivoting days into seven columns,
  quarter start/end dates for the year and for a given `20051`-style code, filling in missing
  months with `LEFT JOIN` + `count(col)`, searching on month/weekday names, comparing rows by
  month and weekday, and detecting overlapping date ranges — by self-join and by `LEAD`.
- **10** — ranges as neighbours: `LEAD(proj_start) = proj_end` to find consecutive rows,
  `LEAD`/`LAG` with `PARTITION BY` to compare rows inside a group (plus the `cnt-rn+1` fix for
  tied hire dates), the **gaps-and-islands** idiom (flag each break, running-sum the flags,
  group by the result), filling missing years with a generated range and a `LEFT JOIN`,
  and generating numbers on demand with a recursive `WITH`, `generate_series` or Oracle's
  `MODEL` clause.
- **11** — pagination with `ROW_NUMBER`, skipping rows with `MOD`, the `ON`-clause rule that
  keeps an outer join from collapsing (and the departments that vanish when you get it wrong),
  reciprocal rows found by self-join, `DENSE_RANK` vs `RANK` vs `ROW_NUMBER` for "top n",
  table-wide `MIN`/`MAX` over `()`, `LEAD`/`LAG` shifts with wrap-around, suppressing duplicates
  without `DISTINCT`, **knight values** (the book's only real diagram), and forecasts made by
  cross-joining a three-row numbers table.
- **12** — reshaping a result set: `CASE` + `SUM` to pivot rows into columns (one row or many,
  with `ROW_NUMBER` as the key), cross-joining to unwrap columns back into rows, `LAG` to blank
  out repeated report values, pivot-then-subtract for inter-row maths, buckets by fixed size
  (`ceil(rn/5.0)`) and by fixed count (`NTILE`), horizontal (`LPAD`/`REPEAT`/`REPLICATE`) and
  vertical histograms, window functions in place of `GROUP BY`, `ROLLUP` / `CUBE` /
  `GROUPING SETS` with `GROUPING()` to label every subtotal, `CASE` flag columns, sparse
  matrices, five-second transaction buckets, three counts over three partitions at once, and a
  90-day moving sum with everything pivoted into a report.
- **13** — trees stored as self-references: the parent-child self-join (and the
  `NULL`/equi-join rule that silently drops the root), child-parent-grandparent as a
  **recursive CTE** (`with x (tree, mgr, depth) as (anchor union all step)`) versus Oracle's
  `sys_connect_by_path` + `connect by prior`, the full org chart built downwards from
  `where mgr is null`, subtree queries for one manager, `lpad('.', 2*level, '.')` indentation,
  and classifying rows as leaf / branch / root with three `sign(count(*))` subqueries or
  `connect_by_isleaf` / `connect_by_root`.
- **14** — the "fun" chapter, one vendor at a time: SQL Server's `PIVOT` and `UNPIVOT`,
  Oracle's `MODEL` clause (arrays, `rules iterate … until`) used for both transposing and
  converting numbers to binary, `INSTR`+`SUBSTR` landmark parsing, days-in-a-year via
  `to_char(…,'DDD')`, `TRANSLATE` to spot mixed alphanumeric strings, a ranked pivot of the top
  3 / next 3 / the rest, a double pivot with department headers (`sum(flag1) over …` as a row
  number), object types as a "composite subquery", parsing colon-delimited strings into rows,
  `RATIO_TO_REPORT` percentages, and `max(pass_fail) over (…)` to test a value across a group.
- **A** — the window-function refresher, in order: what grouping buys you, the two-rule
  definition of an SQL group proved with queries, the **NULL group paradox**
  (`count(name)` = 0 in a group that exists — rows vs values), the real rule for what must appear
  in `GROUP BY` (constants and scalar subqueries need not), `count(*) over ()` as the switch that
  stops collapsing, the evaluation order (`WHERE` → windows → `ORDER BY`), partitions as a moving
  `GROUP BY`, NULLs inside partitions, why `order by` inside `over` turns `SUM` into a running
  total, the framing clause read clause by clause, a nine-column `MIN`/`MAX` finale, the
  one-query-versus-three-subqueries performance argument, and window functions in an inline view
  as the base for a formatted report.
- **B** — CTEs as named derived tables: the double aggregate that forces a subquery
  (`max(count(*))` is illegal), why MySQL/PostgreSQL/SQL Server demand an alias and Oracle does
  not, the `with x (col, …) as (…)` form with the column list *before* the body, stacking several
  CTEs with commas, and the recursive Fibonacci (`with recursive … anchor union all step …`),
  `RECURSIVE` being required in MySQL/Oracle/PostgreSQL but not SQL Server/DB2, and the
  `WHERE` clause as the loop's only brake.

## What's in the page

- 325 SQL code blocks with syntax highlighting and copy buttons; tabbed
  DB2 / MySQL / PostgreSQL / Oracle / SQL Server variants where dialects differ.
- 318 figures cropped from the book's PDF, each captioned with its page number.
- Result sets reproduced as real HTML tables so they stay readable on small screens.
- A combined cheat sheet and lightbox galleries of all 528 pages covered (497 chapter pages
  plus the 27 + 4 appendix pages).
- Self-contained single file: no dependencies, dark mode and print-to-PDF built in.

Images live in `assets/ch1/` … `assets/ch14/`, plus `assets/appa/` and `assets/appb/`.
