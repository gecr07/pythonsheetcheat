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

<h2> Regular Expr</h2> 
<h3> Lookahead and Lookbehind</h3>
<ol>
<li>bar(?=bar)     finds the 1st bar ("bar" which has "bar" after it)           </li>
<li> bar(?!bar)     finds the 2nd bar ("bar" which does not have "bar" after it)</li>
<li> (?<=foo)bar    finds the 1st bar ("bar" which has "foo" before it)            </li> 
  
#(?<!foo)bar    finds the 2nd bar ("bar" which does not have "foo" before it) 
  
</ol>
