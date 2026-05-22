# =========================================
# BASE IMAGE
# =========================================

FROM python:3.10-slim


# =========================================
# WORKDIR
# =========================================

WORKDIR /app


# =========================================
# SYSTEM DEPENDENCIES
# =========================================

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*


# =========================================
# COPY PROJECT FILES
# =========================================

COPY . .


# =========================================
# INSTALL PYTHON DEPENDENCIES
# =========================================

RUN pip install --upgrade pip

RUN pip install -r requirements.txt


# =========================================
# EXPOSE PORTS
# =========================================

EXPOSE 8000
EXPOSE 8501


# =========================================
# START FASTAPI + STREAMLIT
# =========================================

CMD uvicorn main:app --host 0.0.0.0 --port 8000 & \
    streamlit run streamlit_app.py \
    --server.port 8501 \
    --server.address 0.0.0.0