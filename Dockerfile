FROM python:3.10.6
EXPOSE 5000
WORKDIR /app
COPY Pipfile Pipfile.lock 
RUN pip install pipenv
COPY . .
CMD ["flask","run", "--host","0.0.0.0"]