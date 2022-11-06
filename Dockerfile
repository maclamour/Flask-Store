FROM python:3.10.6
EXPOSE 5000
WORKDIR /app
COPY Pipfile .
COPY Pipfile.lock .
RUN pip install Pipfile
COPY . .
CMD ["flask","run","--host","0.0.0.0"]
