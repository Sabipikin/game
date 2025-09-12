FROM python:3.9-slim

# set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY main.py .
COPY templates/ ./templates/

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "main.py"]