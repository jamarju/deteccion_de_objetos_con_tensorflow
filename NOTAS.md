# Experimentos

- 2 = 1 con más vídeos
- 3 = 2 ??
- 4 = 3 con augs color_distort, steps = 10000
- 5 = 4 con augs brillo y contraste, steps = 3000
- 6 = 5 con cajas 100x100 (solo vertices)
- 7 = 6 con cajas 100x100 (todas)
- 8 = 7 con cribado MSE entre fotos < 30 (training set baja a 958)
- 9 = 8 con steps /= 4
- a = 9 con lr=1e-2
- b = a con lr=1e-1

# Notas

- las imágenes en tensorboard empiezan a aparecer a los 10 minutos (throttle_secs)

# Cribado de similares

python filtra_similares.py -d train mytrain-cajas-org.csv mytrain-distintas.csv

# Agranda cajas

python agranda_cajas.py mytrain-distintas.csv mytrain.csv 100

# Vídeo en el terminal por ssh

export CACA_DRIVER=ncurses
mplayer -really-quiet -vo caca exp8_valid.mp4

