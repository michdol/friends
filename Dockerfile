FROM python:3.8
ENV DockerHOME=/home/friends/

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHOME
RUN pip install -r ./friends/requirements.txt

EXPOSE 8000

ENTRYPOINT ["tail", "-f", "/dev/null"]