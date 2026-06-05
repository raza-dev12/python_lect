import os

FILE = "books.txt"

def load():
    if not os.path.exists(FILE): return {}
    with open(FILE, "r") as f:
        # Dictionary format: {ID: [Name, Author, Price, Qty, Status]}
        return {l.split('|')[0]: l.strip().split('|')[1:] for l in f if l.strip()}

def save(data):
    with open(FILE, "w") as f:
        for k, v in data.items(): f.write(f"{k}|{'|'.join(map(str, v))}\n")

def get_num(prompt, is_int=False):
    while True:
        try:
            val = int(input(prompt)) if is_int else float(input(prompt))
            if val >= 0: return val
            print(" Value negative nahi ho sakti!")
        except ValueError: print("Invalid Number!")

# --- FEATURES ---
def add_book(data):
    bid = input("Book ID: ").strip()
    if bid in data or not bid: return print(" Invalid/Duplicate ID!")
    name, auth = input("Name: "), input("Author: ")
    qty = get_num("Quantity: ", True)
    price = get_num("Price: $")
    data[bid] = [name, auth, price, qty, "Available" if qty > 0 else "Out of Stock"]
    save(data); print("Book Added!")

def view_books(data):
    if not data: return print(" Library khali hai.")
    print(f"{'ID':<6} | {'Name':<20} | {'Author':<15} | {'Price':<8} | {'Qty':<5} | {'Status'}")
    for k, v in data.items():
        print(f"{k:<6} | {v[0]:<20} | {v[1]:<15} | ${float(v[2]):<7.2f} | {v[3]:<5} | {v[4]}")

def search_book(data):
    term = input("Search (ID/Name): ").lower()
    res = {k: v for k, v in data.items() if term in k.lower() or term in v[0].lower()}
    view_books(res)

def update_book(data):
    bid = input("Enter Book ID to update: ")
    if bid not in data: return print(" ID nahi mili.")
    print("Khaali (Enter) agar change nahi karna.")
    name = input(f"New Name [{data[bid][0]}]: ") or data[bid][0]
    auth = input(f"New Author [{data[bid][1]}]: ") or data[bid][1]
    qty_in = input(f"New Qty [{data[bid][3]}]: ")
    qty = int(qty_in) if (qty_in.isdigit() and int(qty_in) >= 0) else int(data[bid][3])
    price_in = input(f"New Price [{data[bid][2]}]: ")
    price = float(price_in) if (price_in and float(price_in) >= 0) else float(data[bid][2])
    
    data[bid] = [name, auth, price, qty, "Available" if qty > 0 else "Out of Stock"]
    save(data); print(" Updated!")

def delete_book(data):
    bid = input("Enter Book ID to delete: ")
    if data.pop(bid, None): save(data); print("🗑️ Deleted!")
    else: print("❌ ID nahi mili.")

def analyze_data(data):
    if not data: return print("📭 No data.")
    prices = [float(v[2]) for v in data.values()]
    qtys = [int(v[3]) for v in data.values()]
    print(f" Total Books: {len(data)}")
    print(f" Avg Price: ${sum(prices)/len(data):.2f}")
    print(f" Max Price: ${max(prices)}")
    print(f" Min Price: ${min(prices)}")
    print(f"Available: {sum(1 for q in qtys if q > 0)} |  Out of Stock: {sum(1 for q in qtys if q == 0)}")

# --- MAIN ---
def main():
    if input("Username: ") != "admin" or input("Password: ") != "1234": return print("🔒 Access Denied!")
    
    menu = {"1": add_book, "2": view_books, "3": search_book, "4": update_book, "5": delete_book, "6": analyze_data}
    while True:
        data = load()
        print("\n1.Add | 2.View | 3.Search | 4.Update | 5.Delete | 6.Analyze | 7.Exit")
        choice = input("Option: ").strip()
        if choice == "7": break
        if choice in menu: menu[choice](data)
        else: print("⚠️ Invalid Option")

if __name__ == "__main__": main()