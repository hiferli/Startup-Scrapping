import startupURLs
import pageReader

for link in startupURLs.getStartups():
    pageReader.SlideCapture(link);