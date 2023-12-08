FROM mcr.microsoft.com/windows/servercore:ltsc2019
WORKDIR \app
COPY . \app
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", ".\app.py"]


