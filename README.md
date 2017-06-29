SHELL BOT PARA TELEGRAM
=======================

### Instalación
- Enviar un mensaje a @botfather a través de telegram para registrar el bot que 
usaŕas para controlar tu equipo. Este proporcionará la API_KEY para el 
funcionamiento de ese bot.
- Descargar el programa de github.
- Instalar los paquetes necesarios para el funcionamiento del bot (esto en el futuro se hará solo con un script que autodescargue lo necesario)
  + PytelegramBot
  + python 3.5>

### Primera ejecución
- Ejecutar el comando 

`python bot.py --api-key <api-key> --admins <admin1, admin2 ... adminn>`
El _api-key_ es el que ha proporcionado el botfather al crear el bot.
Los _adminn_ son los nombres de usuario de telegram que tendrán permiso para 
poder mandar comandos al bot. **MUY IMPORTANTE**: Por motivos de seguridad, no 
se podrá ejecutar sin especificar ningún usuario ni se recomienda poner un 
usuario aleatorio. No querrás darle las llaves de tu casa a un desconocido o 
dejar la puerta abierta de par en par.

- Una vez hecho esto, ya se puede mandar comandos a nuestro bot como si 
estuviésemos en la propia máquina.

### Para el futuro
- Recibir inputs para acciones de tipo sudo
- ... ¿Sugerencias?

