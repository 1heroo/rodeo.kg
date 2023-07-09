# Запуск бекенда для rodeo.kg

До этого нужно приготовить поддомент ```api.rodeo.kg``` для 12500 порта машины, проект будет запущен именно на этом порту 


- Установить на машине следующие приложение: git, docker, docker-compose 
- Клонировать исходный код бекенда rodeo.kg командой 
```git clone https://github.com/1heroo/rodeo.kg``` 

- Перейти в директорию с проектом

- Создать файл переменных окуржения `.env` в директории `source/` со следующим содержанием:


```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=admin
POSTGRES_HOST=db
POSTGRES_DB_NAME=rodeo_db
POSTGRES_PORT=5432


HOST=https://api.rodeo.kg
```

- Запустить проект командой: ```docker-compose -f local.yml up --build -d```


Все, проект запущен, доступ к автоматически сгенерированной документации API http://yourip:12500/redoc/ или https://api.rodeo.kg/redoc.
Доступ к админке проекта http://yourip:12500/admin/ или https://api.rodeo.kg/admin/


-> Отключить проект можно командой ```docker-compose -f local.yml down```
Если возникли ошибки с базой данных, просто перезагрузите проект
