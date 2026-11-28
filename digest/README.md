# Open-source digest

A regularly updated digest of open-source projects that serve Nigerians and West Africans, at home and in the diaspora. It covers land and title, property and rent, farm and farm data, prices and payments, shipping and pickup, messaging, identity and trust, and directories of Nigerian open-source projects. Editions are published in [docs/digest/](../docs/digest/). See [issue #6](https://github.com/Erriccc/jappa-labs/issues/6).

## What is here

- `watchlist.yml` lists the projects we follow, each with a one-line description and a category. Our own projects are in the `own` group: editions show them in a separate "From Jappa Labs" section and never rank them with the others. A description must not contain ` #`, which starts a comment.
- `scan.py` reads public GitHub data for each project and records what shipped.
- `data/YYYY-MM-DD.json` holds the results of each scan.
- `render.py` builds a weekly edition from the scan files.
- `tests/` holds the tests for `render.py` and the site. Run them with `python3 -m unittest discover -s digest/tests`.

## Run the scan

You need Python 3. The script uses only the standard library.

```bash
python3 digest/scan.py
```

For each project it records counts over the last 90 days (change this with `--days N`):

- commits on the default branch (count and authors). Each listed commit has an `author` (the GitHub login, or the git name if GitHub can't match an account) and a `login` (the GitHub login, or `null`). Files from before 28 November 2026 have no `login`;
- pull requests opened and merged;
- issues opened and closed (pull requests are not counted as issues);
- releases;
- stars, forks and licence.

To keep the daily data files small, the lists of individual commits, pull requests, issues and releases only include items created or updated in the last day (change this with `--detail-days N`). For a full edition scan, with every item in the 90-day window listed, run:

```bash
python3 digest/scan.py --detail-days 90
```

It also records, for each project:

- fork history: the number of forks created in each month since the repo was created. GitHub only lists forks that still exist, and the scan reads at most 1,000 (newest first), so the total can be lower than the fork count.
- dependents: if the project is a published package that [deps.dev](https://deps.dev) knows about, the number of packages that depend on its default (usually latest) version. Otherwise this is `null`.

It writes `digest/data/YYYY-MM-DD.json` and prints a short markdown summary.

### Star growth

GitHub does not let us list who starred a repo we do not own, so star history cannot be rebuilt from the past. Instead, each daily scan records the star count. Star growth can be built from these daily snapshots, starting on 25 November 2026.

The script works without a token, but GitHub allows only 60 unauthenticated requests an hour. To scan the full list, set `GITHUB_TOKEN` or `GH_TOKEN` in your environment. A token with no extra scopes is enough, as all data is public. If a repo cannot be found, or the rate limit is reached, that repo is marked in the output and the scan carries on.

## Render an edition

```bash
python3 digest/render.py --if-due
```

Editions are weekly; the scan is daily. `render.py` reads the scan files from the last 7 days and writes `docs/digest/YYYY-MM-DD-edition-N.md`, numbered after the newest edition there. It credits the people behind each project, with a profile link when the GitHub login is known, and lists:

- **Builders this week:** projects with commits or merged pull requests recorded in the week, counted from the daily commit lists without duplicates. Accounts ending in `[bot]` are left out. Star changes are against the scan from a week earlier, when there is one.
- **Shipped:** releases and merged pull requests from the week.
- **From Jappa Labs:** the `own` group, without bot commits.

Options:

- `--if-due` writes an edition only if 7 or more days have passed since the newest one. `--force` writes one anyway.
- `--date YYYY-MM-DD` picks the scan to render (default: the newest), and `--data-dir` and `--out-dir` change where files are read and written.

It never overwrites an edition, and it skips the edition if more than 20% of repos failed to scan. Text from repos is escaped, so it can't break the Jekyll build.

## Automation

A [GitHub Actions workflow](../.github/workflows/digest-scan.yml) runs the scan every day, renders an edition when one is due, and commits the results. To publish an edition now, run the workflow by hand with **force_edition** ticked. A [Pages workflow](../.github/workflows/pages.yml) then rebuilds the site.

## Suggest a project

Know a project we missed? Suggestions and corrections are welcome in [issue #6](https://github.com/Erriccc/jappa-labs/issues/6).
