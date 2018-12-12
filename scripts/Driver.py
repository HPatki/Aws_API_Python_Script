from classes import IAM

iam = IAM.IAM()
policies = iam.listPolicies()
allPolicies = policies['Policies']
for indvPolicy in allPolicies:
    print (indvPolicy)
