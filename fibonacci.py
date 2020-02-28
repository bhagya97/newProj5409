import time
import logging
import random

fibonacci()
def fibonacci():
    logging.basicConfig(filename="logfile.log",level=logging.DEBUG)
    starting_time=time.time()

    ### generate random numbers each time
    input1= random.randint(0,100)

    ### taking input from file
    #input_file= open("fib_input.txt", "r")
    #input1= int(input_file.readline().strip())

    first=0
    second=1

    ### open the output file
    output_file= open("fib_output.txt","a")

    output_file.write("Input:")
    output_file.write(str(input1))
    output_file.write("\n")
    output_file.write("Output")
    output_file.write(str(first))
    output_file.write("\n")
    output_file.write(str(second))
    output_file.write("\n")

    for i in range(0,input1-2):
        element=first+second
        first=second
        second=element
        output_file.write(str(element))
        output_file.write("\n")

    ### close the files
    output_file.close()
    #input_file.close()

    ending_time=time.time()

    ###calculate the time taken
    time_taken= ending_time-starting_time
    logging.debug("fibonacci: %2.18f for Input: %d",time_taken,input1)
    print("fibo timetaken",time_taken)





