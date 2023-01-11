FROM python:3.8
ENV DockerHOME=/home/friends/

RUN mkdir -p $DockerHOME

WORKDIR $DockerHOME

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY . $DockerHOME

# TODO: don't do it like that, figure it out
RUN chmod -R 777 $DockerHOME

RUN pip install -r ./friends/requirements.txt

EXPOSE 8000

ENTRYPOINT ["tail", "-f", "/dev/null"]