import cv2
import imutils

image = cv2.imread("SanyikaVerda.jpg")
cv2.imshow("Nyerfoto", image)
cv2.waitKey(0)
image = cv2.resize(image, (800,600) )
cv2.imshow("Ujrameretezettkep", image)
cv2.waitKey(0)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Szurkeskep", gray)
cv2.waitKey(0)
gray2 = cv2.bilateralFilter(gray, 50, 50, 50,50)
cv2.imshow("Billater ", gray2)
cv2.waitKey(0)
#gray2 = cv2.erode(gray2, None, iterations=1)
#vcv2.imshow("Erozioskep", gray2)
#cv2.waitKey(0)
#gray2 = cv2.dilate(gray2, None, iterations=1)
#cv2.imshow("Rakoskep", gray2)
#cv2.waitKey(0)
# Alkalmazzuk a Canny éldetektort a képen
ratio = gray2.shape[0] / 500.0
gray = cv2.GaussianBlur(gray2, (5, 5), 0)
cv2.imshow("Blurozottkep", gray)
cv2.waitKey(0)
edged = cv2.Canny(gray, 75, 200)
cv2.imshow("Élek", edged)
cv2.waitKey(0)

contours=cv2.findContours(edged.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
contours = imutils.grab_contours(contours)
contours = sorted(contours,key=cv2.contourArea, reverse = True)[:10]

#for c in contours:
#    cv2.drawContours(image, [c], -1, (0, 255, 0), 2)

# cv2.imshow("Konturozas", image)
# cv2.waitKey(0)

closest_approx = None
list_of_contours = []

for c in contours:

    x, y, w, h = cv2.boundingRect(c)
    LEDGE = gray[y:y + h, x:x + w]
    LEDGE2 = cv2.Canny(LEDGE, 75, 200)
    CNumber, _ = cv2.findContours(LEDGE2, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    num_contours = len(CNumber)
    print("Az adott él kontur szama ", num_contours)
    approx = cv2.approxPolyDP(c, 0.02 * cv2.arcLength(c, True), True)
    if len(approx) != 4:
        continue
    if  ( 13 < num_contours < 30 ) :
        closest_approx = approx

# Kirajzoljuk a legközelebbi négyszöget
closest = cv2.drawContours(image, [closest_approx], -1, (255, 0, 0), 2)

cv2.imshow("Megtalalt rendszamtabla", image)
cv2.waitKey(0)

