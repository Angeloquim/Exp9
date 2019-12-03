import pandas as pd
data1 = {'Student':['Ice Bear','Panda','Grizzly'],
        'Math':[80,95,79]}
grades1=pd.DataFrame(data1,columns=['Student','Math'])
data2 = {'Student':['Ice Bear','Panda','Grizzly'],
        'Electronics':[85,81,83]}
grades2=pd.DataFrame(data2,columns=['Student','Electronics'])
data3 = {'Student':['Ice Bear','Panda','Grizzly'],
        'GEAS':[90,79,93]}
grades3=pd.DataFrame(data3,columns=['Student','GEAS'])
data4 = {'Student':['Ice Bear','Panda','Grizzly'],
        'ESAT':[93,89,88]}
grades4=pd.DataFrame(data4,columns=['Student','ESAT'])

merge=pd.merge (grades1,grades2,how='right',on='Student')
merge1=pd.merge (merge,grades3,how='right',on='Student')
mergefinal=pd.merge (merge1,grades4,how='right',on='Student')
mergelong=pd.melt(mergefinal,id_vars = 'Student', 
                  var_name = 'Subject', 
                  value_name='Grades')
