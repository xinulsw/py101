-- todo/todo.sql

-- tabela z zadaniami
DROP TABLE IF EXISTS zadania;
CREATE TABLE zadania (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- unikalny identyfikator
    zadanie TEXT NOT NULL, -- opis zadania do wykonania
    zrobione BOOLEAN NOT NULL, -- informacja czy zadania zostało juz wykonane
    data_pub DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP -- data dodania zadania
);

-- pierwsze dane
INSERT INTO zadania (id, zadanie, zrobione)
VALUES (null, 'Wyrzucić śmieci', 0);
INSERT into zadania (id, zadanie, zrobione)
VALUES (null, 'Nakarmić psa', 0);
