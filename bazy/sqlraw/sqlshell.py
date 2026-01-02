import sqlite3

con = sqlite3.connect(":memory:")
con.isolation_level = None
cur = con.cursor()

bufor = ""

print("Podaj polecenie SQL do wykonania w sqlite3.")
print("Naciśnij Enter, aby wyjść.")

while True:
    line = input()
    if line == "":
        break
    bufor += line
    if sqlite3.complete_statement(bufor):
        try:
            bufor = bufor.strip()
            cur.execute(bufor)

            if bufor.lstrip().upper().startswith("SELECT"):
                print(cur.fetchall())
        except sqlite3.Error as e:
            print("Wystąpił błąd:", e.args[0])
        bufor = ""

con.close()
