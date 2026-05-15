# ─── STUDENT MANAGEMENT SYSTEM (Short Version) ───────────────
students = {}  # Main dictionary
 
# ── Helpers ───────────────────────────────────────────────────
def grade(pct):
    return "A" if pct >= 80 else "B" if pct >= 65 else "C" if pct >= 50 else "Fail"
 
def avg(marks):0
    return round(sum(marks) / len(marks), 2) if marks else 0
 
def show(r):
    s = students[r]
    pct = avg(s["marks"])
    print(f"\n  Roll: {r} | Name: {s['name']} ({s['name'].upper()})")
    print(f"  Subjects (tuple): {s['subjects']}")
    print(f"  Marks    (list) : {s['marks']}")
    print(f"  Percentage: {pct}% | Grade: {grade(pct)}")
 
# ── 1. Add Student ────────────────────────────────────────────
def add():
    r = int(input("Roll No: "))
    if r in students:
        print("Already exists!"); return
    n    = input("Name: ").strip().title()          # .title()
    subs = tuple(input("Subjects (comma): ").split(","))   # tuple
    mks  = list(map(int, input("Marks (comma): ").split(",")))  # list
    students[r] = {"name": n, "subjects": subs, "marks": mks}
    print(f"✅ '{n}' added! | upper→ {n.upper()} | find 'a'→ {n.lower().find('a')}")
 
# ── 2. Display All ────────────────────────────────────────────
def display():
    if not students: print("No records."); return
    print(f"\n Total: {len(students)} student(s)")
    for r in students: show(r)
 
# ── 3. Search ─────────────────────────────────────────────────
def search():
    r = int(input("Roll to search: "))
    show(r) if r in students else print("Not found.")  # if-else
 
# ── 4. Update ─────────────────────────────────────────────────
def update():
    r = int(input("Roll to update: "))
    if r not in students: print("Not found."); return
    c = input("Update (n)ame or (m)arks? ")
    if c == "n":
        students[r]["name"] = input("New name: ").strip().title()
    elif c == "m":
        students[r]["marks"] = list(map(int, input("New marks (comma): ").split(",")))
    print("✅ Updated!")
 
# ── 5. Delete ─────────────────────────────────────────────────
def delete():
    r = int(input("Roll to delete: "))
    if r in students: del students[r]; print("✅ Deleted.")
    else: print(" Not found.")
 
# ── 6. Result ─────────────────────────────────────────────────
def result():
    for r, s in students.items():
        pct = avg(s["marks"])
        print(f"\n  {s['name']} | {pct}% | Grade: {grade(pct)}")
        # marks.count() — count how many scored above 75
        print(f"  Scores >75: {sum(1 for m in s['marks'] if m > 75)}")
 
# ── Bonus: Topper ─────────────────────────────────────────────
def topper():
    if not students: print("No records."); return
    t = max(students, key=lambda r: avg(students[r]["marks"]))
    print(f"\nTopper: {students[t]['name']} | {avg(students[t]['marks'])}% | Grade: {grade(avg(students[t]['marks']))}")
 
# ── Menu ──────────────────────────────────────────────────────
menu = {"1": add, "2": display, "3": search, "4": update, "5": delete, "6": result, "7": topper}
 
while True:
    print("\n1.Add 2.Display 3.Search 4.Update 5.Delete 6.Result 7.Topper 0.Exit")
    c = input("Choice: ")
    if c == "0": print("Bye!"); break
    elif c in menu: menu[c]()
    else: print("Invalid!")
 
