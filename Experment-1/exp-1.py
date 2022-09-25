class Check:# class
    def __init__(self,s): #constructor
        self.sen=s; #input string
        self.vowels={'a','e','i','o','u'}; #set of ovwels
        self.ch=[]; #list for storeing each and every char of input str

    def check(self): #logic
        self.sen=self.sen.lower() #making input into lower
        
        for ch in self.sen: 
            self.ch.append(ch) #storeing each and every char in ch list
            
        self.ch=set(self.ch) #converting ch list into set
        
        if len(self.ch & self.vowels)==len(self.vowels): #checking for condition 
            print("sentence contain all the vowels") 
            
        else: 
            print(" sentence don’t contain all the vowels ") 

obj=Check(input("enter a sentence:")) #creating obj for class Check
obj.check() #invoking the method
