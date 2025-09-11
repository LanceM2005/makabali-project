# from bson import ObjectId
import pymongo
from pydantic import BaseModel

class DBManager:

    def __init__(self, conn_str:str, db, col):
        '''connect to db server and set self.col'''
        
        myclient = pymongo.MongoClient(conn_str)
        mydb = myclient[db]
        self.col = mydb[col]

    def create(self, d: dict):
        '''create user
        
        args:
            d (dict): data to insert into db
        
        returns:
            id (str): object_id as a str
        '''

    def read_by_id(self, obj_id:str):
        '''read user by id 
                
        args:
            obj_id (str): 

        returns:
            data (dict): data retrieved, or None
        '''
        
    def read(self,query:dict):
        '''read many by query
        
        args:
            query (dict)

        returns:
            data (list): convert Cursor to list for return
        '''
    
    def read_all(self):
        '''read all
        
        returns:
            data (list)
        '''

    def update(self,obj_id,updates:dict):
        ''' update by id 
        
        args:
            obj_id (str)
            updates (dict)
        
        returns:
            modified_count (int)
        '''

    def delete_by_id(self,obj_id):
        ''' delete by id
        
        args:
            obj_id (str)

        returns:
            deleted_count (int)
        '''
    
    def delete(self,query:dict):
        ''' delete many by query 
        
        args:
            query (dict)

        returns:
            deleted_count (int)
        '''
    
    def delete_all(self):
        ''' delete all

        returns:
            deleted_count (int)
        '''


        result = self.col.delete_many({})
        return result.deleted_count              