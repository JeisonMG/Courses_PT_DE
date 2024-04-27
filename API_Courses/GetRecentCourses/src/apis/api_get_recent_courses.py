import pyodbc
import os
import json

class database_execute:

    def __init__(self, view_name):

        # get connection values
        self.server     = os.environ.get("DB_SERVER")
        self.database   = os.environ.get("DB_DATABASE")
        self.username   = os.environ.get("DB_USERNAME")
        self.password   = os.environ.get("DB_PASSWORD")
        self.driver     = '{ODBC Driver 17 for SQL Server}'
        self.view_name  = view_name

    def get_data_from_azure_sql(self):
        """
            function that queries a parameterized view in Azure SQL
            params:
                view_name = string (name of view)
        """
        
        # initialize response
        json_data = []
        
        try:

            # Establish the connection with azure SQL
            with pyodbc.connect(f'SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password};'
                                f'DRIVER={self.driver}') as conn:
                
                with conn.cursor() as cursor:

                    # Run SQL query with parameterized view
                    cursor.execute(f'SELECT * FROM {self.view_name}')

                    # Recover the results
                    rows = cursor.fetchall()

                    # Convert the results to a list of dictionaries
                    data = [dict(zip([column[0] for column in cursor.description], row)) for row in rows]

                    # validate that the data was obtained
                    if data:

                        # Convert the result to JSON format
                        json_data = json.dumps(
                            {
                                "message": "successful",
                                "status_code": 200,
                                "data": data
                            }
                        )

                    else:
                        json_data = json.dumps(
                            {
                                "message": "No results found",
                                "status_code": 404,
                                "data": data
                            }
                        )

        finally:

            # close connection
            conn.close()
 
        return json_data