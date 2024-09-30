import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.transacciones_model import Transacciones
from fastapi.encoders import jsonable_encoder

class TravesanoController:
        
    def create_transaccion(self, transacciones: Transacciones):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO transacciones (id_pago,tipo_pago,fecha_pago,estado) VALUES (%s,%s,%s,%s)", (transacciones.id_pago, transacciones.tipo_pago, transacciones.fecha_pago,transacciones.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "Transaccion añadida correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_transaccion(self, transaccion_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM transacciones WHERE id = %s", (transaccion_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_pago':int(result[1]),
                    'tipo_pago':result[2],
                    'fecha_pago':str(result[3]),
                    'estado':bool(result[4]),
                  
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Transaccion not find")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_transacciones(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM transacciones")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_pago':data[1],
                    'tipo_pago':data[2],
                    'fecha_pago':data[3],
                    'estado':data[4],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Transaccion not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_transacciones(self, transacciones_id: int, transacciones: Transacciones):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE transacciones
            SET id_pago = %s,
            tipo_pago = %s,
            fecha_pago = %s,
            estado = %s 
            WHERE id = %s
            """,(transacciones.id_pago, transacciones.tipo_pago, transacciones.fecha_pago,transacciones.estado,transacciones_id,))
            conn.commit()
           
            return {"resultado": "Transaccion actualizada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_transacciones(self, transacciones_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM transacciones WHERE id = %s',(transacciones_id,))
            conn.commit()           
            return {"resultado": "Transaccion eliminada correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    