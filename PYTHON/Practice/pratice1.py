Team_Members = [
    {
             'Name':'Dhanaveera',
             'Branch':'B.tech',
             'score':{'python':90, 'js':78 ,'MangoDB':66}
    },
    {
             'name':'Raju',
             'Branch':'B.com',
             'score':{'python':89, 'js':56 ,'MangoDB':90}
    },
    {          
             'name':'Malcha',
             'Branch':'B.Tech',
             'score':{'python':78, 'js':64 ,'MangoDB':66}
        
    },
    {        'name':'Nabi',
             'Branch':'Inter',
             'Score':{'python':70, 'js':93 ,'MangoDB':59}
        
    },
    {       
             'name':'vijaya',
             'Branch':'B.Tech',
             'Score':{'python':52, 'js':48 ,'MangoDB':86}
        
    },
    {           
              'name':'Sathish',
              'Branch':'B.ed',
              'Score': {'python':35, 'js':68 ,'MangoDB':56}
        
    },
    {         'name':'Durga',
               'Branch':'B.Tech',
               'Score':{'python':79, 'js':48 ,'MangoDB':49}
               
    },
    {          'name':'Bhargav',
                'Branch':'B.Tech',
                'Score':{'python':44, 'js':69 ,'MangoDB':80}
               
    },
    {           'name':'Siri',
                'Branch':'B.Tech',
                'Score':{'python':80, 'js':45 ,'MangoDB':79}
          
    },
    {
                 'name':'prabha',
                 'Branch':'B.Tech',
                 'Score':{'python':45, 'js':76 ,'MangoDB':56}
    }
]
 
num_TeamMembers = 10


Score={}

for member in Score.items:
       if  'Score' in member and 'Team_Members' in member['Score']:
            python_score = member['Score']['python']
            js_score = member['Score']['js']
            MangoDB_score = member['Score']['MangoDB']
            student_name = member['name']
            

    
if member ['Score']['maths']>10:
    print(sum(python_score,js_score,MangoDB_score))
    
    
  
          


    
    
    
    
    
    
    
    
  


   