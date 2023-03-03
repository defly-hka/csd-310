import mysql.connector

cneckshn = mysql.connector.connect(
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
)
cursor = cneckshn.cursor()

#Browse books option
def bookshelf(_cursor):
    librarian = "SELECT book_name, Details, Author FROM book"
    cursor.execute(librarian)
    #executing the librarian is a good thing here (please don't harm local librarians)
    #pulls book data (not including book_id) and displays it line by line with descriptions included
    books = cursor.fetchone()
    while books is not None:
        print(books[0], books [1])
        books = cursor.fetchone()

    
#FindAStore, much like our last one except for stores
def im_the_map(_cursor):
    WheresWhatabook = "SELECT Locale FROM store"
    cursor.execute(WheresWhatabook)
    stores = cursor.fetchall()
    print (stores)

#validate user by checking if the number entered exists in the the "user" table by searching through the user_id column, if there is 1 result the user is validated
def DoIKnowYou(whoAREyou):
    query = "SELECT COUNT(*) FROM user WHERE user_id = %s"
    cursor.execute(query, (whoAREyou,))
    result = cursor.fetchone()[0]
    return result == 1
whoAREyou = int(input("Please enter your User ID: "))
if DoIKnowYou(whoAREyou):
    print("Welcome Back!")
else:
    print("Invalid user ID")

#Option to view their own wishlist as it is currently
##I was COMPLETELY lost on the joins for the wishlist so I did consult the context from the class github for that part. Books to add and add to wishlist are the only things I have left after this
def MyWishes(_cursor, _user_id):
    WishUpon = ("SELECT user.user_id, book.book_id, book.book_name, book.author " 
                + "FROM wishlist " 
                + "INNER JOIN user ON wishlist.user_id = user.user_id "
                + "INNER JOIN book ON wishlist.book_id = book.book_id "
                + "WHERE user.user_id ={}".format(_user_id)
                )
    cursor.execute(WishUpon)
    wishlist = cursor.fetchall()
    print (wishlist)

#it helped figure out how to show the other books
def NewBooks(_cursor, _user_id):
    WhatElseYaGot = ("Select book_id, book_name, author "
                     + "FROM book "
                     + "WHERE book_id NOT IN"
                     +"SELECT book_id FROM wishlist WHERE user_id = {})".format(_user_id)
                    )
    cursor.execute(WhatElseYaGot)
    TheRestoftheBooks = cursor.fetchall()
    print(TheRestoftheBooks)

def MakeAWish (_cursor, _user_id):
    #display new books
    print("Take a look at the rest of our selection: ")
    NewBooks(_cursor, _user_id)
    
    #The make a wish part
    book_id = input("Please enter the ID of the book to add it to your wishlist: ")
    
    #insert the book into the table
    cursor.execute("INSERT INTO wishlist (user_id, book_id) VALUES (%s, %s)", _user_id, book_id)
    db.commit
    print("book added to your wishlist!")

#Account options loops them through the accountOptions until a valid input is selected
def accountOptions():
     print("1. My Wishlist\n 2. Add Book\n 3. Main Menu")
     user_nav = int(input("\n Welcome back! How can we help today? Please choose 1-3: "))
     if user_nav == 1:
         MyWishes(cursor, user_id)
    elif user_nav == 2:
        MakeAWish(cursor, user_id)
    elif user_nav == 3:
        show_menu()
    else:
        print("Sorry, that's not a valid option, please try again.")

#Defining the variable they'll use to choose from the main display menu
choice = int(input("Please enter your choice: "))

if choice == 1:
    bookshelf(cursor)
elif choice == 2:
    im_the_map(cursor)
elif choice == 3:
    DoIKnowYou()
    accountOptions()
elif choice == 4:
    cursor.close()
    cneckshn.close()

if choice <1 or choice >4:
    print("Sorry! Please choose an option from the menu (1-4): ")
    choice = show_menu()
    
#Defining our intro menu and showing it to the user with a welcome message
def show_menu():
    print("1. Browse Books")
    print("2. Find a Store")
    print("3. User Check-in")
    print("4. Exit")
    print(choice)

print("Welcome to WhataBook!")
show_menu()

