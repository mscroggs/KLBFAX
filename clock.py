temp="""             XXXXXXXXXXXXX             
           XXXXXXXXXXXXXXXXX           
         XXXXX           XXXXX         
       XXXX        X        XXXX       
      XXXX        XXX        XXXX      
     XXX           X           XXX     
    XXX                         XXX    
   XXX                           XXX   
   XX                             XX   
  XXX                             XXX  
  XX                               XX  
 XX                                 XX 
 XX                                 XX 
XXX                                 XXX
XX                                   XX
XX                                   XX
XX                                   XX
XX                                   XX
XX  X                             X  XX
XX XXX                           XXX XX
XX  X                             X  XX
XX                                   XX
XX                                   XX
XX                                   XX
XX                                   XX
XXX                                 XXX
 XX                                 XX 
 XX                                 XX 
  XX                               XX  
  XX                              XXX  
   XX                             XX   
   XXX                           XXX   
    XXX                         XXX    
     XXX           X           XXX     
      XXXX        XXX        XXXX      
       XXXX        X        XXXX       
         XXXXX           XXXXX         
           XXXXXXXXXXXXXXXXX           
             XXXXXXXXXXXXX             """.split("\n")

def map(j):
    if j=="X":
        return True
    return False

clock = [[map(j) for j in i] for i in temp]

