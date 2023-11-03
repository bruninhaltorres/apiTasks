FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY ./ ./

RUN pip install Django==4.2.7
RUN pip install gunicorn
RUN pip install -r requirements.txt

EXPOSE 8000

# Comando para iniciar o aplicativo usando Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "setup.wsgi"]