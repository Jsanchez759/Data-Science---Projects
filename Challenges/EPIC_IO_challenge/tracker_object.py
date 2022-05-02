import cv2
import pandas as pd
import logging

logging.basicConfig(level=logging.DEBUG,
                    format= "{asctime} {levelname:<8} {message}",
                    style="{")  # To show all the messages (including logging.info) and format with time mark

initial_positions = pd.read_json('initial_conditions.json')
video = cv2.VideoCapture('input.mkv')  # Object that open the video
logging.info("The input features (video and initial positions) imported properly")

success, frame = video.read()  # Read de input video
multi_tracker = cv2.legacy.MultiTracker_create()
boxes = []
for players, id in zip(initial_positions['coordinates'], initial_positions['id']):
    bbox = tuple(players)
    boxes.append(bbox)
    multi_tracker.add(cv2.legacy.TrackerMOSSE_create(), frame, bbox)  # Initialize tracker with first frame for each id
    logging.info(f'The tracker for the {id} player was created correctly')


def drawBox(img, bbox, id):
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(img, (x,y), ((x+w), (y+h)), (255,0,0))
    cv2.putText(img,
                'Tracking the Id '+ str(id)+' player',
                (x, y),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2)


while True:
    success, frame = video.read()

    if success is False:  # To check any problem with video
        break

    timer = cv2.getTickCount() # Start timer

    ok, bbox = multi_tracker.update(frame)  # Update the tracker with each new frame of the video

    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)  # Frames per second

    for i, j in zip(bbox, initial_positions['id']):
        if ok:  # Tracking success
            logging.info(f'The tracker for {j} in the new frame is ok and the new position is x={int(i[0])} and '
                         f'y={int(i[1])}')
            drawBox(frame, i, j)  # Draw the Bounding Box
        else:
            cv2.putText(frame,
                        "Tracking failure detected",
                        (int(i[0]), int(i[1])),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255),
                        2)
            logging.warning('There is a problem with the tracking strategy')


    cv2.putText(frame, "FPS : " + str(int(fps)),
                (70, 700),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2)

    cv2.imshow('Tracking window', frame)  # Show the video

    if cv2.waitKey(1) & 0xff == ord('q'):  # If we press q and wait one second, quit the program and camera
        break