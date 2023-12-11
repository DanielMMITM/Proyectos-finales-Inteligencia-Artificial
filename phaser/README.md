# Proyectos-finales-Inteligencia-Artificial
En este repositorio se encuentran 3 proyectos, el juego de phaser, uno para detección de gente con cubrebocas y otro para detección de flores.

## Phaser
Este juego se modificó para que al momento de ser jugado, mediante un conjunto de datos sea entrenado y posteriormente pueda jugar por su propia cuenta. Esto se hizo mediante una red neuronal multicapa con la librería Synaptic de JavaScript

## Detección de personas con cubrebocas
Para este proyecto se generó un dataset con personas con cubrebocas y personas sin cubrebocas, para ello se utilizó la herramienta Cascade Trainer GUI. Con el XML generado por esta herramienta lo utilizamos en nuestro código para poder hacer detectar cuando una persona trae cubrebocas, esto se comprueba con acceso a la cámara del dispositivo.

## Detección de flores mediante una CNN

Para este proyecto se generó un dataset con 5 flores distintas, algunas fueron sacadas de internet, otras fueron tomadas por mí mediante un video de una flor y la ayuda de OpenCV para poder capturar múltiples fotos mediante el video desde diferentes perspectivas. Este proyecto se logra mediante el uso de una red convolusional, se entrenó para que pueda detectar que flor se está mostrando
