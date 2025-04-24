# Cloud Storage

> Proyecto -> Bucket -> objetos(archivos en cualquier formato, carpetas..)

## CONCEPTOS:
- ***BUCKET_NAME***: id del depósito.
- ***OBJECT_NAME***: id del objeto.
- #***NUMBER***: agregado al final del nombre del recurso, indica la generación especifica del objeto(version, ej: #0)

## Permite:
-  Buckets con espacio de nombres jerárquico habilitado

## Se puede interacturar por medio de:
- Console Google Cloud
- CLI Google Cloud
- Bibliotecas cliente(Python, Javam Node.js, C#, C++..)
- Terraform: herramienta de infraestructura como código (IaC)
- Cloud Storage FUSE
- gRPC: framework de RPC universal de código abierto

## Seguridad:
- IAM: lo usa para controlar quién tiene acceso a los recursos del proyecto. Se puede otorgar ciertos tipos de acceso a buckets y objetos, como update, create o delete.
- Encriptación de datos: usa la encriptación del lado del servidor de forma predeterminada. También hay opciones complementarias como encriptación por medio de **claves de encriptación administradas por el cliente** y **claves de encriptación proporcionadas por el cliente**.
- Autenticación: se asegura de que cualquier persona que acceda a tus datos tenga las credenciales adecuadas.
- Bloqueo del bucket: permite determinar durante cuánto tiempo se deben retener los objetos en los buckets mediante la **especificación de una política de retención**.
- Eliminación no definitiva: evita la pérdida permanente de datos contra la eliminación accidental o maliciosa mediante la retención de 7dias de objetos y buckets borrados recientemente.
- Control de versiones de objetos: cuando se reemplaza o borra una versión publicada de un objeto, puede retenerse como una versión no actual si **habilitas el control de versiones de objetos**.
- Filtrado de IP de bucket: Con el filtrado de IP de bucket, puedes restringir el acceso a un bucket según la dirección IP de origen de la solicitud y proteger tus datos del acceso no autorizado desde direcciones IP específicas o la nube privada virtual (VPC).


## Creación desde consola Google Cloud
### 1. seleccionar proyecto

### 2. Buscar servicio `cloud storage`


### 3. Crear bucket


#### 3.1. Información basica


#### 3.2. Ubicación


#### 3.3. Clase de almacenamiento


#### 3.4. Control de acceso
![alt text](/assets/image.png)

#### 3.5. Seguridad
![alt text](/assets/image-2.png)

#### 3.6. Confirmar
![alt text](/assets/image-1.png)

#### 3.7. Bucket creado
![alt text](/assets/image-3.png)


## Uso desde biblioteca de cliente(python)
> Primero, se debe configurar cliente de GCP (con credenciales)
### 1. Buscar servicio `IAM y Administración`
![alt text](/assets/image-4.png)

#### 1.1. Ir a `Cuentas de servicio`
![alt text](/assets/image-5.png)

#### 1.2. Crear una cuenta de servicio
![alt text](/assets/image-6.png)

#### 1.2. Detalles
![alt text](/assets/image-7.png)

#### 1.2. Asignar rol
![alt text](/assets/image-9.png)

#### 1.2. Mas permisos(opcional)
![alt text](/assets/image-10.png)

#### 1.2. Cuenta de servicio creada
![alt text](/assets/image-11.png)

#### 1.2. Crear claves de acceso
![alt text](/assets/image-12.png)

![alt text](/assets/image-13.png)

![alt text](/assets/image-14.png)

![alt text](/assets/image-15.png)

![alt text](/assets/image-16.png)

![alt text](/assets/image-17.png)

### 2. Buscar servicio `cloud storage`
### 2. Buscar servicio `cloud storage`