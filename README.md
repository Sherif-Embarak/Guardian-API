### Guardian-API Installation
##### 1- download the repo
##### 2- download and install  python3.6
##### 3- open cmd and cd to "/path/to/downloaded/repo/"
###### example: cd C:\Users\<user>\OneDrive\Documents\Guardian-API
##### 4- virtualenv -p "/path/to/installed/python.exe"  venv
###### example: virtualenv -p "C:\Users\<user>\AppData\Local\Programs\Python\Python36\python.exe"  venv
##### 5- cd /venv/scripts
##### 6- activate
##### 7- cd to "/path/to/downloaded/repo/"
##### 8- pip install -r requirements.txt
##### 8- python manage.py runserver 8080
### Guardian-API Usage:
##### http://127.0.0.1:8080/api/articles?article_txt=(word_to_search)&writer=(writer_to_search)&return='list_of_fields_to_return(separate_by_comma)'
###### example: http://127.0.0.1:8080/api/articles?article_txt=president&writer=tom&return=article_txt,article_write
###### fields: article_txt,article_tile,article_writer,article_time,article_url,category,subcat
