## Object tracking challenge
El problema propuesto fue implementar un algoritmo de tracking consiste en predecir la posición de un objeto en un 
frame dado sabiendo la posición de dicho objeto en el frame anterior.

Para resolver este challenge, fundamentalmente se utilizó la librería de **Open CV y su módulo de
Multitracking de imágenes** para así poder ir rastreando la posición de varios objetos a la vez; como 
algoritmo o estrategia de rastreo se optó por utilizar el **algoritmo MOSSE** 

Cuando ejecutamos el programa, se captura el primer cuadro de video, con las posiciones iniciales dadas en el archivo
.JSON, que fue leído con la librería pandas para recorrer más fácil su contenido, se le asigna un rastreador a cada una
de las imágenes que están asociadas a esa posición

Luego de que se le asigna un rastreador a cada uno, se va recorriendo cada frame del video y el rastreador va actualizando
las coordenadas de cada imagen que fue asignada, así también se le asigna un Bounding Box para ir visualizando la posición
y rendimiento del algoritmo de tracking seleccionado

**¿Por qué se optó por el algoritmo MOSSE para el seguimiento?**

Además de que se implementó el código con todos los otros 7 algoritmos que provee Open CV para hacer seguimiento de imágenes
y este fue el de mejor desempeño, el algoritmo MOOSE (Minimum Output Sum of Squared Error), usa una correlación adaptativa
con fines de seguimiento que genera filtros de correlación estables. Por lo que lo hace robusto frente a escalas, poses y deformaciones
y un algoritmo ideal para este tipo de videos que las imágenes a seguir son bastante dinámicas


Video donde se puede visualizar como es el funcionamiento del modelo de forma local: https://drive.google.com/file/d/14jBFX4yGPHpP2NnxZOaxFC-pkr-uSdZZ/view?usp=sharing
