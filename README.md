# Detección de objetos con Tensorflow

## Prerrequisitos

* Drivers nvidia:

```
sudo add-apt-repository ppa:graphics-drivers/ppa
sudo apt update
sudo apt upgrade
sudo apt install nvidia-driver-410 xserver-xorg-video-nvidia-410
```

* Instalar anaconda

* Paquetes adicionales:

```
apt install axel ffmpeg
```

* Crear entorno virtual para deep learning (tensorflow-gpu, opencv, fastai, keras, pandas, pandas,  etc.)

```
conda env create -n dl -f=conda/env.yml
```

* Bajar https://github.com/tensorflow/models y descomprimir en `~/git`

* Arreglar esto a mano mientras no acepten el PR: https://github.com/tensorflow/models/pull/6044/files

* Compilar los protobuffers:

```
# Desde tensorflow/models/research/
protoc object_detection/protos/*.proto --python_out=.
```

* Del [zoo de modelos de tensorflow](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) bajar `ssd_mobilenet_v1_ppn_coco`, mover a `pretrained_model`:

```
# Desde el directorio de este repo
mkdir pretrained_model
cd pretrained_model
axel -a http://download.tensorflow.org/models/object_detection/ssd_mobilenet_v1_ppn_shared_box_predictor_300x300_coco14_sync_2018_07_03.tar.gz
tar xvzf ssd*tar.gz
```

## Instrucciones rápidas

* Activar entorno `dl`

```
conda activate dl
```

* Meter datos en train/ y valid/

* Generar datos. Este script:
  * Criba frames similares
  * Agranda cajas a 100 px mínimo
  * Convierte a .csv intermedio para `generate_tfrecord.py`
  * Genera los .record para Tensorflow

```
./gen.sh
```

* Entrenar:

```
./entrena.sh
```

* Visualizar los datos (en otro terminal):

```
conda activate dl
./tb.sh
```

* Congelar grafo para inferencia: editar en `congela.sh` la variable `STEP` apuntando al checkpoint deseado y:

```
./congela.sh
```

* Para inferir imágenes: editar `anota_video.py`, cambiar `PATH_TO_FROZEN_GRAPH` (grafo de inferencia) y `PATH_TO_TEST_IMAGES_DIR` (directorio con imágenes a inferir):

```
. vars.sh
python anota_video.py
mkdir pngs
mv *.png pngs
```

* Para reconstruir vídeo con anotaciones:

```
cd pngs
../pngs2mp4.sh
```

(resultado: out.mp4)

