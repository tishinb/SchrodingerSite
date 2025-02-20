## [RU] Инструкция по установке и запуску
### Установка на Linux
1. Установка репозитория.
```
git clone https://github.com/tishinb/SchrodingerSite.git
```
2. Создание Docker-образа
Способ без тега:
```
sudo docker build .
```
Способ с тэгом:
```
sudo docker build -t [имя образа]:[имя тега] .
```
Например:
```
sudo docker build -t tbvdockerflask:1.0 .
```
3. 
