FROM python:3.9
COPY ./templates/ /py_app/templates/
COPY *.py /py_app
EXPOSE 8080
WORKDIR /py_app
RUN pip install psycopg2-binary
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install Jinja2
CMD ["python", "/py_app/main.py"]