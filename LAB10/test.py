# reading from prepoinsuline-seq.txt file, & counting how many characters
preproinsulin = open('/Users/xavier/Desktop/hello_pyton/LAB10/preproinsulin-seq.txt', 'r')
content = preproinsulin.read()
print(content)
print("prepoinsuline has: ", len(content.lower()), "characters")
preproinsulin.close()


# opening lsinsulin-seq-clean.txt file, in overwriting mode
linsulin = open("/Users/xavier/Desktop/hello_pyton/LAB10/lsinsulin-seq-clean.txt", "w")
linsulin.write(content[0:24]) # slicing the content of preproinsulin-seq.txt & overwriting in the lsinsulin-seq-clean.txt file
print("linsuline has: ", len(content[0:24]), "characters") # printing number of characters
linsulin.close()

# doing the same on the binsulin-seq-clean.txt file (slicing characters and overwriting file)
binsulin = open("/Users/xavier/Desktop/hello_pyton/LAB10/binsulin-seq-clean.txt", "w")
binsulin.write(content[24:54])
print("binsuline has: ", len(content[24:54]), "characters")
binsulin.close()    

# doing the same on the cinsulin-seq-clean.txt file (slicing characters and overwriting file)
cinsulin = open("/Users/xavier/Desktop/hello_pyton/LAB10/cinsulin-seq-clean.txt", "w")
cinsulin.write(content[54:89])
print("cinsuline has: ", len(content[54:89]), "characters")
cinsulin.close() 

# doing the same on the ainsulin-seq-clean.txt file (slicing characters and overwriting file)
ainsulin = open("/Users/xavier/Desktop/hello_pyton/LAB10/ainsulin-seq-clean.txt", "w")
ainsulin.write(content[89:110])
print("ainsuline has: ", len(content[89:110]), "characters")
ainsulin.close() 

# function to slice characters from global variable 'content', passing the filename and path of the destination file, & the character numbers where to slice
def slice_and_write(file_name, path, slice_start, slice_end):
    format_file = ".txt"
    complete_path = path + file_name + format_file
    filename = open(complete_path, "w")
    filename.write(content[slice_start:slice_end])
    print(f'{file_name} has: {len(content[slice_start:slice_end])}, characters')
    filename.close()

slice_and_write("test-seq-clean", "/Users/xavier/Desktop/hello_pyton/LAB10/", 89, 110)