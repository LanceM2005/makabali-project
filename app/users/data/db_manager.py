from bson import ObjectId
import pymongo
from pydantic import BaseModel

class DBManager:

    def __init__(self, conn_str:str, db, col):
        '''connect to db server and set self.col'''
        
        myclient = pymongo.MongoClient(conn_str)
        mydb = myclient[db]
        self.col = mydb[col]

    def create(self, d: dict):
        result = self.col.insert_one(d)
        return str(result.inserted_id)

    def read_by_id(self, obj_id:str):
        '''read user by id 
                
        args:
            obj_id (str): 

        returns:
            data (dict): data retrieved, or None
        '''
        result = self.col.find_one({"_id": ObjectId(obj_id)})
        if result:
            result["_id"] = str(result["_id"])
        return result
        
    def read(self,query:dict):
        '''read many by query
        
        args:
            query (dict)

        returns:
            data (list): convert Cursor to list for return
        '''
        cursor = self.col.find(query)
        results = list(cursor)
        for r in results:
            r["_id"] = str(r["_id"])
        return results
    
    def read_all(self):
        '''read all
        
        returns:
            data (list)
        '''
        cursor = self.col.find({})
        results = list(cursor)
        for r in results:
            r["_id"] = str(r["_id"])
        return results

    def update(self,obj_id,updates:dict):
        ''' update by id 
        
        args:
            obj_id (str)
            updates (dict)
        
        returns:
            modified_count (int)
        '''
        result = self.col.update_one(
            {"_id": ObjectId(obj_id)},
            {"$set": updates}
        )
        return result.modified_count

    def delete_by_id(self,obj_id):
        ''' delete by id
        
        args:
            obj_id (str)

        returns:
            deleted_count (int)
        '''
        result = self.col.delete_one({"_id": ObjectId(obj_id)})
        return result.deleted_count
    
    def delete(self,query:dict):
        ''' delete many by query 
        
        args:
            query (dict)

        returns:
            deleted_count (int)
        '''
        result = self.col.delete_many(query)
        return result.deleted_count
    
    def delete_all(self):
        ''' delete all

        returns:
            deleted_count (int)
        '''


        result = self.col.delete_many({})
        return result.deleted_count              