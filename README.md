# 🎛️ Perpetuum

Moves your mouse in an infinity loop inside the app window. `ENTER` to start, `SPACE` to stop.

```bash
python3 -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python main.py          # run
./build.sh               # build & install Perpetuum.app (needs Accessibility permission)
```

## Accessibility permission

Cursor doesn't move / macOS blocks it? Grant Perpetuum access:

1. Open System Settings → Privacy & Security → Accessibility (or run `open "x-apple.systempreferences:com.apple.preference.security?Privacy_Accessibility"`).
2. Add `/Applications/Perpetuum.app` (or toggle it on if already listed).
3. Still broken after a rebuild? Remove it (`−`) and re-add — `./build.sh` re-signs the binary, which can invalidate the old grant.
