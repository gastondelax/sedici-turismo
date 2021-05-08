# sedici-unlp
Raspado de fichas de tesis de turismo del repositorio del Servicio de Difusión de la Creación Intelectual (SeDiCI), UNLP. 
El primer archivo contiene script para obtener el listado de url de las fichas de tesis de grado de la Licenciatura en Turismo; resultado se exporta a archivo excel.
  Se aconseja tener una única URL con todas las fichas de interés. Para ello, modificar en Url el límite máximo de fichas visibles en la misma página.
El segundo archivo contiene scrip para obtener los campos de cada tesis. Se itera sobre cada url del excel generado con archivo 1, a fin de obtener autor, año, director, título y subtítulo y resumen. Resyutado: dataframe. Se exporta a archivo Excel.
Ambos archivos escritos en Python. 
Se utilizan las librerias request, beauitiful soup y pandas.
La escructura el HTML de SEDICI es irregular. En caso de utitlizar el código para otra clase de fichas, se aconseja agregar condicionales en la iteración de los campos en archivo 2.
