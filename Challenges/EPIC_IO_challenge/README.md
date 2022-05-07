## Object tracking challenge

**Español:**

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

Video donde se puede visualizar como es el funcionamiento del modelo de forma local / Video where you can see how the model works locally: https://drive.google.com/file/d/14jBFX4yGPHpP2NnxZOaxFC-pkr-uSdZZ/view?usp=sharing

**English:**

The proposed problem was to implement a tracking algorithm that consists of predicting the position of an object in a
given frame knowing the position of said object in the previous frame.

To solve this challenge, the **Open CV library and its Image Multitracking module** were fundamentally used to be able to track the position of several objects at the same time; What algorithm or tracking strategy it was decided to use the **MOSSE algorithm**

When we execute the program, the first video frame is captured, with the initial positions given in the .JSON file, which was read with the pandas library to navigate its content more easily, a tracker is assigned to each of the images that are associated with that position

After a tracker is assigned to each one, each frame of the video is traversed and the tracker updates the coordinates of each image that was assigned, as well as a Bounding Box is assigned to visualize the position and performance of the algorithm of selected tracking

**Why was the MOSSE algorithm chosen for tracking?**

In addition to the fact that the code was implemented with all the other 7 algorithms that Open CV provides to track images and this was the one with the best performance, the MOOSE algorithm (Minimum Output Sum of Squared Error), uses an adaptive correlation for tracking purposes which generates stable correlation filters. For what makes it robust against scales, poses and deformations and an ideal algorithm for this type of videos that the images to follow are quite dynamic
