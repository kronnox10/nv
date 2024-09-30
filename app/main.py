from fastapi import FastAPI
from routes.user_routes import router as user_router
from routes.rol_routes import router as Rol_router
from routes.atributo_routes import router as atributo_router
from routes.atributoxusuario_routes import router as atrixuser_router
from routes.pago_routes import router as Pago_router
from routes.Transacciones_routes import router as Transaccion_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    #"http://localhost.tiangolo.com",
    #"https://localhost.tiangolo.com",
    "http://localhost"
    #"http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(user_router) 
app.include_router(Rol_router)
app.include_router(atributo_router)  
app.include_router(atrixuser_router)  
app.include_router(Pago_router)  
app.include_router(Transaccion_router) 



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) ##manin cuando termines las bases de datos me avisas para construir el modelo y empezar a hacer las rutas etc....