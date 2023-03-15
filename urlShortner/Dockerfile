FROM --platform=$BUILDPLATFORM python:3.10
EXPOSE 8000
WORKDIR /urlShortner 
COPY requirements.txt /urlShortner
RUN pip install -r requirements.txt --no-cache-dir
COPY . /urlShortner 
ENTRYPOINT ["python3"] 
CMD ["manage.py", "migrate"]
CMD ["manage.py", "runserver", "0.0.0.0:8000"]