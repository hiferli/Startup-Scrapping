import startupURLs
import pageReader
import Constants

for link in startupURLs.GetStartups():
    pageReader.SlideCapture(link);

print(f'All Slide Capture successful. Total Execution time is {round(Constants.totalTime , 3)} seconds ({Constants.timeConvert(round(Constants.totalTime , 3))})')