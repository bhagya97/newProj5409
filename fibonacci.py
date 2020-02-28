input_file= open("fib_input.txt", "r")
input1= int(input_file.readline().strip())
first=0
second=1
output_file= open("fib_output.txt","w")
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
output_file.close()
input_file.close()
print("done")
