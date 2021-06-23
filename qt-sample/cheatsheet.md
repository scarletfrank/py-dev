# Mannal

> 待整理逻辑，参考[learnpyqt](https://www.learnpyqt.com/courses/packaging-and-distribution/packaging-pyqt5-pyside2-applications-windows-pyinstaller/)写的。原作者写的真不错

## 单纯用命令行管理

```shell
# Default build process
pyinstaller app.py
# Afterwards build process
pyinstaller app.spec
# 先运行，生成.spec，之后可以一直按.spec重复build
```

### 更改exe名字

更改`.spec`

```conf
name = 'qt5-sample'
```

或者

```shell
pyinstaller --name "Hello World" app.py
```

### 去掉Console

还是`.spec`

```conf
console=False
```

Alternatively,

```shell
pyinstaller -w app.py
# or
pyinstaller --windowed app.py
# or
pyinstaller --noconsole app.py

```

### 单文件打包

```shell
pyinstaller --onefile app.py
```

## 用Qt Designer管理


### qrc文件

手工写来处理引用

```shell
# Shell
pyrcc5 resources.qrc -o resources.py
# .py中
import resources
```


### 更复杂的UI

用Qt Designer编辑一个`.ui`，同时引入或新建`.qrc`（里面导入了ui和icon）

之后就可以用以下的命令

```shell

pyrcc5 resources.qrc -o resources.py # 每一次更改UI都要更新资源
python app.py # 测试用
pyinstaller --windowed --icon=resources/favicon.ico app.py #打包用
```