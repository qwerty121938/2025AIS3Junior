FROM ubuntu:22.04

# Install dependencies
RUN apt-get update && \
    apt-get install -y apache2 python3 python3-venv python3-pip && \
    apt-get clean

# Copy project files into container
WORKDIR /var/www/html
COPY apache-test ./apache-test

# Set up Python backend
WORKDIR /var/www/html/apache-test/backend
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install -r requirements.txt

# Copy Apache config
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf

# 啟用 mod_proxy 模組
RUN a2enmod proxy && a2enmod proxy_http

# Expose ports
EXPOSE 80

# Start Apache first, then backend
CMD service apache2 start && . /var/www/html/apache-test/backend/venv/bin/activate && python3 /var/www/html/apache-test/backend/app.py