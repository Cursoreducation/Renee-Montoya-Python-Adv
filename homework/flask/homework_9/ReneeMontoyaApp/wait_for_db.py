import time


def connect_to_db(db):
    tries = 5

    while tries > 0:
        try:
            db.create_all()
            tries = 0
        except:
            tries += -1
            print('Failed to connect to database. Waiting and then trying again (try countdown: %s)' % tries)
            time.sleep(10)  # Wait a bit until database is loaded

    print("Database available!")
