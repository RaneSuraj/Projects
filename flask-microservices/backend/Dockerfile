#Base Image
FROM python:3.11-slim

#Working DIR
WORKDIR /app

#copy files
COPY . .

#installing requirments
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000
EXPOSE 5001

#command to run the application
CMD ["python", "app.py"]
