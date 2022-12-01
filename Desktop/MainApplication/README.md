# MainApplication

В этом модуле описываются:
* пользовательский интерфейс десктопного приложения;
* его логика для взаимодействия с моделью машинного обучения и сервером.

## Установка Python и среды разработки
Для разработки рекомендуется использовать VS Code или подходящую IDE, поддерживающую работу с Python и QT.

Необходим установленный Python версии 3 и выше (разработчиками использовался Python версии 3.9 и выше).

Необходимо установить средство для работы с QT любым доступным способом (рекомендуется установить с помощью [расширения Qt for Python для VS Code](https://marketplace.visualstudio.com/items?itemName=seanwu.vscode-qt-for-python) и/или установть [Qt Creator с официального сайта](https://www.qt.io/product/development-tools))

## Установка необходимых библиотек Python
Используемые библиотеки:</br>
* PySide6 - библиотека для реализации пользовательского интерфейса на платформе QT с помощью Python.</br>
```bash
pip install pyside6
```

## Преднастройка расширения Qt for Python
При использовании расширения Qt for Python при разработке необходимо сначала прописать пути к библиотеке PySide6 в настройках расширения. Для этого необходимо указать пути до следующих файлов, находящихся в папке Scripts вашей версии Python:

* Qt For Python › Designer: pyside6-designer.exe
* Qt For Python › Qmllint: pyside6-qmllint.exe
* Qt For Python › Rcc: pyside6-rcc.exe
* Qt For Python › Uic: pyside6-uic.exe

После этого в палитре комманд (Ctrl+Shift+P) вам будут доступны команда Compile Qt UI File, с помощью которой возможно скомпилировать .ui файл в файл на языке Python.