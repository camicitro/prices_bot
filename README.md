<h1 align="center"> BuenosPreciosBot  </h1>

## Introducción
Este proyecto es un bot de telegram para que, seleccionando un supermecado, se pueda buscar los distintos precios de un producto. Está basado en Mendoza (Argentina), por lo que incluye algunos de los supermercados más comunes de ese lugar.
La idea básica de este proyecto, era aprender sobre:
- Web Scraping
- Creación y uso de un bot de telegram
- Creación de prompts útiles

Yo no sabía NADA sobre web scraping ni la creación de bots. Es por eso que decidí aprender de esos temas mediante la realización de este proyecto usando ChatGPT, es decir, intentando darle los mejores prompts posibles para que me ayudara a crear el código junto con una explicación de cada cosa. Además de aprender sobre dichos temas, pude probar diversas formas de hacer prompts y los distintos resultados que daba, tratando de mejorarlos cada vez más.

## Herramientas y tecnologías utilizadas
<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ef/ChatGPT-Logo.svg/2048px-ChatGPT-Logo.svg.png" style="width: 50px; height: auto;" />
  <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTebRBzJhW1BDg-1D9keKRb3e0GXVBUBI1ORA&s" style="width: 50px; height: auto;" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/Telegram_logo.svg/2048px-Telegram_logo.svg.png" style="width: 50px; height: auto;" />
  <img src="https://cdn.iconscout.com/icon/free/png-256/free-python-logo-icon-download-in-svg-png-gif-file-formats--technology-social-media-vol-5-pack-logos-icons-3030224.png?f=webp" style="width: 50px; height: auto;" />
</p>

## Estructura del proyecto
En la carpeta raíz tenemos los siguientes archivos y carpetas:
- logs
  - bot.log
- scraping
  - \_\_init_\_.py
  - atomo_scraper.py
  - base_scraper.py
  - carrefour_scraper.py
  - changomas_scraper.py
  - coto_scraper.py
  - jumbo_scraper.py
  - scraper_factory.py
  - vea_scraper.py
- testing
  - test_atomo_scraping.py
  - test_carrefour_scraping.py
  - test_changomas_scraping.py
  - test_coto_scraping.py
  - test_jumbo_scraping.py
  - test_vea_scraping.py
- utils (actualmente no se usa)
  - \_\_init_\_.py
  - helpers.py 
- bot.py
- requeriments.txt

### bot.py
Este es el archivo principal que contiene el código para ejecutar el bot.
- Importa las funciones de scraping y utilidades desde las carpetas correspondientes.
- Se enfoca únicamente en la lógica del bot y no en el scraping.

### scraping
Esta carpeta contiene los distintos scrapers. Acá utilicé el patrón de diseño "Factory", abstrayendo la creación de estos objetos.
El archivo _base_scraper.py_ tiene la clase BaseScraper que contiene la lógica común a todos los scrapers.
Los distintos scrapers de supermercados, heredan de la clase BaseScraper el método _scrape_.
El archivo _scraper_factory.py_ se encarga de crear instancias de los scrapers específicos según el supermercado seleccionado.

### utils
Esta carpeta contiene archivos que tienen funciones auxiliares que no se relacionan direcamente con la interacción con el bot o con el scraping. Sino con otras coss como el procesamiento de las imagenes o la normalización de los datos. Atualmente no la utilizo pero la idea es en un futuro agregar las imágenes de los productos.

### requeriments.txt
Este archivo tiene un listado de todas las dependencias necesarias para este proyecto. Facilitando la instalación en otros entornos.

### logs
Acá se encuentra el archivo _bot.log_, que sirve para registrar eventos importantes o errores al ejecutar el bot.

## ¿Cómo utilizar el bot?
Simplemente corriendo el archivo desde la carpeta raíz del proyecto con el comando:
```python bot.py``` es posible probar el funcionamiento del bot. Además, hay que agregarlo en telegram. El nombre de usuario del mismo es: @buenos_precios_bot, y el QR:

<div align="center">
  <img src="https://github.com/user-attachments/assets/a33a9c8b-fefd-4ab4-b5ce-ac1701bd456e" style="width: 150px;">
</div>

Una vez esté corriendo nuestro programa, podemos comenzar a interactuar con el bot, para ello hay que iniciarlo mandando el siguiente mensaje:
```/start```. Una vez hecho esto, seguí las instrucciones que da el bot y ¡listo!

### Consideraciones a tener en cuenta
Si es la primera vez que vas a correrlo, es necesario instalar las dependencias. Podés hacerlo instalando una por una o corriendo el archivo requeriments.txt mediante el comando:
```pip install -r requirements.txt```

Recomiendo que primero crees un entorno virtual porque sino vas a instalar las dependencias en tu entorno global y puede traer complicaciones con otros proyectos.

Además, una cosa importante a tener en cuenta, es que necesitás el token del bot, que no está subido. Si querés, podes crear un nuevo bot y obtener el token, después crear el archivo .env dentro de la ruta raíz del proyecto y poner dicho token. Para crear el bot desde telegram, tenes que buscar el siguiente contacto:

<div align="center">
  <img src="https://github.com/user-attachments/assets/943caeb2-b8e7-419b-b891-f4fcec05ca81" style="width: 180px">
</div>

Y después, ejecutar en el chat el comando: ```/start``` y seguir las instrucciones hasta obtener el token.

Por último, tené en cuenta que el scraping lo realicé el día 07/01/2025, por lo que si al momento de probar el bot no te funciona algún supermercado, puede ser que la página haya cambiado. Así que hay que actualizar los códigos del scraping.

<div align="center">
  <img src="https://github.com/user-attachments/assets/af35144c-a2a5-48cd-b087-3175b968d782" style="width: 500px">
</div>

## Conclusiones
Me pareció entretenido realizar este proyecto, principalmente porque pude aprender a hacer web scraping. Además, considero que al hacerlo con ChatGPT, e ir viendo la explicación junto con las ideas del código, aprendí más rápido que siguiendo un curso o video tutorial de youtube.

Con el respecto al uso de ChatGPT, creo que es necesario primero darle un contexto sobre el tema, como los objetivos que queremos cumplir, las herramientas utilizadas, etc. Además, detallar lo mejor posible las funcionalidades básicas que queremos que cumpla, pero siempre manteniéndonos claros y concisos. Una buena idea también es darle algún ejemplo para que entienda el resultado que queremos obtener.
Después de algunas pruebas, también descubrí que lo mejor era escribirle los prompts en inglés.
Lo más importante de todo, es usar lo que nos da el chat como una guía, o al menos revisarlo y así adaptarlo a nuestro proyecto.

### Problemas que se presentaron
Algunos problemas que tuve durante el proyecto fueron:
- Varios de los supermercados tenían una estructura de su página web diferente a los demás, por lo que tuve que realizar un scraper para cada uno.
- Algunas veces no podía definir bien qué selector usar, eso fui solucionándolo a prueba y error.
- Ciertos supermercados, como el "ChangoMas", detectaban que estaban siendo scrapeados si ocultaba la ventana del navegador al usar selenium. Además, tuve también que agregarle un tiempo extra luego de cargar el html de la página para que no lo detectara y tomara bien los productos.
- No pude agregar correctamente las imágenes a los productos porque me detectaba que eran productos diferentes (ya sea el nombre o la imagen), por eso tampoco pude hacer una agrupación de modo que mostrara en un mismo mensaje los precios de los distintos supermercados por producto. La idea sería aprender un poco más y lograr hacerlo en una próxima versión.

### Mejoras a futuro
- Planeo desplegar la aplicación en un servidor para que el bot se ejecute de forma continua y esté disponible para probarlo sin necesidad de correr el programa localmente.
- Que se scrapeen todos los productos en un proceso en segundo plano cada cierta cantidad de horas o dias y lo guarde en una BD. Entonces que el bot realice la búsqueda directamente en la BD.
- Agregar la opción "Todos" para que busque en todos los supermercados a la vez.
- Agregar imagenes de los productos y agrupar por producto (que en un mensaje ponga el producto seleccionado y los distintos precios de los supermercados). En este caso debería modificar también que al iniciar no solicite un supermercado o que esta funcionalidad se muestre al seleccionar la opción de "Todos".
- Agregar búsquedas por categorías.



