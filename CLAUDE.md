# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

Perpetuum: a ~70-line PyQt6 app, all in `main.py`, that moves the cursor in an infinity loop inside its own window (logo as background). No tests, no linter, no other files worth reading.

## Commands

```bash
source venv/bin/activate && python main.py   # run
./build.sh                                    # build + install Perpetuum.app (regenerates InfinityCursor.spec/entitlements.plist)
./clear.sh                                    # remove build/dist/spec/installed app
```

## How it works

- `running`/`speed` are module globals shared between the Qt main thread and the `move_cursor` daemon thread — that's the pattern, keep it.
- Path is a Lissajous curve relative to the window's own geometry, not the screen.
- `ENTER`/`SPACE` (keyPressEvent) start/stop; `mousePressEvent` swallows clicks while running.
- Naming is inconsistent on purpose to leave alone: `InfinityCursor.spec`/`clear.sh` say `InfinityCursor`, `build.sh` builds `Perpetuum.app`.

## Edit rules

Philosophy: keep bloat minimal. Do smallest possible edits, same file, same globals-and-functions style. No new files, classes, deps, error handling, config, tests, or unrequested cleanup/refactors — including the naming mismatch above. If a change grows the line count, it needs a reason.
