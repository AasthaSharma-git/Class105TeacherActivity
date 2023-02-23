import cv2

# vid=cv2.VideoCapture(0)
vid=cv2.VideoCapture('AnthonyShkraba.mp4')

width=int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height=int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

writer=cv2.VideoWriter('ModifiedVideo.avi',cv2.VideoWriter_fourcc(*'xvid'),10,(width,height))

if vid.isOpened()==False:
    print('Cannot open camera....')
else:
    while True:
        ret,frame=vid.read()
        writer.write(frame)
        cv2.imshow('MyVideo',frame)
        if cv2.waitKey(50)==32:
            break

vid.release()
        