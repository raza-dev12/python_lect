# # file path
# file_path = "data/books.txt"
# isLoggedIn = False
# username = "admin"
# password = "123"
# *** Helper Methods ***
# ** 1. Validators
def valid_book_name(prompt="Enter book name: "):
    while True:
        name = input(prompt).strip()
        if not name:
            print("❌ Name cannot be empty!")
            continue
        return name  
def valid_author_name(prompt="Enter author name: "):
    while True:
        name = input(prompt).strip()
        if not name:
            print("❌ Name cannot be empty!")
            continue
        if name.isdigit():
            print("❌ Name cannot be numeric only!")
            continue
        if not name.replace(" ", "").isalpha():
            print("❌ Invalid name! Only alphabets and spaces allowed.")
            continue
        return name
def valid_price(prompt="Enter book price: "):
    while True:
        price = input(prompt).strip()
        if not price:
            print("❌ Price cannot be empty!")
            continue
        try:
            price = float(price)
            if price <= 0:
                print("❌ Price must be greater than 0!")
                continue
            return price
        except ValueError:
            print("❌ Price must be a valid number!")
def valid_quantity(prompt="Enter book quantity: "):
    while True:
        quantity = input(prompt).strip()
        if not quantity:
            print("❌ Quantity cannot be empty!")
            continue
        try:
            quantity = int(quantity)
            if quantity < 0:
                print("❌ Quantity cannot be in negative!")
                continue
            return quantity
        except ValueError:
            print("❌ Quantity must be a valid number without decimals!")
def valid_book_id(prompt="Enter book id: "):
    while True:
        _id = input(prompt).strip()
        if not _id:
            print("❌ ID cannot be empty!")
            continue
        try:
            _id = int(_id)
            if _id <= 0:
                print("❌ ID must be greater than 0!")
                continue
            if str(_id) not in book_ids():
                print("❌ ID not found!")
                continue
            return _id
        except ValueError:
            print("❌ ID must be a valid number without decimals!")
def valid_choice(options, prompt="Enter choice: "):
    while True:
        choice = input(prompt).strip()
        if not choice:
            print("❌ Choice cannot be empty!")
            continue
        if choice not in options:
            print(f"❌ Invalid choice! Choose from {', '.join(options)}")
            continue
        return choice

# ** 2. File Methods
# read books
def read_books():
    try:
        with open(file_path,"r") as file:
            return file.readlines()
    except:
        return []
# write books
def write_books(lines):
    with open(file_path,"w") as file:
        return file.writelines(lines)
# append line
def append_line(line):
    with open(file_path,"a") as file:
        return file.write(f"{line}\n")

# ** 3. Other useful methods
# get next book id
def next_book_id():
    lines = read_books()
    if lines == []:
        return 10001
    else:
        return int(lines[-1].split(",")[0]) + 1
# get stock status
def stock_status(qty, treshold=0):
    if qty > treshold:
        return "In-Stock"
    else:
        return "Out-Of-Stock"
# get all book ids
def book_ids():
    lines = read_books()
    _idList = []
    if lines:
        for line in lines:
            _idList.append(line.split(",")[0])
    return _idList
# get books data in dictionary format
def get_books_data():
    lines = read_books()
    books = []
    for line in lines:
        data = line.strip().split(",")
        books.append({
            "id": int(data[0]),
            "name": data[1],
            "author": data[2],
            "price": float(data[3]),
            "qty": int(data[4]),
            "status": data[5]
        })
    return books
# ** 4. Formatters
# format price to $$
def format_price(price=1):
    return str(price)+"$"
def format_table_data(data):
    print("="*95)
    print(f"|{'ID'.center(8):<8}|{'Name'.center(30):<30}|{'Author'.center(20):<20}|{'Price'.center(8):<8}|{'Qty'.center(8):<8}|{'Status'.center(14):<14}|")
    print("-"*95)
    for line in data:
        _id, name, author, price, qty, status = line.strip().split(",")
        print(f"|{_id.center(8):<8}|{name.title().center(30):<30}|{author.title().center(20):<20}|{format_price(price).center(8):<8}|{qty.center(8):<8}|{status.center(14):<14}|")
        print("-"*95)
    print("="*95)

# *** Core Features Methods ***
# 1 Add Book
def add_book():
    book_id = next_book_id()
    book_name = valid_book_name()
    author_name = valid_author_name()
    book_price = valid_price()
    book_quantity = valid_quantity()
    stock_status = "In-Stock"
    try:
        append_line(f"{book_id},{book_name},{author_name},{book_price},{book_quantity},{stock_status}")
        print("✅ Book added successfully!")
    except:
        print("❌ Something went wrong!")
# 2 Update Book
def update_book():
    book_id = str(valid_book_id())
    lines = read_books()
    updated = False

    for i, line in enumerate(lines):
        data = line.strip().split(",")
        if data[0] == book_id:
            print("\nWhat do you want to update?")
            print("1. Book Name")
            print("2. Author Name")
            print("3. Book Price")
            print("4. Book Quantity")
            print("5. Update All")
            choice = valid_choice(["1", "2", "3", "4", "5"])
            if choice == "1":
                data[1] = valid_book_name()
            elif choice == "2":
                data[2] = valid_author_name()
            elif choice == "3":
                data[3] = str(valid_price())
            elif choice == "4":
                qty = valid_quantity()
                data[4] = str(qty)
                data[5] = stock_status(qty)
            elif choice == "5":
                data[1] = valid_book_name()
                data[2] = valid_author_name()
                data[3] = str(valid_price())
                qty = valid_quantity()
                data[4] = str(qty)
                data[5] = stock_status(qty)
            else:
                print("❌ Invalid choice!")
                return            
            data[5] = stock_status(int(data[4]))
            lines[i] = ",".join(data) + "\n"
            updated = True
            break
    if updated:
        write_books(lines)
        print("✅ Book updated successfully!")
    else:
        print("❌ Book not found!")
# 3 Read Book in table format
def display_books():
    format_table_data(read_books())
# 4 Delete Book
def delete_book():
    book_id = str(valid_book_id())
    lines = read_books()
    found = False

    for i, line in enumerate(lines):
        data = line.strip().split(",")
        if data[0] == book_id:
            found = True
            print("\n=== Book Details ===")
            print(f"ID     : {data[0]}")
            print(f"Name   : {data[1].title()}")
            print(f"Author : {data[2].title()}")
            print(f"Price  : {format_price(data[3])}")
            print(f"Qty    : {data[4]}")
            print(f"Status : {data[5]}")
            confirm = valid_choice(["y", "n"],"\nAre you sure you want to delete this book? (y/n): ").lower()
            if confirm == "y":
                lines.pop(i)
                write_books(lines)
                print("✅ Book deleted successfully!")
            else:
                print("❌ Delete cancelled!")
            break
    if not found:
        print("❌ Book not found!")
# 5 Stats
def show_stats():
    books = get_books_data()
    if not books:
        print("❌ No books available!")
        return
    
    total_books = len(books)
    total_price = sum(book["price"] for book in books)
    avg_price = total_price / total_books
    most_expensive = max(books, key=lambda x: x["price"])
    cheapest = min(books, key=lambda x: x["price"])
    available_books = sum(1 for book in books if book["status"] == "In-Stock")
    out_of_stock = total_books - available_books

    print("\n📊 Library Statistics")
    print("=" * 40)
    print(f"Total Books        : {total_books}")
    print(f"Average Price      : {avg_price:.2f}$")
    print(f"Most Expensive     : {most_expensive['name']} ({most_expensive['price']}$)")
    print(f"Cheapest Book      : {cheapest['name']} ({cheapest['price']}$)")
    print(f"Available Books    : {available_books}")
    print(f"Out of Stock       : {out_of_stock}")
    print("=" * 40)
# 6 Admin Login
def login():
    print("🔑 Login to the system.")
    _username = input("Enter username: ") 
    _password = input("Enter password: ")
    global isLoggedIn 
    if (_username == username and _password == password):
        isLoggedIn = True
        print("✅ Logged In!")
    else:
        isLoggedIn = False
        print("❌ Invalid username or password!")

# *** Main Method ***
def main():
    print("Welcome to Library Management System 📚")
    while True:
        if not isLoggedIn:
            login()
            continue
        print("\nWhat do you want to do?")
        print("1. See All Books")
        print("2. Add New Book")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. View Statistics")
        print("6. Exit")
        choice = valid_choice(["1", "2", "3", "4","5","6"])
        if choice == "1":
            display_books()
        elif choice == "2":
            add_book()
        elif choice == "3":
            update_book()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            show_stats()
        else:
            break

# *** Entry Point ***
main()