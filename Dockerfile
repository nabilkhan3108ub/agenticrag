FROM python:3.11-slim

WORKDIR /app

# Install the CPU-only build of torch first (avoids ~2GB of unused CUDA/GPU libs)
RUN pip install --no-cache-dir torch --index-url https://download.pytorch.org/whl/cpu

# Then install the rest of the dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ ./app/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
