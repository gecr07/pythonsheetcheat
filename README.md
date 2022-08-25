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

### Que pasa cuando haces pip

> TAR file (tarball) named uwsgi-2.0.18.tar.gz that’s been compressed with gzip.

1. Cuando se usa pip se descarga un archivo tar.gz el cual se le llama ***tarball***
2. Se genera un archivo .whl
>On line 6, it takes the tarball and builds a .whl file through a call to setup.py
3. En la línea 7 , etiqueta la rueda uWSGI-2.0.18-cp38-cp38-macosx_10_15_x86_64.whl.
4.  instala el paquete real después de haber construido la rueda.

Todo lo anterior en un caso ideal que se instale bien python es aberrante y cambia todo el tiempo revislo


## sdist

> El tar.gztarball que piprecupera es una distribución de origen , o sdist, en lugar de una rueda. De alguna manera, a sdistes lo opuesto a una rueda.
> Una distribución fuente contiene código fuente. Eso incluye no solo el código de Python, sino también el código fuente de cualquier módulo de extensión (generalmente en C o C++ ) incluido con el paquete. Con las distribuciones de código fuente, los módulos de extensión se compilan del lado del usuario en lugar del desarrollador.

Osea que un *** source distribution*** traes todo el codigo fuente incluso archivos que son e c o c++ y se supone se compila de lado del cliente cuanod lo descargas vaya.

## PyPI

> El Python Package Index o PyPI es el repositorio de software oficial para aplicaciones de terceros en el lenguaje de programación Python. Los desarrolladores de Python pretenden que sea un catálogo exhaustivo de todos los paquetes de Python escritos en código abierto1​

