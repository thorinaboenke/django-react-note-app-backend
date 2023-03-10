# Note App with Django and React

## Backend

You have to have python 3 installed

### Clone repository
```bash
git clone git@github.com:thorinaboenke/django-react-note-app-frontend.git
cd backend
```

### Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install django djangorestframework django-cors-headers
```

### Start the server
```bash
python manage.py runserver
```

App is running on localhost:8000

Urls:
| Url         | Description                         |
| ----------- | ------------------------------------|
| admin/      | Django admin interface              |
| api/notes   | Api Endpoint for Note List          |

![image](https://user-images.githubusercontent.com/68156005/224311952-ed805fa3-ceed-4bda-be27-fc7b53b33e6d.png)


## Frontend
### clone repository
```bash
git clone git@github.com:thorinaboenke/django-react-note-app-backend.git
cd Frontend
```

### Install dependencies and start App
```bash
npm install
npm run
```

App is running on localhost:3000

### Usage
Fill a not (140 characters max.) in the text field, click 'Post my Note'

Check the Box "I don't like coffee" to hide all notes containing the word coffee.

![image](https://user-images.githubusercontent.com/68156005/224311528-96c3c705-5f18-4e99-9a09-75f50d262379.png)
