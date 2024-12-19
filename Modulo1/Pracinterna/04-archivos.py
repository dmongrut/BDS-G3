file = open("alumnos.txt","w")
file.write("100, cesar,cesar@gmail.com")
file.close()

""" file = open("alumnos.txt","w")
file.write("200, cesar,cesar@gmail.com")
file.close() """

file = open("alumnos.txt","a")
file.write("\n")
file.write("200, cesar,cesar@gmail.com")
file.close()


file_read = open("alumnos.txt","r")
alumnos = file_read.read()
print(alumnos)
print("******")
print(type(alumnos))
file.close()

