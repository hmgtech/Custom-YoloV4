import os 
  
# Function to rename multiple files 
def main(): 
  
    for count, filename in enumerate(os.listdir("Dataset")): 
        dst ="cococola" + str(count) + ".jpg"
        src ='Dataset/'+ filename 
        dst ='Dataset/'+ dst 
          
        # rename() function will 
        # rename all the files 
        os.rename(src, dst) 
  
# Driver Code 
if __name__ == '__main__':
	main()
      
