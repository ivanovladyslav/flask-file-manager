# flask-file-manager

Просмотр содержимого директории:
http://localhost:5000/index?d=/Your/Path
Пример: 
http://localhost:5000/index?d=/vladislav/downloads/

По параметру d передается путь директории, которую необходимо просмотреть (простой фронтенд реализован в templates/index.html)

Создание папки:
http://localhost:5000/create?d=/Your/Path&name=NameOfFolder
Пример:
http://localhost:5000/create?d=/vladislav/downloads&name=newFolder

По параметру name передается имя создаваемой папки

Удаление папки:
http://localhost:5000/delete?d=/Your/Path&name=NameOfFolder
Пример:
http://localhost:5000/delete?d=/vladislav/downloads/&name=newFolder

По параметру name передается имя удаляемой папки

Скачивание файлa:
http://localhost:5000/download?d=/Your/Path/NameOfFile
Пример:
http://localhost:5000/download?d=/vladislav/downloads/lab1.png

Родительская директория по умолчанию - /Users

Проверка на наличие уже существующих папок при создании одноименной отсутствует.
Проверка на существование удаляемой папки также отсутствует.


