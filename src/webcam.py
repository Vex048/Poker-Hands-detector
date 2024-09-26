from ultralytics import YOLO
import cv2
import cvzone
import math
from handChecker import handChecker
from pokerHands import Hands
import json
cap = cv2.VideoCapture(0) #Kamera
cap.set(3,1280)
cap.set(4,720)
#cap= cv2.VideoCapture("../Videos/ppe-1-1.mp4") # Dla video



model = YOLO("../Model_parameters/playingCards.pt")
f=open('../classNames/classPoker.json')
classNames = json.load(f)


myColor = (0,0,255)

handCheck=handChecker()
hands = Hands()

numberOfPlayers = 4
currentTurn = 1
printScores=False

while True:
    success,img = cap.read()
    results=model(img,stream=True)
    cv2.putText(img, f'Ilosc graczy: {numberOfPlayers}', (700, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_4)
    if currentTurn ==0:
        cv2.putText(img, f'Tura Krupiera', (700, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_4)
    else:
        cv2.putText(img, f'Tura gracza numer: {currentTurn}', (700, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_4)
    for r in results:
        boxes = r.boxes
        for box in boxes:

            #Bouding Box
            x1,y1,x2,y2=box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1),int(x2),int(y2)
            #cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            w,h = x2-x1,y2-y1

            #Confidence
            conf=math.ceil((box.conf[0]*100))/100

            #Class Name
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if conf > 0.94:
                print("1 ",currentTurn)
                hands.addCard(str(currentClass), currentTurn,numberOfPlayers)

            if len(hands.getHand(currentTurn)) == 2:
                print("2 ",currentTurn)
                print(hands.getHand(currentTurn))
                currentTurn = hands.nextTurn(currentTurn, numberOfPlayers)
                print("3 ",currentTurn)
            elif len(hands.getHand(currentTurn)) >=3 and len(hands.getHand(currentTurn)) <=5:
                #print(hands.getHand(currentTurn))
                possibleHands1 = hands.createHand(1)
                possibleHands2 = hands.createHand(2)
                possibleHands3 = hands.createHand(3)
                possibleHands4 = hands.createHand(4)
                hand1,cards1,score1 = handCheck.iterareThroughListOfHands(possibleHands1)
                hand2,cards2,score2 = handCheck.iterareThroughListOfHands(possibleHands2)
                hand3,cards3,score3 = handCheck.iterareThroughListOfHands(possibleHands3)
                hand4,cards4,score4 = handCheck.iterareThroughListOfHands(possibleHands4)
                printScores=True
                #handCheck.checkForHand()
                #hand = handCheck.returnHand()
                #cv2.putText(img,hand,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2,cv2.LINE_4)



            cvzone.cornerRect(img,(x1,y1,w,h))
            cv2.rectangle(img,(x1,y1),(x2,y2),myColor,3)
            cvzone.putTextRect(img, f"{classNames[cls]} {conf}", (max(0, x1), max(35, y1)),scale=1,thickness=1,colorB=myColor,colorT=(255,255,255),colorR=myColor)
    if printScores:
        scores = [score1,score2,score3,score4]
        playerHands = [hand1,hand2,hand3,hand4]
        winningIndexes = handCheck.checkForSameHand(scores)
        #winningHands = handCheck.getHandsToCompare(playerHands,handsIndexes)
        cv2.putText(img, f'Player 1: {hand1} ', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_4)
        cv2.putText(img, f'Player 2: {hand2} ', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_4)
        cv2.putText(img, f'Player 3: {hand3} ', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_4)
        cv2.putText(img, f'Player 4: {hand4} ', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_4)
        cv2.putText(img, f'Player who won: ', (50, 300), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (0, 255, 255), 2,
                    cv2.LINE_4)
        print("Scores: ",scores)
        print("Winning indexes: ",winningIndexes)
        move = 0
        for i in winningIndexes:
            cv2.putText(img, str(i+1), (400 + move, 300), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2,
                    cv2.LINE_4)
            move +=50

    cv2.imshow("Image", img)
    cv2.waitKey(1)