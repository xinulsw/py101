-- projekty_flask/todo/modele.sql

-- tabela z użytkownikami
DROP TABLE IF EXISTS user;
CREATE TABLE user (
  id INTEGER PRIMARY KEY AUTOINCREMENT, -- unikalny identyfikator
  nazwa TEXT UNIQUE NOT NULL, -- nazwa użytkownika
  haslo TEXT NOT NULL -- hasło użytkownika
);
-- przykładowe dane
INSERT INTO user (id, nazwa, haslo)
VALUES (null, 'adam', 'zaq1@WSX');

-- tabela z zadaniami
DROP TABLE IF EXISTS zadanie;
CREATE TABLE zadanie (
    id INTEGER PRIMARY KEY AUTOINCREMENT, -- unikalny identyfikator zadania
    user_id INTEGER, -- identyfikator użytkownika
    zadanie TEXT NOT NULL, -- opis zadania do wykonania
    zrobione BOOLEAN NOT NULL, -- informacja czy zadania zostało juz wykonane
    data_pub DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP, -- data dodania zadania
    FOREIGN KEY (user_id) REFERENCES user(id) ON DELETE CASCADE -- wskazanie klucza obcego
);

-- przykładowe dane
INSERT INTO zadanie (id, user_id, zadanie, zrobione)
VALUES (null, 0, 'Wyrzucić śmieci', 0);
INSERT into zadanie (id, user_id, zadanie, zrobione)
VALUES (null, 0, 'Nakarmić psa', 0);
