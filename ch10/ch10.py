#!/usr/bin/env python
#
# Tuenti Challenge 6 - Challenge 10
# Taras Sotnikov

#KEY 1: in cat container.zip | grep -a -i key
#Extract the containing file. Change the extension of docx to zip and extract the containing files
#KEY 2: in tuenti/docProps/core.xml
#KEY 3: in tuenti/tuenti.mp3
#KEY 4: metadata png inside of mp3. 
#KEY 5: base64 decode to pdf file. Subject of pdf, convert hex to ascii
#KEY 6: pdfdetach -saveall key5.pdf. In the video
#KEY 7: mkvextract attachments "video.mkv" 1:key7.txt
#KEY 8: Decode uuencode, gunzip -c ramdisk.cpio.gz | cpio -i
#KEY 9: Use the passphrase from the file. gpg --output key9.txt --decrypt LastLevel.txt.gpg 

#from PIL import Image
#import base64

#image = Image.open("tuenti/tuenti.png")
#text4 = image.info['NextLevel']
#decoded = base64.b64decode(text4)
#with open('key5.pdf', 'w') as f:
#	f.write(decoded)


print "KEY1: d4Gs-AST-ZZKGtYqKmUiFLRIu-7A7HPE"
print "KEY2: D-MaB5gu39RG7qMXdS2FhEhKC-p8LqgB"
print "KEY3: KeBUIntUC7N53lRhs4AxHEHRa9tA08Hp"
print "KEY4: t6oLjeGMCv3r3BFpDfUUdH5i33KDvEB3"
print "KEY5: qekxJkR8mLzivzZJe5ptfTOXfABaAeYV"
print "KEY6: XrBV392qT0DqDSCGuGDStdY6_ADKkD_4"
print "KEY7: fY2iqYwyU4gp0uWD10U5wau5Dt8lNWaJ"
print "KEY8: xMT2MdOTOX5qgu_ZynsuLQFQ4VcRLqWY"
print "KEY9: QbAbxv1TIUkt4NZkK8-VUBU6CxjHFi3Q"