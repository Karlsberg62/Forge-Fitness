import os
#Keep the DEBUG line to migrate to the local database. Comment the line out to migrate to the ElephantSQL Database.
os.environ.setdefault("DEBUG","1")
#Connection to ElephantSQL
os.environ.setdefault("DB_URL",'postgres://ehziason:m51DJy5yioppEOqt8JxOTYlj-aDkLSLX@flora.db.elephantsql.com/ehziason')
#Secret Key
os.environ.setdefault("SK", '175986gjhit#!?34549')