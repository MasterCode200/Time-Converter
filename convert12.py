
tome = input(
  "Kindly enter the time you want to convert in the following format -> 00:00:00   "
)


def conversion(tome):

  f = int(tome[0:2])
  min = tome[3:5]
  sec = tome[6:8]

  finalanswer = ""
  if f > 12:
    p
    ap = "PM"
    support = str(int(f) - 12)
    if(int(support)<10):
      support="0"+str(support)
  elif f < 12:
    ap = "AM"
    if(f==0):
      
      f = 12
      support = str(12)
    else:
      support = str((f))
  else:
    ap="PM"
    support=str(12)
  return (support + ':' + min + ':' + sec + " " + ap)
    
x = conversion(tome)
print(x)    


    


