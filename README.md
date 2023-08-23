## API endpoints

### Registration APIs:<br />
/api/users/ (POST) for registration<br />
/api/token/login (POST)<br />
/api/token/logout (POST)<br />

### Menu APIs:<br />
/api/menu-items (GET, POST)<br />
/api/menu-items/`<int:pk>` (GET, PUT, PATCH, DELETE)<br />

### Booking APIs:<br />
/api/bookings/tables/ (GET, POST)<br />
/api/bookings/tables/`<int:pk>` (GET, PUT, PATCH, DELETE)<br />

## Steps to run the app<br />
### 1. Install `pipenv`<br />
```bash
pip install pipenv
```

### 2. Setup MySQL database connection in littlelemon/settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'YOUR_MYSQL_DATABASE_NAME',
        'USER': 'YOUR_USERNAME',
        'PASSWORD': 'YOUR_MYSQL_PASSWORD',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```

### 3. Install dependencies
```bash
pipenv install
```

### 4. Make migrations

```bash
python manage.py makemigrations
```

### 5. Migrate

```bash
python manage.py migrate
```

### 6. Run the app

```bash
python manage.py runserver
```
