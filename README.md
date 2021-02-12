## my-project
##ถ้าขึ้น chuntika@LAPTOP-IAOG2T3D MINGW64 ~ (main)
#$ git config --global user.name "chuntikab"
#$ git config --global user.email "my..@gmail.com"
#$ git config --global user.password "mypass..."
#$ cd /c/Users/chuntika/gitHub

##เมื่อเปลี่ยนเป็น chuntika@LAPTOP-IAOG2T3D MINGW64 ~/gitHub (main)
#$ git status
  $ git status
  On branch main
  Your branch is up to date with 'origin/main'.

  Untracked files:
    (use "git add <file>..." to include in what will be committed)
          djangoworkshop/

  nothing added to commit but untracked files present (use "git add" to track)

#$ git add .

#$ git status
On branch main
Your branch is up to date with 'origin/main'.

Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
        new file:   djangoworkshop/db.sqlite3
        new file:   djangoworkshop/djangoworkshop/__init__.py
        new file:   djangoworkshop/djangoworkshop/__pycache__/__init__.cpython-39.pyc
        new file:   djangoworkshop/djangoworkshop/__pycache__/settings.cpython-39.pyc
        new file:   djangoworkshop/djangoworkshop/__pycache__/urls.cpython-39.pyc
        new file:   djangoworkshop/djangoworkshop/__pycache__/wsgi.cpython-39.pyc
        new file:   djangoworkshop/djangoworkshop/asgi.py
        new file:   djangoworkshop/djangoworkshop/settings.py
        new file:   djangoworkshop/djangoworkshop/urls.py
        new file:   djangoworkshop/djangoworkshop/wsgi.py
        new file:   djangoworkshop/manage.py
        new file:   djangoworkshop/store/__init__.py
        new file:   djangoworkshop/store/__pycache__/__init__.cpython-39.pyc
        new file:   djangoworkshop/store/__pycache__/admin.cpython-39.pyc
        new file:   djangoworkshop/store/__pycache__/models.cpython-39.pyc
        new file:   djangoworkshop/store/__pycache__/views.cpython-39.pyc
        new file:   djangoworkshop/store/admin.py
        new file:   djangoworkshop/store/apps.py
        new file:   djangoworkshop/store/migrations/__init__.py
        new file:   djangoworkshop/store/migrations/__pycache__/__init__.cpython-39.pyc
        new file:   djangoworkshop/store/models.py
        new file:   djangoworkshop/store/templates/index.html
        new file:   djangoworkshop/store/tests.py
        new file:   djangoworkshop/store/views.py
        
        
        
#$ git commit -m "ใส่ข้อความบ่งบอกว่าเปลี่ยน/เพิ่มอะไร"
[main 6b8ef96] add project django
 24 files changed, 233 insertions(+)
 create mode 100644 djangoworkshop/db.sqlite3
 create mode 100644 djangoworkshop/djangoworkshop/__init__.py
 create mode 100644 djangoworkshop/djangoworkshop/__pycache__/__init__.cpython-39.pyc
 create mode 100644 djangoworkshop/djangoworkshop/__pycache__/settings.cpython-39.pyc
 create mode 100644 djangoworkshop/djangoworkshop/__pycache__/urls.cpython-39.pyc
 create mode 100644 djangoworkshop/djangoworkshop/__pycache__/wsgi.cpython-39.pyc
 create mode 100644 djangoworkshop/djangoworkshop/asgi.py
 create mode 100644 djangoworkshop/djangoworkshop/settings.py
 create mode 100644 djangoworkshop/djangoworkshop/urls.py
 create mode 100644 djangoworkshop/djangoworkshop/wsgi.py
 create mode 100644 djangoworkshop/manage.py
 create mode 100644 djangoworkshop/store/__init__.py
 create mode 100644 djangoworkshop/store/__pycache__/__init__.cpython-39.pyc
 create mode 100644 djangoworkshop/store/__pycache__/admin.cpython-39.pyc
 create mode 100644 djangoworkshop/store/__pycache__/models.cpython-39.pyc
 create mode 100644 djangoworkshop/store/__pycache__/views.cpython-39.pyc
 create mode 100644 djangoworkshop/store/admin.py
 create mode 100644 djangoworkshop/store/apps.py
 create mode 100644 djangoworkshop/store/migrations/__init__.py
 create mode 100644 djangoworkshop/store/migrations/__pycache__/__init__.cpython-39.pyc
 create mode 100644 djangoworkshop/store/models.py
 create mode 100644 djangoworkshop/store/templates/index.html
 create mode 100644 djangoworkshop/store/tests.py
 create mode 100644 djangoworkshop/store/views.py
 
 
 
 #$ git push -u origin main






