<div align="center">

```
███████╗██╗      █████╗  ██████╗██╗  ██╗   ██████╗ ██████╗ ██████╗ ███████╗
██╔════╝██║     ██╔══██╗██╔════╝██║ ██╔╝  ██╔════╝██╔═══██╗██╔══██╗██╔════╝
███████╗██║     ███████║██║     █████╔╝   ██║     ██║   ██║██║  ██║█████╗
╚════██║██║     ██╔══██║██║     ██╔═██╗   ██║     ██║   ██║██║  ██║██╔══╝
███████║███████╗██║  ██║╚██████╗██║  ██╗  ╚██████╗╚██████╔╝██████╔╝███████╗
╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝   ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
          ██████╗ ███████╗███╗   ███╗ ██████╗ ███████╗
          ██╔══██╗██╔════╝████╗ ████║██╔═══██╗██╔════╝
          ██║  ██║█████╗  ██╔████╔██║██║   ██║███████╗
          ██║  ██║██╔══╝  ██║╚██╔╝██║██║   ██║╚════██║
          ██████╔╝███████╗██║ ╚═╝ ██║╚██████╔╝███████║
          ╚═════╝ ╚══════╝╚═╝     ╚═╝ ╚═════╝ ╚══════╝
```

**Build, stage and run Slack Code demos, from one screen.**

![Python 3.12](https://img.shields.io/badge/python-3.12-3776AB?logo=python&logoColor=white)
![Slack Code beta](https://img.shields.io/badge/Slack%20Code-beta-4A154B?logo=slack&logoColor=white)
![Terminal UI](https://img.shields.io/badge/UI-Textual-F5A623)
![Fork](https://img.shields.io/badge/fork%20of-scastaneda--work-555)

[Quick start](#-quick-start) ·
[What's new](#-whats-new-in-this-fork) ·
[The demo manager](#-1-the-demo-manager) ·
[Private demos](#-4-keep-customer-demos-private) ·
[Story beats](#-7-new-story-beats) ·
[Dependencies](#-dependencies)

</div>

---

> [!NOTE]
> **This is a fork of Sergio's
> [Slack Code Demo Generator](https://github.com/scastaneda-work/Slack-Code-Demo-Generator).**
> His project is the engine: a bot that runs scripted Slack Code and Claude Tag
> demos in your own demo org, the scenario format, the seed scripts, the sample
> stories and the `/build-slack-demo` skill. Read his repo for how those work.
> This README covers only what the fork adds.

## ✨ What's new in this fork

<table>
<tr>
<td width="50%" valign="top">

**🎛️ A demo manager**<br>
`./demo` lists your demos, posts backstories, starts the bot, and tells you
the phrase to type, all on one screen.

**🧩 Stories that plug themselves in**<br>
Drop a story file in and it's live. There's no central list to edit.

**🔇 Mute a demo**<br>
Switch a demo's trigger phrases off before a call, and back on after, with no
restart.

**🔒 Private customer demos**<br>
Keep a customer's demo on your machine while sharing everything else.

</td>
<td width="50%" valign="top">

**♻️ Restorable delete**<br>
Deleted demos go to a trash folder you can restore from.

**🎭 Persona switcher**<br>
Present the bot as Claude, Devin, GitHub or one you create.

**🎬 New story beats**<br>
Design hand-offs, "use this image", a living Plan canvas, and cast members who
post as themselves.

**✅ Stronger checks**<br>
The self-test now catches a broken trigger phrase or a missing file before the
demo, not during it.

</td>
</tr>
</table>

## 🚀 Quick start

```bash
# 1. One-time setup: Slack app, tokens, Python venv
open SETUP.md

# 2. Open the demo manager
./demo

# 3. Pick a demo → Set the scene → Turn on → Kick it off
```

Or open this folder in **Claude Code** and say *"help me set this up"*, then
*"build a demo for &lt;customer&gt;"*. [HANDOFF.md](HANDOFF.md) covers the full
clone → demo → teardown lifecycle.

---

## 🎛️ 1. The demo manager

Run `./demo` for the full-screen app, or `./demo <command>` for the same
features on the command line.

```
┌─ SLACK CODE DEMOS ─────────────────────────────────── ● Bot on  Bot settings ┐
│ Your demos               │  Checkout redesign                                │
│   Acme  1                │  A product team prototypes the new checkout…      │
│   ▸ Checkout redesign    │                                                   │
│                          │  1  Set the scene     [ Post backstory ]          │
│ ▸ Sample demos  8        │  2  Turn on           ● Bot is running            │
│                          │  3  Kick it off       @Claude build the acme…  ⧉  │
│ ＋ New demo              │                                                   │
│                          │  Respond to these phrases  [■ on]                 │
├──────────────────────────┴───────────────────────────────────────────────────┤
│  A Bot settings   N New demo   M More                                        │
└──────────────────────────────────────────────────────────────────────────────┘
```
<sub>Simplified sketch of the layout.</sub>

| I want to… | In `./demo` | On the command line |
|---|---|---|
| See my demos | opens on launch | `./demo list` |
| Post a demo's backstory | **Post backstory** | `./demo run <id> post-backstory` |
| Start or stop the bot | `B` | — |
| Check what a phrase opens | `P` | `./demo route "<phrase>"` |
| Mute a demo | **Respond to these phrases** | `./demo hide <id>` |
| Delete a demo (with undo) | **Delete demo…** · restore with `X` | `./demo delete <id>` · `./demo restore <id>` |
| Check everything is set up | `T` | `./demo check` |
| Switch the agent | `A` | `./demo persona use <slug>` |
| Build a new demo | `N` | — |

Pressing **Return** runs the next step in the checklist.

> [!TIP]
> **Why:** in the original, a demo was a set of loose files you ran from
> memory: the right seed script, the launch command, and a trigger phrase
> buried in the code. `./demo` puts all of it on one screen, so an SE who
> rarely opens a terminal can still run a demo.

### Manifests: what makes a set of files "one demo"

Each demo has a manifest, `demos/<id>.toml`, listing everything it owns:

```toml
name      = "Acme · Checkout redesign"
customer  = "Acme"                              # the group it's listed under
scenarios = ["acme_checkout_redesign"]          # its story file(s)
trigger   = "build the acme checkout redesign"  # the phrase to type in Slack
channels  = ["acme-checkout"]
files     = ["channels/seed_acme_checkout_redesign.py", "docs/demos/acme-checkout-redesign/"]
docs      = [{ label = "Talk track", path = "docs/demos/acme-checkout-redesign/talk-track.md" }]

[[actions]]                                     # each action becomes a button
id    = "post-backstory"
label = "Post backstory"
run   = ["channels/seed_acme_checkout_redesign.py", "--create"]
```

`./demo` builds its list by reading every file in `demos/`, so a new manifest
is a new demo. Field reference: [demos/README.md](demos/README.md).

---

## 🧩 2. Stories register themselves

Each story file now carries its own trigger phrases and its own place in the
matching order:

```python
# scenarios/billing_webhook.py
ROUTE_KEYWORDS = ("billing webhook", "stripe webhook", "durable queue")
ROUTE_PRIORITY = 30          # lower is checked first
```

**Adding a demo, before and after:**

<table>
<tr><th>Original</th><th>This fork</th></tr>
<tr>
<td valign="top">

1. Write `scenarios/acme.py`
2. Add `"acme"` to `_KNOWN` in `scenarios/__init__.py`
3. Add its phrases to `_ROUTE_KEYWORDS`, at the right position
4. Restart the bot

</td>
<td valign="top">

1. Write `scenarios/acme.py`, with its phrases inside it
2. Restart the bot

</td>
</tr>
</table>

**What happens on an @-mention:**

```
"@Claude roll back the migration"
        │
        ├─ build/fix word?    "roll back" ✓
        │
        ├─ build the list:    every loaded story − muted ones, sorted by priority
        │                       30  billing_webhook     ✗
        │                       40  checkout_incident   "roll back the" ✓  ← opens
        │                       60  sql_migration       "migration" ✓  (never reached)
        │                       90  website_redesign
        │
        └─ nothing matched?   → freeform (the live agent builds from scratch)
```

> [!TIP]
> **Why:**
> - Adding or removing a demo is one file, so there's no second list to
>   forget. In the original, forgetting it meant a phrase silently opened the
>   wrong demo.
> - No shared file has to name your story, which is what makes
>   [private demos](#-4-keep-customer-demos-private) possible.
> - A broken story file is skipped and reported instead of stopping the bot.
> - The order is fixed. The original picked Tag stories from an unordered set,
>   so two Tag stories sharing a phrase could swap after a restart.

<details>
<summary><b>Under the hood</b></summary>

- **At startup**, `scenarios/__init__.py` imports every module in the folder
  (names starting with `_` are skipped) to form `_KNOWN`. Import failures land
  in `DISCOVERY_ERRORS`, which the self-test reports.
- **On every @-mention**, `route_table()` reads the mute list, takes
  `_KNOWN − muted`, and sorts the rows by `(ROUTE_PRIORITY, slug)`.
  `route_scenario()` returns the first story with a keyword found in the
  lowercased message.
- The list is rebuilt per mention **only so muting needs no restart**. That
  costs one small file read and a sort of about ten rows. Adding or deleting a
  story file still needs a bot restart.
- Once a code channel opens, it's locked to its story. Follow-ups never route
  again.
- `scenarios_tag/` works the same way, with `KEYWORDS` in place of
  `ROUTE_KEYWORDS`.

</details>

---

## 🔇 3. Mute a demo

Switch off **Respond to these phrases** on a demo's page, or run
`./demo hide <id>` (and `./demo unhide <id>` to undo). Its trigger phrases stop
opening it, and the page shows where the phrase goes instead.

- **Nothing is deleted.** The demo stays in the list, marked muted.
- **No restart.** The bot checks the mute list on every @-mention.
- **Open sessions keep working.** A code channel that's already open is locked
  to its story.

> [!TIP]
> **Why:** before a call with one customer, mute another customer's demo so a
> stray phrase can't open the wrong story. The original had no way to switch a
> demo off short of deleting it.

<details>
<summary><b>Under the hood</b></summary>

`./demo` writes the demo's story names to `.demo_manager_state.json`
(git-ignored, per machine). The bot only ever reads that file; `./demo` only
ever writes it. A missing or broken file means "nothing muted".

```json
"hidden_demos":     { "welloguard-redesign": { "scenarios": ["website_redesign"] } },
"hidden_scenarios": ["website_redesign"]
```

</details>

---

## 🔒 4. Keep customer demos private

A demo built for a real customer shouldn't be pushed back to the shared repo,
but you still want it working on your machine.

**1. List its files in `.git/info/exclude`.** It works exactly like
`.gitignore`, but it's never shared, so the customer's name doesn't appear in a
shared file either.

```
scenarios/acme_*
channels/seed_acme_*
demos/acme-*
docs/demos/acme-*/
```

**2. Put Claude Code notes about it** in `CLAUDE.local.md` at the repo root.

**3. Put extra self-test checks** in `qa_local/<name>.py`: a module with
`run() -> int` that returns its failure count. `qa.py --self-test` runs every
file there when the folder exists.

`CLAUDE.local.md` and `qa_local/` are already git-ignored, and
`/build-slack-demo` asks whether a new customer demo should stay private and
sets this up for you.

> [!IMPORTANT]
> Exclude the files **before** you commit the demo. Git keeps tracking files
> it has already committed. If you already have, run `git rm --cached <file>`
> to stop tracking them; the files stay on disk.

> [!TIP]
> **Why it works:** a demo in this fork is made only of its own new files. The
> bot, `./demo` and the self-test find them by looking in their folders, so no
> shared file mentions them. On your machine the files exist and everything
> sees the demo. In the shared copy they don't, and nothing looks for them.

---

## ♻️ 5. Restorable delete

```bash
./demo delete acme-checkout-redesign    # shows what will move, then moves it to .trash/
./demo trash                            # list deleted demos
./demo restore acme-checkout-redesign   # put it back
```

Every file the demo owns moves at once: manifest, story, seed, docs and art.
Files another demo also uses stay put. Sample demos can only be muted, not
deleted, and nothing in Slack is touched.

> [!TIP]
> **Why:** removing a demo in the original meant deleting files and list
> entries by hand, with no undo.

---

## 🎭 6. Switch the agent persona

The bot can present as any AI agent. This fork adds **Devin** and **GitHub**
personas next to **Claude**, plus a switcher:

```bash
./demo persona                                   # list
./demo persona use devin                         # switch
./demo persona new "Cursor" --maker "Anysphere"  # create one
```

Or press `A` in `./demo`. Switching updates the name Slack shows and the way
the bot talks together, and restarts the bot if it's running.

> [!NOTE]
> Slack doesn't let an app change its own picture. Upload that in the app's
> settings (**Open app settings** in the same window).

> [!TIP]
> **Why:** show the story with the agent the customer actually uses, without
> editing config files.

---

## 🎬 7. New story beats

Optional hooks a story can define to add moments to the demo. Every beat is
pre-baked, so it renders instantly and the same way every time.

| Beat | What the audience sees | Hooks |
|---|---|---|
| 🖼️ **Asset review** | Someone shares a design link (Canva, Figma…) and a designer character replies with a review. The link never goes to the live agent. | `participant_beats()` · `phase: "on_asset"` |
| 🔁 **"Use this image"** | The preview swaps in the new artwork, combining with the patch in either order. | `IMAGE_EDIT_PHRASES` · `image_diff()` · `image_edit_report()` |
| ➕ **Second pre-baked edit** | A follow-up ask, such as adding a carousel slide, lands instantly. | `SLIDE_EDIT_PHRASES` · `slide_diff()` · `slide_edit_report()` |
| 💬 **Reaction after the swap** | A cast member responds once the new image is in. | `phase: "on_image"` |
| 📋 **Living Plan canvas** | A Plan tab that ticks off steps as each beat lands. | `plan_canvas()` |
| ⚡ **Scripted replies** | An on-story first reply, next-step hint and dashboard reply. The opening reply skips the live agent, so it's instant. | `opening_reply()` · `first_pass_hint()` · `metrics_report()` |
| 🪶 **Fallback preview** | If Slack rejects a large image page, a smaller version is tried. | `preview_fallbacks()` |
| 👤 **Cast as real people** | A chime-in posts as that real user when their token is in `tokens.json`, and is spoofed by name otherwise. The bot ignores those posts. | `PARTICIPANTS[].email_stem` · `tokens.json["users"]` |

Full signatures are in the docstring at the top of
[`scenarios/__init__.py`](scenarios/__init__.py).

> [!TIP]
> **Why:** demos with a design hand-off, such as marketing pages and campaigns,
> needed more than the original check → patch → recap.

---

## ✅ 8. Checks

`qa.py --self-test` now also verifies:

- [x] every **manifest** parses, every file it lists exists, and its trigger
      opens its own story
- [x] every **story file** loads and belongs to exactly one demo
- [x] the **new story-beat plumbing**, independent of any one story
- [x] your **private checks** in `qa_local/`

It ignores whatever you've muted, so muting can't change the results. The
unit tests (`pytest`) cover the manager and the terminal UI.

---

## 📦 Dependencies

Two new packages. Both are in `requirements.txt`, so the usual
`.venv/bin/pip install -r requirements.txt` picks them up.

| Package | Why it's needed | Used by |
|---|---|---|
| [`textual`](https://textual.textualize.io/) `>=8.2,<9` | The full-screen terminal UI. It also brings in [`rich`](https://github.com/Textualize/rich) for colour and layout. | `./demo` |
| [`pytest-asyncio`](https://pypi.org/project/pytest-asyncio/) | Lets the async unit tests run (2 tests were failing without it). | `pytest` only |

**Python:** 3.11 or newer, because the manifests are read with the standard
library's `tomllib`. **3.12 is recommended**, as before.

Everything else `./demo` uses (`pty`, `termios`, `subprocess`) is part of the
standard library on macOS and Linux.

---

## 🗂️ What's new in the folder

```
.
├── demo                     launcher: ./demo
├── demokit/                 the demo manager
│   ├── manifest.py            reads demos/*.toml
│   ├── routing.py             "which demo does this phrase open?"
│   ├── state.py               mute list + run log
│   ├── actions.py             runs a demo's buttons (seed scripts)
│   ├── trash.py               delete → .trash/, restore
│   ├── health.py              per-demo and machine checks
│   ├── personas.py            list / switch / create personas
│   ├── bot.py                 start and stop the bot
│   ├── cli.py                 ./demo <command>
│   └── tui/                   the full-screen UI
├── demos/                   one manifest per demo
├── personas/
│   ├── devin.md               new
│   └── github.md              new
├── tests/
│   ├── test_demokit.py        new
│   ├── test_personas.py       new
│   └── test_tui.py            new
├── qa_local/                (git-ignored, optional) private checks
└── CLAUDE.local.md          (git-ignored, optional) private Claude Code notes
```

Everything else (the bot, `agent/`, `listeners/`, `scenarios/`,
`scenarios_tag/`, `channels/`, `qa.py`, `run.sh`) comes from the original
project, with the changes described above.

---

<div align="center">

**Built on [Sergio's Slack Code Demo Generator](https://github.com/scastaneda-work/Slack-Code-Demo-Generator).**<br>
Every artifact is a prop. There's no real repo, no real GitHub, and no real CI.

</div>
