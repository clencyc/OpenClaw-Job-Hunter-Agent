# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:
- Custom automation hooks
- Local script wrappers
- Environment-specific runtime credentials
- Anything unique to your local machine layout

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update core skills without losing your custom tool overrides.

---

## Custom Job Hunting Tools

### fetch_new_listings
Description: Scrapes Google and major job boards for fresh FastAPI or Django backend developer application pages. Returns a list of text URLs.
Inputs: none

Execution:
```bash
python3 ~/.openclaw/workspace/fetch_jobs.py
```

### run_job_applier
Description: Runs an autonomous browser agent that takes a job posting URL, reads my local resume text, and fills out the application form fields automatically.
Inputs:
- url: string (The application link or job board URL)

Execution:
```bash
python3 ~/.openclaw/workspace/run_applier.py --url "{{url}}"
```

---

## Related

- [Agent workspace](/concepts/agent-workspace)