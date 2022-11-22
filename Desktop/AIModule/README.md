# AI Module

В этом модуле описываются:
* разработанная модель машинного обучения;
* код для ее обучения в виде .ipynb блокнотов;
* сохраненная обученная модель, готовая для использования.

## Установка Python и среды разработки
Для разработки рекомендуется использовать VS Code или подходящую IDE, поддерживающую работу с Python и Jupyter Notebooks.

Необходим установленный Python версии 3 и выше (разработчиками использовался Python версии 3.9 и выше).

Необходимо установить Jupyter любым доступным способом (рекомендуется установить с помощью [расширения Jupyter для VS Code](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) и/или установть [Jupyter Notebooks с официального сайта](https://jupyter.org/install))

## Установка необходимых библиотек Python
tensorflow - библиотека для машинного обучения и нейросетей в частности.</br>
keras - библиотека для взаимодействия с нейронными сетями.</br>
numpy - библиотека для работы с массивами данных и их обработки.</br>
librosa - библиотека для анализа музыки и аудио.</br>
jams - библиотека для работы с JAMS файлами.
```bash
pip install tensorflow
pip install keras
pip install numpy
pip install librosa
pip install jams
```

## Загрузка датасета для обучения модели
В качестве датасета используется GuitarSet. Он содержит в себе аудиофайлы в формате .wav и аннотации к ним в формате .jams (JSON Annotated Music Specification). Количество файлов обоих типов - по 360 каждого.

Основной сайт для его скачивания - [GuitarSet](https://zenodo.org/record/3371780#.Y3xyJXbP3x4)

Необходимо скачать два архива:
* [annotation.zip](https://zenodo.org/record/3371780/files/annotation.zip?download=1) - архив с аннотациями. Необходимо распаковать его в папке [./GuitarSet/annotations](./GuitarSet/annotation/). Папка annotations должна выглядеть так:
<p align="center">
  <img src="https://github.com/SharafeevRavil/GuitarClassification/tree/main/Desktop/AIModule/documentation/annotations.png" />
</p>

* [audio_mono-mic.zip](https://zenodo.org/record/3371780/files/audio_mono-mic.zip?download=1) - архив с аудиофайлами. Необходимо распаковать его в папке [./GuitarSet/audio/mic](./GuitarSet/audio/mic/). Папка audio/mic должна выглядеть так:
<p align="center">
  <img src="https://github.com/SharafeevRavil/GuitarClassification/tree/main/Desktop/AIModule/documentation/audio_mic.png" />
</p>
