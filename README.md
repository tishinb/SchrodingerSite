## [RU] Инструкция по установке и запуску
### Установка на Linux
1. Установка репозитория.

```
git clone https://github.com/tishinb/SchrodingerSite.git
```

2. Создание Docker-образа

```
sudo docker build -t [имя образа]:[имя тега] .
```

Например:

```
sudo docker build -t tbvdockerflask .
```

3. Запуск Docker-образа

```
sudo docker run tbvdockerflask
```
