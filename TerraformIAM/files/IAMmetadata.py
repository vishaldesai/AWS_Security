import boto3
import json

client = boto3.client('iam')

iamuserresponse = client.list_users(MaxItems=1000)

# Get username and Group
print ('#####User belongs to Group############')
print ('Username:Group')
print ('######################################')
for key,value in iamuserresponse.items():
    if key == 'Users':
        for i in range(len(value)):
            ## Get Group for given user
            groupresponse = client.list_groups_for_user(UserName=value[i]['UserName'],  MaxItems=100)
            for key1, value1 in groupresponse.items():
                    if key1 == 'Groups':
                        for j in range(len(value1)):
                            #print("['" + value[i]['UserName'] + ' belongs-to ' + value1[j]['GroupName'] + "'],")
                            print( value[i]['UserName'] + ':' + value1[j]['GroupName'])


#Get Group name and inline Policy

print ('#####Inline policy attached to Group#########################')
print ('Group:InlinePolicy')
print ('#############################################################')
groupresponse = client.list_groups(MaxItems=1000)
for  key,value in groupresponse.items():
    if key == 'Groups':
            for i in range(len(value)):
                ## Get Group inline group policy
                inlinegrppolicyresponse = client.list_group_policies(GroupName=value[i]['GroupName'], MaxItems=100)
                for key1, value1 in inlinegrppolicyresponse.items():
                    if key1 == 'PolicyNames':
                        for j in range(len(value1)):
                            #print ("['" +  value[i]['GroupName'] + ' has-policy ' + value1[j]  + "'],")
                            print (value[i]['GroupName'] + ':' + value1[j])


#Get Group name and managed policy
print ('#####Managed policy attached to Group#########################')
print ('Group:ManagedPolicy')
print ('#############################################################')
groupresponse = client.list_groups(MaxItems=1000)
for  key,value in groupresponse.items():
    if key == 'Groups':
            for i in range(len(value)):
                ## Get Group inline group policy
                paginator = client.get_paginator('list_attached_group_policies')
                response_iterator = paginator.paginate(GroupName=value[i]['GroupName'])
                for response in response_iterator:
                    #print(response['AttachedPolicies'].items())
                    for key1, value1 in response.items():
                        if key1 == 'AttachedPolicies':
                            for j in range(len(value1)):
                                #print("['" + value[i]['GroupName']  + ' has-policy ' + value1[j]['PolicyName']  + "'],")
                                print(value[i]['GroupName']  + ':' + value1[j]['PolicyName'])
