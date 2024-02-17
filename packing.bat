@echo off
REM 打包程序
chcp 65001
pyinstaller main.spec
echo 打包完成，按任意键退出。
pause > nul