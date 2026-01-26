# PostlyFast

PostlyFast is a Django-based web application that allows users to create, view, and manage posts. The app includes user authentication features such as login, registration, and logout.

## Features

- User registration and login
- Create, view, and manage posts
- Search posts by username or text content
- Upload media files
- Responsive and simple UI

## Screenshots

![Home Page](https://github.com/Shahriar-Hasan123/postlyFast/blob/main/screenshot/homepage.png)
![Create Post](https://github.com/Shahriar-Hasan123/postlyFast/blob/main/screenshot/create_post.png)
![Login_page](https://github.com/Shahriar-Hasan123/postlyFast/blob/main/screenshot/login.png)
![Registration_page](https://github.com/Shahriar-Hasan123/postlyFast/blob/main/screenshot/register.png)



## Requirements

- Python 3.10+
- Django 5.2.8
- ASGI Ref 3.11.0
- django-cors-headers 4.9.0
- django-filter 25.2
- Pillow 12.0.0 (for image uploads)
- python-decouple 3.8
- sqlparse 0.5.3


## Installation

1. Clone the repository:

```bash
git clone git@github.com:Shahriar-Hasan123/postlyFast.git
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Create a superuser (optional, for admin access):

```bash
python manage.py createsuperuser
```

6. Run the development server:

```bash
python manage.py runserver
```

7. Open your browser and go to:

```
http://127.0.0.1:8000/post
```

## Usage

- Register a new account or login with an existing account.
- Create new posts using the "Create a Post" button.
- View and manage your posts directly from the homepage.

## Folder Structure

```
PostlyFast/
├── post/               # App for handling posts
├── postlyFast/         # Project settings
├── templates/          # HTML templates
├── static/             # CSS, JS, images
├── media/              # Uploaded files
├── manage.py
└── requirements.txt
```
