CREATE user 'whatabook_user'@'localhost' IDENTIFIED WITH my_sql_native_password BY 'MySQL8IsGreat!';
GRANT ALL PRIVILEGES ON whatabook.* TO 'whatabook_user'@'localhost';

#Creating Store
CREATE TABLE Store(
	store_id INT NOT NULL PRIMARY KEY,
    locale VARCHAR(500) NOT NULL
    );
INSERT INTO whatabook.store (store_id, locale)
    Values (1, 'Alexandria');
    
#ADDING USERs
CREATE table user (
	user_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(75) NOT NULL, 
	last_name VARCHAR(75) NOT NULL
	);
INSERT INTO whatabook.user (user_id, first_name, last_name)
	Values (1, 'Roland', 'Deschain'),
    (2, 'Mark', 'Watney'),
    (3, 'Paul', 'Atreides');
#Creating Books
CREATE TABLE book(
	book_id INT NOT NULL AUTO_INCREMENT, 
    book_name VARCHAR(200) NOT NULL,
    details VARCHAR(500),
    author VARCHAR(200) NOT NULL,
    PRIMARY KEY (book_id)
	);
INSERT INTO whatabook.book (book_id, book_name, details, author)
	Values (1, 'The Dark Tower', 'The man in black fled across the desert, and the gunslinger followed', 'Stephen King'),
    (2, 'The Martian', 'The greatest botanist on the planet, and also technically a space pirate', 'Andy Wier'),
    (3, 'Dune', 'The spice must flow, praise the great Shai Hulud', 'Frank Herbert'),
    (4, "The Hitchhiker's Guide to the Galaxy", "Don't forget your towel", 'Douglas Adams'),
    (5, 'Good Omens', "It's Ineffable", "Terry Pratchett & Neil Gaiman"),
    (6, 'The Screwtape Letters', 'My dearest Wormwood, friendliest advice from an affectionate demon', "C.S. Lewis"),
    (7, "Old Man's War", 'Fighting an enemy among the stars who has a million ways to make your green skin shiver', 'John Scalzi'),
    (8, 'The Alchemist', "No heart has ever suffered when it goes in search of its dreams", 'Paulo Coelho'),
    (9, 'Big Fish', "There's a lot more truth to even the most fantastical of stories", 'Daniel Wallace');
#Creating Wishlist
CREATE TABLE Wishlist(
	wishlist_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL AUTO_INCREMENT,
    book_id INT NOT NULL AUTO_INCREMENT,
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (book_id) REFERENCES Books(id)
	);
INSERT INTO whatabook.wishlist (user_id, book_id)
	Values (1, 7),
    (2, 4),
    (3, 1);

SELECT *
FROM Wishlist
JOIN Users ON Wishlist.user_id = Users.user_id
JOIN Books ON Wishlist.book_id = Books.book_id;