# python计时器小工具
***

## 演示
仅需`` 空格键 ``循环调用 ``开始 / 暂停 / 清零 ``

<img src=".\yanshi.gif">

## Windows命令行快捷调用
在任意路径创建vbs文件，使用绝对路径运行timer.py文件
```vbs
Set WshShell = CreateObject("WScript.Shell")
WshShell.Run "D:\Miniconda\envs\play\python.exe D:\Code\PythonCode\newlearnProject\littletools\timer.py", 0, False
```

创建timer.bat文件，放在有环境变量的文件夹（如：System32）,在命令行输入bat的文件名timer即可调用timer.py
```bat
@echo off
start "" "D:\Code\PythonCode\newlearnProject\littletools\timer.vbs"
exit
```
