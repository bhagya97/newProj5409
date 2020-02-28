import time
import logging
import random

factorial()
def factorial():
    logging.basicConfig(filename="logfile.log",level=logging.DEBUG)
    starting_time=time.time()

    ### generate random numbers each time
    input1= random.randint(0,100)

    ### input from the file
    #input_file=open("fact_input.txt", "r")
    #input1= int(input_file.readline().strip())
    n=1
    output_file=open("fact_output.txt","a")
    
    ### 0!=1- Basecase
    if input1==0:
        output_file.write("Input: 0")
        output_file.write("\n")
        output_file.write("Output: 1")
        output_file.write("\n")
       
    else:
        for i in range(1,input1+1):
            n=i*n
        
        output_file.write("Input:")
        output_file.write(str(input1))
        output_file.write("\n")
        output_file.write("Output:")
        output_file.write(str(n))
        output_file.write("\n")

    ### close the files
    #input_file.close()
    output_file.close()

    ending_time=time.time()

    ###calculate the time taken
    time_taken= ending_time-starting_time
    logging.debug("factorial: %2.18f for Input: %d",time_taken,input1)
    print("fact timetaken",time_taken)

