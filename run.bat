@echo off
echo ======== 开始执行测试 ========

:: 安装依赖
pip install -r requirements.txt

:: 清理上次结果
if exist allure-results rd /s /q allure-results

:: 执行测试
pytest testcases/ -v --alluredir=./allure-results

echo ======== 测试执行完毕 ========