from multiprocessing import Process
import psycopg2
from decouple import config


class TestOops:

    def __init__(self, var, start, end):
        self.start = start
        self.var = var
        self.end = end


class InheritedTest(TestOops):

    def __init__(self, var, start, end):
        TestOops.__init__(self, var, start, end)

    def table(self, i):
        print(self.var*i)


if __name__ == "__main__":
    try:
        connection = psycopg2.connect(user=config("USER"),
                                      password=config('PASSWORD'),
                                      host=config('HOST'),
                                      port="5432",
                                      name=config('NAME'))
        cursor = connection.cursor()
        sql = '''CREATE TABLE DATA(
           D1 INT,
        )'''
        cursor.execute(sql)
        postgres_insert_query = """ INSERT INTO DATA (D1) VALUES (%s)"""
        record_to_insert = (5)
        cursor.execute(postgres_insert_query, record_to_insert)

        connection.commit()
        count = cursor.rowcount
        print(count, "Record inserted successfully into mobile table")

    except (Exception, psycopg2.Error) as error:
        if (connection):
            print("Failed to insert record into mobile table", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")

    ins = InheritedTest(2, 3, 10)
    procs = []
    # instantiating process with arguments
    for i in range(ins.start, ins.end+1):
        proc = Process(target=ins.table, args=(i,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()
