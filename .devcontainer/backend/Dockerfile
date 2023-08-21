# [Choice] Ubuntu version (use ubuntu-22.04 or ubuntu-18.04 on local arm64/Apple Silicon): ubuntu-22.04, ubuntu-20.04, ubuntu-18.04
ARG VARIANT=ubuntu-20.04
FROM mcr.microsoft.com/vscode/devcontainers/base:0-${VARIANT}

# [Optional] Uncomment this section to install additional OS packages.
RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends python3-pip pkg-config libmysqlclient-dev python3-dev

# Install Python packages from requirements.txt
COPY .devcontainer/backend/requirements.txt /tmp/
RUN pip3 install --no-cache-dir -r /tmp/requirements.txt

# Install Google Chrome
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list \
    && apt-get update -y \
    && apt-get install -y google-chrome-stable

# Install ChromeDriver
RUN wget https://chromedriver.storage.googleapis.com/VERSION_NUMBER/chromedriver_linux64.zip \
    && unzip chromedriver_linux64.zip -d /usr/bin \
    && chmod +x /usr/bin/chromedriver

COPY backend/ /app/

WORKDIR /app
CMD ["python3", "main.py"]
