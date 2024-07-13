FROM python

# WORKDIR /workspace
# 
# RUN apt update \
#     &&  DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
#     wkhtmltopdf

WORKDIR /code

ENV SKLEARN_ALLOW_DEPRECATED_SKLEARN_PACKAGE_INSTALL True

COPY bin .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

# CMD "python3 app.py"
