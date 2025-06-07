# To-Do List CLI (Because Simplicity is Overrated)

Welcome to the *ultimate* productivity weapon of 1996 — the Command Line To-Do List!  
Tired of sleek GUIs and modern UX? Us too. Get back to your roots. Suffer productively.

## Features That Barely Compete with Post-it Notes

- **Add Tasks** — Like writing on a sticky note, but with more keystrokes.
- **View Tasks** — See your tasks in all their monochrome glory.
- **Mark as Done** — Because nothing screams satisfaction like toggling a boolean.
- **Delete Tasks** — Ctrl+Z for your soul.
- **Auto-Priority Magic** — We guess what's urgent. Hope you're cool with that.
- **Search** — Type like your life depends on it.
- **Filter** — Because you deserve to procrastinate more efficiently.

## 📁 File Structure (So Minimal It Hurts)
```

ToDoList\
│
├── main.py              # The main loop — all roads lead here
├── task.py              # The task blueprint. Godlike class.
├── task\_manager.py     # Business logic pretending to be a manager
├── utils.py             # Functions you won’t remember writing
├── ui.py                # yes....UI
├── todolist.json        # Your precious digital post-its
└── README.md            # You're reading it. Congrats.

````

## Dependencies (A Fancy Word for "Stuff That Breaks Later")

* `tabulate` – For pretending CLI can look good
* `colorama` – Because black and white is too honest
* `datetime` – So you can miss deadlines in ISO format

Install them manually if you like pain:

```bash
pip install tabulate colorama
```

## How It Works (Or Pretends To)

Tasks are saved as JSON. When you quit, they persist. When you return, they haunt you.

### Task Schema (A Glorified Dictionary)

```json
{
  "id": 1,
  "title": "Do something probably important",
  "description": "Maybe related to work, maybe not.",
  "status": "Not Finished....yet",
  "priority": "High",
  "deadline": "2025-06-09",
  "estimated_time": 45,
  "created_at": "2025-06-07T22:00:00"
}
```

## Known Bugs (A.K.A. Features in Beta)

* No cloud sync. Because your terminal doesn't need it.
* Deleting tasks is forever. No undo. Welcome to adulthood.
* Filtering will judge your priorities. Harshly.

## Contributing

Pull requests welcome — but expect sarcasm in the reviews.

## License

MIT. Use it, abuse it, modify it, rename it, sell it. Just don't call it "AI."

---

> “Why use a sleek, modern productivity app when you can suffer like a true developer?”
> — Probably no one, but still.

