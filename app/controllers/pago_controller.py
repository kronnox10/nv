import mysql.connector
from fastapi import HTTPException
from config.db_config import get_db_connection
from models.pago_model import Pago
from fastapi.encoders import jsonable_encoder

class payController:
        
    def create_pay(self, pago: Pago):   
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO pago (id_usuario,monto,fecha_pago,estado) VALUES (%s,%s,%s,%s)", (pago.id_usuario, pago.monto, pago.fecha_pago,pago.estado,))
            conn.commit()
            conn.close()
            return {"resultado": "Pago añadido correctamente"}
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
        

    def get_pay(self, pago_id: int):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pago WHERE id = %s", (pago_id,))
            result = cursor.fetchone()
            payload = []
            content = {} 
            
            content={
                    'id':int(result[0]),
                    'id_usuario':int(result[1]),
                    'monto':float(result[2]),
                    'fecha_pago':str(result[3]),
                    'estado':bool(result[4]),
                  
            }
            payload.append(content)
            
            json_data = jsonable_encoder(content)            
            if result:
               return  json_data
            else:
                raise HTTPException(status_code=404, detail="Pago not find")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
       
    def get_pays(self):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM pago")
            result = cursor.fetchall()
            payload = []
            content = {} 
            for data in result:
                content={
                    'id':data[0],
                    'id_usuario':data[1],
                    'monto':data[2],
                    'fecha_pago':data[3],
                    'estado':data[4],
                }
                payload.append(content)
                content = {}
            json_data = jsonable_encoder(payload)        
            if result:
               return {"resultado": json_data}
            else:
                raise HTTPException(status_code=404, detail="Pagos not found")  
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()


    def update_pay(self, pago_id: int, pago: Pago):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE pago
            SET id_usuario = %s,
            monto = %s,
            fecha_pago = %s,
            estado = %s 
            WHERE id = %s
            """,(pago.id_usuario, pago.monto, pago.fecha_pago, pago.estado,pago_id,))
            conn.commit()
           
            return {"resultado": "Pago actualizado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()   
       
    def delete_pay(self, pago_id: int):
        try: 
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('DELETE FROM pago WHERE id = %s',(pago_id,))
            conn.commit()           
            return {"resultado": "pago eliminado correctamente"} 
                
        except mysql.connector.Error as err:
            conn.rollback()
        finally:
            conn.close()
    