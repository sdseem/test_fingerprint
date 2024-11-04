import psycopg2

class FingerprintDBConnection:
    def get_connection(self):
        try:
            conn = psycopg2.connect(dbname='postgres', user='user', password='password',
                                    host='host.docker.internal', port='5432')
            conn.autocommit = True
            return conn.cursor()
        except Exception as e:
            print('Can`t establish connection to database')


    def save_raw(self, fingerprint):
        connection = self.get_connection()
        insert_query = """
        INSERT INTO RAW_FINGERPRINTS(RAW_FINGERPRINT)
        VALUES (%s);
        """
        print(insert_query)
        data = (str(fingerprint),)
        connection.execute(insert_query, data)
        connection.close()