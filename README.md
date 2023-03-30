# SpiderFoot_dns_resolver_module
SpiderFoot DNS Resolver Module

# Máster en Dirección de Ciberseguridad, Hacking Ético y Seguridad Ofensiva XV
## RESOLUCIÓN DE LA ACTIVIDAD2
### Alumno: Enrique López Patau



Se ha realizado un módulo de SpiderFoot a partir de la plantilla proporcionada que lo que hace
es resolver la IP para el nombre de dominio proporcionado.

El nombre interno del módulo es: **sfp_elpdnsresolver**

El nombre atiende a la siguiente nomenclatura: 
* sfp indica que es un módulo de spiderfoot
* elp indica que es de Enrique Lopez Patau 
* dnsresolver indica que resuelve nombre de DNS

El nombre que se le ha dado para el listado de módulos de la interfaz web es: **ELP DNS Resolver**

### EJECUCIÓN DEL MÓDULO

Para ejecutarlo, se debe copiar en el directorio en el que estén los módulos de spiderfoot y
lanzar el módulo por línea de comandos o mediante la interfaz web.

En mi caso, utilizaba la última versión de Kali Linux con lo que el módulo hay que copiarlo en el path:

/usr/share/spiderfoot/modules/

y, si queremos invocarlo desde línea de comandos, lo haremos con la siguiente instrucción:

`spiderfoot -m sfp_elpdnsresolver -s <nombre_dominio>`

Un ejemplo de invocación podría ser:

`spiderfoot -m sfp_elpdnsresolver -s www.google.es`

y también se puede poner:

`spiderfoot -m sfp_elpdnsresolver -s google.es`

Dado que se adminten campos del tipo DOMAIN_NAME e INTERNET_NAME
