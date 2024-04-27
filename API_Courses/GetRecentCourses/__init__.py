import logging
import json

import azure.functions as func
from .src.apis.api_get_recent_courses import database_execute


def main(req: func.HttpRequest) -> func.HttpResponse:

    if req.method != 'GET':
        return func.HttpResponse(
            "This API only accepts GET requests",
            status_code=400
        )
    
    # Set view name
    view_name = "dbo.vw_most_recent_courses"

    # Instantiate the get_view class
    db_connector = database_execute(view_name)

    # Gets the data from the view
    json_data = db_connector.get_data_from_azure_sql()

    # Returns the HTTP response with the data in JSON format
    return func.HttpResponse(
        json_data,
        mimetype="application/json",
        status_code=200
    )
    
