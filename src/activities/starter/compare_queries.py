import sqlite3
import time
from importlib import resources

from activities import data


def execute_and_time_query(db_path, query, label):
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    start_time = time.time()
    cur.execute(query)
    results = cur.fetchall()
    end_time = time.time()
    duration = end_time - start_time
    print(f"Query on {label} database executed in {duration:.6f} seconds")
    print("Query results:")
    for result in results:
        print(result)
    con.close()


def compare_paralympics_queries(db_un, db_n):
    query_un = "SELECT * FROM Games WHERE type = 'summer' AND year = 2012;"
    query_n = '''SELECT g.type,
                        g.year,
                        c.country,
                        h.place_name AS host,
                        g.start,
                        g.end,
                        GROUP_CONCAT(d.description, ', ') AS disabilities_included,
                        g.countries,
                        g.events,
                        g.sports,
                        g.participants_m,
                        g.participants_f,
                        g.participants,
                        g.highlights,
                        g.URL
                 FROM Games g
                          JOIN GamesHost gh ON g.id = gh.games_id
                          JOIN Host h ON gh.host_id = h.id
                          JOIN Country c ON h.country_id = c.id
                          LEFT JOIN GamesDisability gd ON g.id = gd.games_id
                          LEFT JOIN Disability d ON gd.disability_id = d.id
                 WHERE h.place_name = 'London'
                   AND g.year = 2012
                 GROUP BY g.id, c.country, h.place_name
    ;'''
    execute_and_time_query(db_un, query_un, "un-normalised")
    execute_and_time_query(db_n, query_n, "normalised")


def main():
    db_path_pu = resources.files(data).joinpath("para-not-normalised.sqlite")
    db_para_u = resources.files(data).joinpath("para-normalised.db")
    compare_paralympics_queries(db_path_pu, db_para_u)


if __name__ == "__main__":
    main()
