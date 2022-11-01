# binanen
Libreria binanen
En cuanto a código, dentro del “init”, es donde se exportan los datos haciendo las consultas necesarias a la API de Aemet. Lo único necesario es tener las api keys para utilizarla. Además, dentro del “init” también pasamos los datos desde “Json” a un “Dataframe” para que sea más cómodo trabajar con ellos.
Después hemos creado otra función dentro de la clase que hace lo siguiente:
  1.	Para empezar, te devuelve el nombre de todas las provincias de España y después un Input para que selecciones la que quieres.
  2.	Una vez escrito, la función lo que hace es pasar a mayúsculas el input que has escrito, ya que en el “Dataframe” están todos los nombres de las provincias en mayúsculas. 
    3.	Si en nombre que nos ha devuelto el input no concuerda con ninguno de nuestro “Dataframe”, le vuelve a pedir un nombre de provincia. Así hasta que coincida con alguno.
  4.	La función filtra todos los puntos de información que tiene la provincia seleccionada, y en otro input, vuelve a pedir que selecciones un nombre de los que tenemos de esa provincia.
  5.	Una vez elegido el nombre otra vez, lo pasa a mayúsculas, y si no coincide con ningún nombre de esa provincia, vuelve a pedir otro nombre.
  6.	Finalmente, la clase te devuelve la latitud y la longitud del lugar seleccionado.
