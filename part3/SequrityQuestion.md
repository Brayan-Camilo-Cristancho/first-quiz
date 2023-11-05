### Implicaciones del software

- Una aplicación móvil para Android e iOS.
- Una interfaz web que el cliente puede utilizar en lugar de la aplicación móvil.
- Esto está escrito en Javascript con Next.js.
- Una base de datos MySQL que almacena información del cliente, incluidas contraseñas, direcciones particulares, números de teléfono, etc.
- Un backend de Python implementado en FastAPI
- Tiene 12 empleados de ingeniería de software que tienen acceso completo al sistema, 3 empleados de atención al cliente que pueden ver la información del cliente y realizar cambios en pedidos y cuentas, y un empleado de ventas.

Para mencionar las implicaciones de seguridad es importante evaluar los factores y sus datos proporcionados por Owasp, con el fin de tomar un mejor criterio.
Por ejemplo, factores como:
- Cobertura Máxima y Promedio.
- Tasa de Incidencia Máxima y Promedio.
- Impacto ponderado

### Implicaciones de seguridad
- Tomaría como referencia el riesgo A01:2021-Broken Access Control ya que el acceso al los distintos componentes del software es limitado según el cargo del empleado. Por lo tanto, tendría en cuenta la administración de accesos de control y limitación del (CORS), identificadores de sesión y evaluar el tiempo de los tokens como (JWT), validar que no hayan metadatos o archivos qué revelen información como algún tipo (.git), entre otras implicaciones.
- Validaría el riesgo A02:2021-Cryptographic Failures ya que comprendo de distintas aplicaciones orquestadas que intercambian información, por lo que testearía la información sensible enviada según el lenguaje, tanto para FastAPI, como para Next.js y las aplicaciones móviles. Además, tendría en cuenta recomendaciones de Owasp como, evitar el almacenamiento de datos confidenciales, cifrado de datos en tránsito, deshabilitar almacenamiento en caché, entre otras según se vaya presentando.
- Tendría en cuenta el riesgo A04:2021-Insecure Design ya que el software comprende de una arquitectura compleja y que debe estar bien diseñada para una posterior implementación, por lo que según los componentes hay que establecer un diseño riguroso para no presentar vulnerabilidades. 
- Tendría en cuenta la vulnerabilidad A06:2021-Vulnerable and Outdated Components ya que se comprende de distintos lenguajes de programación. Por lo tanto, se deberá usar módulos, frameworks y librerías actualizadas validando constantemente las vulnerabilidades que cada una presenta y las últimas versiones. También, se tiene que validar cuidadosamente la base de datos determinando privilegios, roles y su almacenamiento en un entorno seguro.
- Según lo determinado en los incisos anteriores, es importante realizar un análisis riguroso de los recursos y componentes donde se aloja todas estas aplicaciones, por ejemplo tener en cuenta los aspectos de seguridad del servicio de Cloud que se esté usando.
- En última instancia, tendría en cuenta la vulnerabilidad A10:2021-Server-Side Request Forgery e implementaría su prevención según la capa del modelo OSI requerida.
