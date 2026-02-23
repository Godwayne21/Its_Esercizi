import cv2
from ultralytics import YOLO
# 1. Carichiamo il modello YOLOv8 Nano (il più veloce su CPU)
model = YOLO('yolov8n.pt')
# 2. Apriamo il file video (o la webcam mettendo 0)
video_path = "video.mp4" # Sostituisci con il tuo file
cap = cv2.VideoCapture(video_path)
print("Analisi in corso... Premi 'q' per uscire.")
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    # 3. Eseguiamo il rilevamento solo sulle PERSONE (classe 0 in YOLO)
    # device='cpu' forza l'uso del processore
    results = model.predict(frame, classes=[0], conf=0.4, device='cpu', verbose=False)
    # 4. Conteggio delle persone rilevate
    person_count = len(results[0].boxes)
    # 5. Visualizzazione dei risultati sul frame
    annotated_frame = results[0].plot() # Disegna i rettangoli attorno alle persone
    # Logica di allarme: se superiore a 5 persone
    color = (0, 0, 255) if person_count > 5 else (0, 255, 0)
    label = f"PERSONE: {person_count} - ALLARME ASSEMBRAMENTO!" if person_count > 5 else f"PERSONE: {person_count}"
    cv2.putText(annotated_frame, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX,  
                1, color, 3, cv2.LINE_AA)
    # 6. Mostra il video
    cv2.imshow("Monitoraggio Assembramenti", annotated_frame)
    # Esci premendo 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()