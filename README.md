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

Es un  modulo que tiene python integrado compite con virtualenv para evitar problemas usaremos el anterior ay mas documentacion.

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



