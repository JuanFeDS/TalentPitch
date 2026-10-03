'''Routes for user-related API endpoints'''
import os
import json

from typing import List
from datetime import datetime
from pydantic import BaseModel

from fastapi import APIRouter, HTTPException
# from google.cloud import bigquery
# from google.oauth2 import service_account

# Initialize APIRouter for user routes
router = APIRouter()

# BigQuery connection setup using a service account
# SERVICE_ACCOUNT_INFO = os.getenv('GCP_KEY')
# service_account_info = json.loads(SERVICE_ACCOUNT_INFO)
# Usamos from_service_account_info para cargar las credenciales desde el diccionario
# credentials = service_account.Credentials.from_service_account_info(service_account_info)

# Inicializamos el cliente de BigQuery con las credenciales
# client = bigquery.Client(credentials=credentials, project=credentials.project_id)

class User(BaseModel):
    '''
    Pydantic BaseModel representing a user.
    
    Attributes:
        id (int): Unique identifier for the user.
        name (str): Full name of the user.
        identification_number (int): User's identification number.
        slug (str): Slugified version of the user's name for URL-friendly usage.
        video (str): URL to the user's video.
        email (str): User's email address.
        gender (str): User's gender (e.g., 'M' for male, 'F' for female).
        created_at (datetime): Date and time when the user was created.
        updated_at (datetime): Date and time when the user was last updated.
    '''
    id: int
    name: str
    identification_number: int
    slug: str
    video: str
    email: str
    gender: str
    created_at: datetime
    updated_at: datetime

@router.get('/users')
async def get_users():
    return {'message': 'Users!'}


# @router.get('/users')
# async def get_users():
#     '''
#     Fetch user details by user ID from BigQuery.
    
#     Returns:
#         list: A list of dictionaries containing all the users information, if found.
    
#     Raises:
#         HTTPException: If the user ID does not exist, a 404 error is returned.
#     '''

#     # SQL query to fetch the users data from BigQuery
#     query = '''
#     SELECT * 
#     FROM `rich-gift-437021-n6.Datos_TalentPitch.TBL_USERS` 
#     '''

#     # Execute the query
#     query_job = client.query(query)
#     df_user = query_job.to_dataframe()

#     # Raise exception if no users exist
#     if df_user.empty:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Convert the result to a dictionary and return as JSON response
#     result = df_user.to_dict(orient="records")

#     return result


# @router.get('/users/{user_id}', response_model=List[User])
# async def get_user_by_id(user_id):
#     '''
#     Fetch user details by user ID from BigQuery.
    
#     Args:
#         user_id (int): The unique identifier of the user.
        
#     Returns:
#         List[User]: A list containing the user information, if found.
    
#     Raises:
#         HTTPException: If the user ID does not exist, a 404 error is returned.
#     '''

#     # SQL query to fetch the user data by ID from BigQuery
#     query = f'''
#     SELECT * 
#     FROM `rich-gift-437021-n6.Datos_TalentPitch.TBL_USERS` 
#     WHERE ID = {user_id}
#     '''

#     # Execute the query
#     query_job = client.query(query)
#     df_user = query_job.to_dataframe()

#     # Raise exception if user not found
#     if df_user.empty:
#         raise HTTPException(status_code=404, detail="User not found")

#     # Convert the result to a dictionary and return as JSON response
#     result = df_user.to_dict(orient="records")

#     return result
