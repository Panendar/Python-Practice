import datetime

quit = True

# file = open("code.code", "r")
# # Read the file line by line
# lines = file.readlines() 

# print( [ line for line in lines if line.strip() == ''])

# file.close()

def write_journal():
    written_text = input("Enter your journal entry: ")
    with open("journal.txt", "w") as f:
        f.write(f"{written_text}""\t\t====>" +str(datetime.datetime.now()) + "\n")
        return written_text

def read_journal():
    with open("journal.txt", "r") as f:
        content = f.readlines()
        if content == []:
            print("No journal entries found.  \n Please write your journal first____.")
        else:
            print("\n=== Journal Entries ===")
            for entry in content:
                # Split the entry into text and timestamp
                parts = entry.strip().split("\t\t====>")
                text = parts[0]
                timestamp = parts[1]
                print(f"Entry: {text}")
                print(f"Date: {timestamp}")
                print("-" * 30)
            return content

def search_journal():
    year = int(input("Enter the year of the search journal entry (YYYY): "))
    month = int(input("Enter the month of the journal entry you want to search (MM): "))
    day = int(input("Enter the day of the journal entry you want to search (DD): "))
    # Format the date with zero-padding for single digit months and days
    search_date = f"{year}-{month:02d}-{day:02d}"
    with open("journal.txt", "r") as f:
        content = f.readlines()
        found = False
        for line in content:
            if search_date in line:
                # Split the entry into text and timestamp for better display
                parts = line.strip().split("\t\t====>")
                text = parts[0]
                timestamp = parts[1]
                print("\n=== Found Journal Entry ===")
                print(f"Entry: {text}")
                print(f"Date: {timestamp}")
                print("-" * 30)
                found = True
        if not found:
            print(f"No journal entry found for {search_date}.")
            return None
            
def exit():
    global quit
    print("Exiting the program. Goodbye!")
    quit = False
    

while quit:
    print("===========MENU==========")
    menu = int(input("1. WRITE JOURNAL\n2. READ JOURNAL\n3. SEARCH\n4. EXIT\n      =>Enter your choice: "))

    if menu == 1:
        write_journal()
    elif menu == 2:
        read_journal()
    elif menu == 3:
        search_journal()
    elif menu == 4:
        exit()
    else:
        print("ENTER THE VALID OPTION FROM THE MENU")
