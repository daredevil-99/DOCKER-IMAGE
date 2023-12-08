FROM mcr.microsoft.com/windows/servercore:ltsc2019

# Install Python
RUN powershell -Command "wget -Uri 'https://www.python.org/ftp/python/3.9.7/python-3.9.7.exe' -OutFile 'python-3.9.7.exe'" && \
    python-3.9.7.exe /quiet InstallAllUsers=1 PrependPath=1 && \
    DEL python-3.9.7.exe

# Set the working directory
WORKDIR /app

# Copy the application files
COPY . /app

# Upgrade pip
RUN powershell -Command "python -m pip install --upgrade pip"

# Install requirements
RUN powershell -Command "python -m pip install -r requirements.txt"

# Expose port (if needed)
EXPOSE 5000

# Set the entry point
CMD ["python", "app.py"]


