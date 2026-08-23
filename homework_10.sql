CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    publication_year INTEGER,
    price REAL
);

INSERT INTO books (title, author, publication_year, price)
VALUES
    ('Кобзар', 'Тарас Шевченко', 1840, 320.00),
    ('Тигролови', 'Іван Багряний', 1944, 210.00);


UPDATE books
SET price = 300.00
WHERE id = 2;

DELETE FROM books
WHERE id = 4;