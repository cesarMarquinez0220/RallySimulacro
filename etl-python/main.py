from dotenv import load_dotenv
import os 
import csv
import mysql.connector
from pathlib import Path

load_dotenv()
#variables para conexion
host = os.getenv("DB_HOST")
username = os.getenv("DB_USERNAME")
pasword = os.getenv("DB_PASSWORD")
database = os.getenv("DB_DATABASE")

archivo = Path(__file__).parent.parent / "nomina_sucia.csv"

def limpiezaDatos(archivo):
    lista_limpia = []
    
    try:
        with archivo.open("r",encoding="utf-8-sig") as file:
            contenido = csv.DictReader(file)
        
            for fila in contenido:
                codigo = fila['codigo']
                nombres = fila['nombre'].title()
                departamentos = fila['departamento'].strip()
                salario_bruto = float(fila['salario_bruto'])
                
                
                if departamentos in("IT","Informática"):
                    departamentos = "Tecnología"
                    
                lista_limpia.append({
                    "codigo": codigo,
                    "nombres":nombres,
                    "departamento":departamentos,
                    "salario_bruto":salario_bruto
                })
        
        return lista_limpia   
            
            
    except Exception as Error:
        print("Algo ocurrio mal: ", Error)
        
        
resultado = limpiezaDatos(archivo)
#print("Esto es lo viejo", resultado)

def logicaNegocio(resultado):
    lista_correcion_salario = []
    
    for fila in resultado:
        codigo = fila['codigo']
        nombres = fila['nombres']
        departamentos = fila['departamento']
        salario_neto = fila['salario_bruto']
        
        calculo_salario_neto = salario_neto * (1-0.0975)
        
        lista_correcion_salario.append({
            "codigo": codigo,
            "nombres":nombres,
            "departamento":departamentos,
            "salario_neto":calculo_salario_neto
            
        })
    
    return lista_correcion_salario

negocio=logicaNegocio(resultado)
#print("Esto es lo nuevo que va",negocio)

def upsert(host,username,pasword,database,negocio):
    cnx = None    
    sentencia_select = "SELECT id FROM empleados WHERE codigo_empleado = %s"
    sentencia_insert = "INSERT INTO empleados (codigo_empleado,nombre_completo,departamwnto,salario_neto) VALUES (%s, %s, %s, %s)"
    sentencia_update = "UPDATE empleados SET salario_neto  = %s WHERE codigo_empleado = %s "
    
    actualizados = 0
    insertados = 0
    
    try:
        cnx = mysql.connector.connect(
            user = username,
            host = host,
            database= database,
            password=pasword
        )
        cursor = cnx.cursor()
        #-----logica del upsert-----
        
            
        for fila in negocio:        
            codigo = fila['codigo']
            nombresCompletos = fila['nombres']
            departamento = fila['departamento']
            salarioNeto = float(fila['salario_neto'])
            cursor.execute(sentencia_select,(codigo,))
            seleccion=cursor.fetchone()
            
            if seleccion != None:
                cursor.execute(sentencia_update,(salarioNeto,codigo))
                actualizados+=1
            elif seleccion ==None:
                cursor.execute(sentencia_insert,(codigo,nombresCompletos,departamento,salarioNeto))
                insertados+=1
            else:
                print("Algo salio mal en el select")

        
        print(f"Reporte de situacion, hubieron {insertados} insertados, {actualizados} actualizados")
        #--------------
        cnx.commit()
        cursor.close()
    except Exception as error:
        
        print("Problemas en la conexion o algo ocurrio mal", error)
    finally:
        if cnx and cnx.is_connected():
            cnx.close()
    return

upsert(host,username,pasword,database,negocio)