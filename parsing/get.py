# Import required packages
import cv2
import pytesseract
import numpy as np
#import os
#import PIL
import re


# Mention the installed location of Tesseract-OCR in your system
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

# Read image from which text needs to be extracted
#img = cv2.imread("Gotovo\\img\\3_1.jpg")




# Preprocessing the image starts
def img_process(img):


	#percent by which the image is resized
	scale_percent = 150

	#calculate the 50 percent of original dimensions
	width = int(img.shape[1] * scale_percent / 100)
	height = int(img.shape[0] * scale_percent / 100)

	# dsize
	dsize = (width, height)

	# resize image
	img = cv2.resize(img, dsize)

	# Convert the image to gray scale
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


	hsllight  = cv2.cvtColor(img, cv2.COLOR_BGR2HLS)
	Lchannell = hsllight[:,:,1]
	lvaluel = cv2.mean(Lchannell)[0]

	# if lvaluel > 80:
	# 	gray = cv2.bitwise_not(gray)
	# Performing OTSU threshold
	ret, thresh2 = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
	thresh1 = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
	# cv2.imshow('?', thresh1)
	# cv2.imshow('1', thresh2)


	# Specify structure shape and kernel size.
	# Kernel size increases or decreases the area
	# of the rectangle to be detected.
	# A smaller value like (10, 10) will detect
	# each word instead of a sentence.
	rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

	# Applying dilation on the threshold image
	dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)
	img_erode = cv2.erode(thresh1, np.ones((3, 3), np.uint8), iterations=1)
	#img_erode = cv2.bitwise_not(img_erode)
	# Finding contours
	contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
													cv2.CHAIN_APPROX_NONE)

	contour2, hierarchy = cv2.findContours(img_erode, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	#print(contours, contour2)

	# Creating a copy of image
	im2 = img.copy()
	im22 = img.copy()

	# A text file is created and flushed
	file = open("recognized.txt", "w+")
	file.write("")
	file.close()

	i = 0
	output = img.copy()
	imgtext = []
	imgtext2 = []
	# Looping through the identified contours
	# Then rectangular part is cropped and passed on
	# to pytesseract for extracting text from it
	# Extracted text is then written into the text file
	# for cnt in contours:
	# 	x, y, w, h = cv2.boundingRect(cnt)
		
	# 	# Drawing a rectangle on copied image
	# 	rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
		
	# 	# Cropping the text block for giving input to OCR
	# 	cropped = gray[y:y + h, x:x + w]
		
	# 	# Open the file in append mode
	# 	#file = open("recognized.txt", "a")
		
	# 	# Apply OCR on the cropped image
	# 	text = pytesseract.image_to_string(cropped, lang="rus")
		
	# 	# Appending the text into file
	# 	if text:
	# 		imgtext.append(str.lower(text))
	# 		#print(text, i)
	# 		i = i + 1
	# 		#file.write(text)
	# 		#file.write("\n")

	# 	# Close the file
	custom_cnt = contours[0]
	i = 0
	for contour in contour2:
		if contour[0][0][1] == custom_cnt[0][0][1]:
			custom_cnt = np.concatenate((custom_cnt, contour))
		else:
			x, y, w, h = cv2.boundingRect(custom_cnt)
			custom_cnt = contour
			# Drawing a rectangle on copied image
			rect = cv2.rectangle(im22, (x, y), (x + w, y + h), (0, 255, 0), 2)
			
			# Cropping the text block for giving input to OCR
			cropped = gray[y:y + h, x:x + w]
			
			# Open the file in append mode
			#file = open("recognized.txt", "a")

			# Apply OCR on the cropped image
			text = pytesseract.image_to_string(cropped, lang="rus")
			
			
			# Appending the text into file
			if text:
				imgtext2.append(str.lower(text))
				#print(text, i)
				i = i + 1
				#file.write(text)
				#file.write("\n")

	#file.close
	imgtext = imgtext + imgtext2
	imgtext2 = []
	for text in imgtext:
		mystr = re.sub(r"[^а-яА-Я0-9]+", ' ', text)
		#mystr = ''.join(e for e in text if e.isalnum() or e == ' ')
		imgtext2.append(mystr)
	print(imgtext2)
	return max(imgtext2, key=len)

	for contour in contours:
		(x, y, w, h) = cv2.boundingRect(contour)

		# print("R", idx, x, y, w, h, cv2.contourArea(contour), hierarchy[0][idx])
		# hierarchy[i][0]: the index of the next contour of the same level
		# hierarchy[i][1]: the index of the previous contour of the same level
		# hierarchy[i][2]: the index of the first child
		# hierarchy[i][3]: the index of the parent
		# print((x, y, w, h))
		cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 1)


	# cv2.imshow('1', img_erode)
	# cv2.imshow('22', img)
	# cv2.imshow('2', dilation)
	# #cv2.imshow('3', img_erode)
	# cv2.waitKey(0)



path1 = 'Gotovo\\img\\12.jpg'
path2 = 'Gotovo\\img\\32.jpg'
print(img_process(cv2.imread(path1, cv2.IMREAD_UNCHANGED)))
print(img_process(cv2.imread(path2, cv2.IMREAD_UNCHANGED)))

#вот короче два файла, которые возвращают "мертвые души о " и "виктор пелевин чапаев и пустота"
#кто-то там доделайте под бота хд))0)
#правда по времени работы них не оптимальненько