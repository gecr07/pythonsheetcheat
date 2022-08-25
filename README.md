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



