use rrhh_rally;

create table empleados (
id int Not null PRIMARY KEY Auto_Increment,
codigo_empleado varchar(50),
nombre_completo varchar(50),
departamwnto varchar(50),
salario_neto decimal(10,2),
fecha_proceso Datetime default CURRENT_TIMESTAMP
);