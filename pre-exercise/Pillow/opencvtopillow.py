import cv2
from PIL import Image 
img = cv2.imread('images/img01.jpg') 
cv2.imshow("OpenCV",img)

# open cv -> pillow
image = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
image.show()
cv2.waitKey(0)
cv2.destroyAllWindows()