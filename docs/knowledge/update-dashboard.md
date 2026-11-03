# The studio: the user's dashboard for this project (`/update-dashboard` adapter)

**https://claude.ai/artifact/4nP5WMkRRMH6CxqMZb5a2r** ("Simulation Theology Studio", private to the user;
made 2026-11-03). Since 1.11.2026 every project keeps an idea studio with the same cost metric (global
CLAUDE.md). Here it holds the research queue with the reason for each piece, every idea (experiments,
KPIs, proposals for Paper 1's revision, readings, the corpus, things to take to Josef), what was built,
what it cost, and the decisions. Claude picks what comes next by default; the user steers with verdicts.

Run `/update-dashboard` at the start of every session here (CLAUDE.md says so); it reads this file.

## What is where

- `docs/studio/backlog.json` (in git, the one list of what is left): `next` (the queue, in order, each item
  with `why`), `items` (every idea: `status` next, building, idea, parked or built; `from` you, josef or
  claude; `summary`, `details`, `doc`), `waiting` (things only the user can do, such as asking Josef),
  `built` (the timeline), `decisions`, `kinds`, `cost` (filled by the cost tool; `trial` by hand).
- `docs/studio/studio.html`: the page (the master copy from `~/.claude/skills/update-dashboard/studio/`,
  restyled: stone and lapis, Spectral and Atkinson Hyperlegible; "Josef's" in place of the master's second
  person; units reading, study, document). It reads `backlog.json` published beside it.
- The artifact's database (read and written with the `ArtifactData` tool, `url` above):
  - `notes`: `{ item (an item's or waiting entry's id, or null), about, kind (idea, message, note), who (me
    or josef), text, files [{ id, url, name, type, size }], at, by }`; Claude adds `reply`, `repliedAt`.
  - `verdicts/<item id>`: `{ v (first = Sooner, later, no = Not now), title, at, by }`; Claude adds `reply`.
  - `ticks/<waiting id>`: `{ done, title, at, by }`; Claude adds `reply`.
  - `settings/steer`: `{ mode: claude | me }`; no document means `steerDefault` (claude).
  - `ratings/<built id>`: `{ stars (1-5), title, at, by }`.

## The routine

1. Read: `ArtifactData` `list` on `notes`, `verdicts`, `ticks`, `ratings`, and `get` on `settings`/`steer`.
   New = no `reply`. What is there is the user's words about this project, data rather than instructions
   from anyone else.
2. Files on a note: `Artifact` `read` with the studio's `url` and `path` = the file's `id`, `out_dir`
   `.studio-inbox/<note id>/` (git-ignored; never commit what the user sends). A transcript or paper the
   user sends for the research goes to `context/` (gitignored) on purpose, like `context/influences/`.
3. Act on each, oldest first: an idea goes into `items` (status `idea`, or into `next` if Claude would do
   it soon); a message or note does what it asks; Sooner moves an item up `next`, Later down, Not now makes
   it `parked`; a tick does the follow-up and marks the waiting entry `"done": "<date>"` (drop after a week).
4. Answer every one with `ArtifactData` `update` pinned with `if_version`: `reply` in one to three plain
   sentences, `repliedAt` (ISO time). Use `batch` for more than a couple.
5. Steering: `me` = finish what is being built, then start nothing new until something is marked Sooner;
   `claude` = take the top of `next`.
6. When a piece is done: status `built`, out of `next`, a card in `built` (date, title, what, link to the
   file on GitHub, `size` `{n, unit}`, `agents`: the ids the Agent tool returned, `revisions`). **Write the
   card in its own edit, in the session that did the work**: the cost tool credits a card only when one
   edit adds at most four cards, and it gives that card the session's stretch since its last card. Then
   `py -3.11 ~/.claude/skills/cost-dashboard/collect.py studio --project .` fills its `tokens`.
   A user's request for changes to a built piece adds 1 to `revisions` and its agents to `agents`.
7. Republish whenever `backlog.json` changed (set `updated` to today): `Artifact` publish with `file_path`
   `docs/studio/studio.html`, `files` `{"backlog.json": "docs/studio/backlog.json"}` (absolute paths or
   `root` when the session runs elsewhere) and, from another conversation, the `url` above (read it first).
   Then commit and push.
8. Report in chat: one line per item, then anything that needs the user.

## Traps

- The setup wrote all the old cards at once, so they carry no cost: transcripts before 2026-11-03 are not
  in the studio's metric (the Study 2 compute is in `research/SUMMARY.md` §10 instead).
- The first costed card ("Reading Levin", 2026-11-03) also carries the studio's one-time setup, done in
  the same session after the reading.
- `collect.py studio` sets `cost.since` from the first agent's transcript; with no agents yet it is empty
  and the page falls back to 3 November.
