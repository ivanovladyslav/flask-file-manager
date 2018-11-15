# flask-file-manager

Просмотр содержимого директории:
http://localhost:5000/index?d=/Your/Path
Пример: 
http://localhost:5000/index?d=User/vladislav/downloads

По параметру d передается путь директории, которую необходимо просмотреть (простой фронтенд реализован в templates/index.html)

Создание папки:
http://localhost:5000/create?d=/Your/Path/NameOfFolder
Пример:
http://localhost:5000/create?d=User/vladislav/downloads/newFolder

Удаление папки:
http://localhost:5000/delete?d=/Your/Path/NameOfFolder
Пример:
http://localhost:5000/delete?d=User/vladislav/downloads/newFolder

Скачивание файлa:
http://localhost:5000/download?d=/Your/Path/NameOfFile
Пример:
http://localhost:5000/download?d=User/vladislav/downloads/lab1.png

Родительская директория по умолчанию - /Users



