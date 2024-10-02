import mysql.connector
from fastapi import HTTPException, UploadFile
import pandas as pd
from app.config.db_config import get_db_connection
from app.models.atributo_model import Atributo
from fastapi.encoders import jsonable_encoder


class AtributoController:
        
    def create_atributo(self, atributo: Atributo):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO atributo (nombre,descripcion,estado) VALUES (%s,%s,%s)", (atributo.nombre, atributo.descripcion,atributo.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "Atributo creado"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()

    def create_atributo_masivo(file: UploadFile):
        try:
            # Leer el archivo Excel
            contents = file.file.read()
            df = pd.read_excel(contents, engine='openpyxl')
               # Conectar a la base de datos
            conn = get_db_connection()
            cursor = conn.cursor()

            for index, row in df.iterrows():
                cursor.execute(
                    "INSERT INTO atributo (nombre, descripcion, estado) VALUES (%s, %s, %s)",
                    (row['nombre'], row['descripcion'], row['estado'])
                )
                conn.commit()
            return {"resultado": "Atributos creados exitosamente"}
        except mysql.connector.Error as err:
            conn.rollback()
            return {"error": str(err)}
        finally:
            conn.close()
       

    def get_atributo(self, atributo_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo WHERE id = %s", (atributo_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'nombre':result[1],
                    'descripcion':result[2],
                    'estado':bool(result[3]),
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Atributo not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_atributos(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM atributo")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'nombre':data[1],
                    'atributo':data[2],
                    'estado':data[3],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="not atributes founds")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    

    def update_atributo(self, atributo_id: int, atributo: Atributo):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE atributo
            SET nombre = %s,
            descripcion = %s,
            estado = %s
            WHERE id = %s
            """,(atributo.nombre, atributo.descripcion,atributo.estado,atributo_id,))
            conn.commit()
           
            return {"resultado": "Atributo actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()    


    def delete_atributo(self, atributo_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM atributo WHERE id = %s',(atributo_id,))
            conn.commit()           
            return {"resultado": "Atributo eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    
       

##atribute_controller = AtributoController()