FROM python:3.11-alpine3.16

WORKDIR /workspace

# Expose port you want your app on
EXPOSE 8070

RUN apt-get update
RUN apt-get install libgl1-mesa-glx -y

# Upgrade pip and install requirements
COPY requirements.txt requirements.txt
RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . .

#ENV AWS_ACCESS_KEY_ID=
#ENV AWS_SECRET_ACCESS_KEY=
# ENV AWS_DEFAULT_REGION="ap-northeast-2"

ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=8070", "--server.address=0.0.0.0"]