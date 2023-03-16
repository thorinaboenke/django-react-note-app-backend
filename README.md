# Note App with Django and React

## Backend

You have to have python 3 installed

### Clone repository
```bash
git clone git@github.com:thorinaboenke/django-react-note-app-backend.git
cd backend
```

### Create virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install django djangorestframework django-cors-headers coverage
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

### Testing
to run test in folder /backend run
```bash
coverage run --omit='*/.venv/*' manage.py test
```
to check test coverage run
```bash
coverage html
```
a folder htmlcov will be created containing an index.html file. open index.html in browser to inspect test coverage

![image](https://user-images.githubusercontent.com/68156005/225372531-c6dd9daf-5ccb-4926-b806-fc2c4e1094d5.png)


## Frontend
### clone repository
```bash
git clone git@github.com:thorinaboenke/django-react-note-app-frontend.git
cd Frontend
```

### Install dependencies and start App
```bash
npm install
npm run
```

App is running on localhost:3000

### Usage
Fill a note (140 characters max.) in the text field, click 'Post my Note'

Check the Box "I don't like coffee" to hide all notes containing the word coffee.

![image](https://user-images.githubusercontent.com/68156005/224311528-96c3c705-5f18-4e99-9a09-75f50d262379.png)



# What risks do you see when designing such an application?

Cyberbullying/hate speech, misinformation, copyright infringements, illegal content, defamation, breaches of privacy/doxxing, discrimination, trolling, spam

Especially the anonymity may embolden users to angange in abovementioned abusive behaviour.

Ultimately the responsibility lies with the platform concerning illegal content etc. and it may be held accountable if no reasonable preventive measures were taken.

# How can you ensure that the application stays a safe space?

### Community Guidelines 📝
Have clear community guidelines, that not only state what content and behaviours in not accepted, but also encourage positive values like supportivness and mindfulness towards others, inclusive language, creating a safe(r) space together. Users need to agree to and accept these guidelines before posting content.

### Possiblity to report/flag problematic content 🚩
Implement features so that users can report harmful or inappropriate content, and encourage them to do so.

### AI assisted filtering 💻
Filter content for text patterns to prevent doxxing/privacy breaches.

Natural Language processing tools, machine learning to identify and flag threats, hate speech..

Analyze use pattern to detect spam/trolling behaviour.

Image recognition to detect and flag inappropriate or offensive images, hate symbols.

These algorithms can be problematic in and of themselves; and depending on the training datasets might create false positives or replicate racial and gender bias.

### Moderation 🕵️
Have moderators to review content posted on the app (spot checks, and when flagged as per point 2 and 3) and take action if necessary (prevent publishing, remove content, ban users etc.).

### Trigger Warnings  ⚠️
For discussing sensitive and potentially triggering topics (for example self-harm), encourage users to add trigger warnings to their posts and/or to use 'spoilers' formatting.

### Transparency 🔍
Be transparent about the measures taken (for example in case content is filtered with algorithms, if use patterns are tracked etc.), no showdow-banning.

### Policies ⚖️
Have policies and an action plan on legal issues in place before an incident occurs.
