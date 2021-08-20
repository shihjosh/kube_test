
```bash
docker-compose run --rm app sh -c "python manage.py startapp core"
docker-compose run --rm app sh -c "python manage.py makemigrations"
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```

開發基本流程

templates > urls > views


USE ngrok

```bash
ngrik http <port>
```

settings.py need add ALLOWED_HOSTS = ['9dcd6d458855.ngrok.io']

---
api:GET POST PUT DELETE
```bash
[
    {
        "DepartmentId": 1,
        "DepartmentName": "IT"
    },
    {
        "DepartmentId": 2,
        "DepartmentName": "Support"
    }
]
```