# Django Boiler-plate ![APM](https://img.shields.io/apm/l/python)

This is a simple django boiler plate preinstalled with django-debug toolbar. It is modified such that i can be used in production as well as in development environments.
## Appendix

This project consits of some libraries which makes development in django easy and time saving. It consists of packages helpful for development and is also modified to deploy for production.
## Authors

- [@Aditya Joshi](https://www.github.com/adijoshi82812)
## Feedback

If you have any feedback, please reach out to me at adijoshi82812@gmail.com
## 🚀 About Me

I'm a full stack developer. I use python-django at the Back End and react.js at the Front End.
## How to use

Clone this repository

```bash
  git clone https://github.com/adijoshi82812/django-boilerplate.git
```

Create a virtual environment

```bash
  python3 -m venv backend-env
```

Activate the virtual environment

```bash
  source backend-env/bin/activate
```

Install the requirements.txt

```bash
  python3 install -r requirements.txt
```

### To rename the project run

```bash
  python3 manage.py rename <Name_of_your_project>
```

### Add the .env file

You must add a .env file inside the root directory of this repository. This allows you to use python-decouple. Add your secret-keys, API Keys, Database Credentials, or anything with high privacy inside the .env file

### Apply the migrate command

```bash
  python3 manage.py migrate
```

Done. \
Happy Coding.
## Tech Stack

**Server**: Python, Django Sqlite