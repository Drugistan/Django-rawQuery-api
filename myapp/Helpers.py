import csv
import tempfile
from django.db import connection


class OptimizedExport:

    def make_query(self):
        # you can write your own query
        raw_query = """
            SELECT * FROM myapp_orders
        """

        try:
            with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='') as temp_file:
                columns_name = [
                    "id", "order_id", "email", "orderCreatedAt", "orderUpdatedAt", "created_at", "updated_at",
                    "customers_id"
                ]
                csv_writer = csv.DictWriter(temp_file, fieldnames=columns_name)
                csv_writer.writeheader()

                data = self.execute_query(raw_query)
                while True:
                    try:
                        chunk = next(data)
                        csv_writer.writerows(chunk)
                    except StopIteration:
                        break

        finally:
            temp_file.close()
        return True, temp_file.name

    def execute_query(self, raw_query):
        with connection.cursor() as cursor:
            cursor.execute(raw_query)
            orders = self.fetch_data(cursor)
            yield orders

    def fetch_data(self, cursor):
        columns = [col[0] for col in cursor.description]
        while True:
            rows = cursor.fetchmany(1000)  # Fetch in batches
            if not rows:
                break
            return [dict(zip(columns, row)) for row in rows]
