FROM python:3.9
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN apt-get install libxcb-xinerama0  -y

COPY Challenges/EPIC_IO_challenge/requirements.txt /requirements.txt
RUN pip3 install -r /requirements.txt
COPY Challenges/EPIC_IO_challenge/tracker_object.py /tracker_object.py
COPY Challenges/EPIC_IO_challenge/input.mkv  /input.mkv
COPY Challenges/EPIC_IO_challenge/initial_conditions.json  /initial_conditions.json
WORKDIR /

CMD python3 tracker_object.py

