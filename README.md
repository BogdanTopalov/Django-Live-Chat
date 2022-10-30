# Django-Live-Chat

Django and PostgreSQL live chat application.  
Registered or anonymous users can open chat rooms.  
Staff users can see all opened chat rooms and respond to the users in them.  
Messages are in real-time (web sockets).  
All communication is saved in the DB.  
If registered users have unseen messages from their rooms,  
they will receive notification once they come online again (or refresh the home page if they didn't log out).  


## Quick look:

**Anonymous user:**  
<img src="https://i.postimg.cc/t4nVrzs7/Anonymous-chat.gif" alt="gif"/>

**Registered user:**  
<img src="https://i.postimg.cc/mZ0cPHXs/User-chat.gif" alt="gif"/>

## How to test it?

1. Create venv and activate it:
   - Execute `python -m venv venv` in the folder's terminal.
   - Activate it from `venv\Scripts\activate`.

2. Install requirements:
   - Execute `pip install -r requirements.txt`.

3. Set up DB:
   - Enter your DB parameters in **django_live_chat/setting.py**.
   - Execute `python manage.py makemigrations` in the terminal.
   - Execute `python manage.py migrate` in the terminal.

4. Create superuser:
   - Execute `python manage.py createsuperuser` in the terminal.
   - Example credentials: Username: Staff

5. Start the server:
   - Execute `python manage.py runserver` to start the server on **http://127.0.0.1:8000/**.
   - Open two separate browsers or browser tabs(one normal tab + one incognito tab)

6. Check the **Quick look** above to see what you can do.
