FROM python:3.8

WORKDIR /cleverti

# Install dependencies
RUN pip install --upgrade pip

# Copy whole project to docker home directory.
COPY . /cleverti
# Install all dependencies on requirements.txt
RUN pip install -r requirements.txt
# Port where the Django app runs
EXPOSE 8000
# Start django server and run entrypoint with migrations
RUN chmod +x /cleverti/entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]
CMD [ "python", "./manage.py runserver 0.0.0.0:8000" ]
