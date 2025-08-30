f = None
try :
    f = open('ghost.java', 'tr')
    print(f.read())

except FileNotFoundError as e :
    print(f"file not found {e}")

except FileExistsError as e :
    print(f' file does not exist{e}')    

finally :
    print("it will excute neverthless")
    if f:
        f.close()
