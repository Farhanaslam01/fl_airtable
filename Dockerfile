FROM python:3.7.1 

WORKDIR /python_fl_airtable

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]