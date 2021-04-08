
i=0;k_10=[];halfmaraton=[];maraton=[];ultra=[]
#runner_list=list(map(lambda x : x.strip(),input().split(',')))
runners_list=input('Enter your name: ').split(',')
teams_list=input('Enter your team :').split('*')
print("hello")
def strip(x):
    x=[i.strip() for i in x]
    return x

# delete spaces from each names:
runners_list=strip(runners_list)    
    
# delete extara names and sort them
runners_list=set(runners_list)
runners_list=list(runners_list)
runners_list.sort()

# print names with their numbers
print('Name of runners:')
for i in range(len(runners_list)):
    print(i ,runners_list[i])
    
# receiving informations of each runner and saveing in a dictionary
for i in range(len(runners_list)):
    info=dict()
    info['name']=runners_list[i]
    info['distance']=float(input('\n%s Enter your distance:'%runners_list[i]))
    info['duration']=int(input('%s Enter your Duration :'%runners_list[i]))
    info['speed']=round(float(info['distance']/(info['duration']/60)),4)
    info['pace']=round(float(info['duration']/info['distance']),4)
    runners_list[i]=info  
    
def sorting(lst,metric):#lst is a list of dictionaries
    lst=sorted(lst,key=lambda i:i[metric],reverse=True)
    return lst

# sort runners base on speed
#print('sorted runners_list based on speed:',sorting(runners_list,'speed'))

def find_fastest(lst):#lst is a list of dictionaries
    return sorting(lst,'speed')[0]


print('\nFastest runner:\n',find_fastest(runners_list))
print('runner with most_distance:\n',max(runners_list,key=lambda i:i['distance']))

# classify finishers
for name in runners_list:
    if name['distance']<10:pass
    elif 10<=name['distance']<21.09775:
        k_10.append(name)
    elif 21.09775<=name['distance']<42.195:
        halfmaraton.append(name)
    elif 42.195<=name['distance']<60:
        maraton.append(name)
    else:ultra.append(name)

#print 3 fastest of each group
print('\nThe 3 fastest of 10k:')
[print(k_10[i]) for i in range(min(3,len(k_10)))]
print ('\nThe 3 fastest of Half_maraton:')
[print(halfmaraton[i]) for i in range(min(3,len(halfmaraton)))]
print ('\nThe 3 fastest of maraton:')
[print(maraton[i]) for i in range(min(3,len(maraton)))]
print ('\nThe 3 fastest of Ultra:')
[print(ultra[i]) for i in range(min(3,len(ultra)))]

    
# make teams with their informations
for i in range(len(teams_list)):
    team_members=teams_list[i].split(',')
    team_members=[i.strip() for i in team_members]
    team=dict()
    team['name']=teams_list[i]
    sum_speed=0
    total_distance=0
    for j in range(len(team_members)):
        info=next(item for item in runners_list if item["name"]==team_members[j])
        sum_speed=info['speed']+sum_speed
        total_distance=info['distance']+total_distance
        team_members[j]=info
    team['average_speed']=sum_speed/len(team_members)
    team['total_distance']=total_distance
    max_team=find_fastest(team_members)
    team['leader']=max_team['name']
    teams_list[i]=team
    
#sort teams by total distance
teams_list=sorting(teams_list,'total_distance')
print('\nAnnounce top 3 teams base on total distance:')
[print(teams_list[i]) for i in range(min(3,len(teams_list)))]



