import sys
from Controllers.PreCondition import *
from Controllers.TestExecution import *
from Controllers.TestPlan import *
from Controllers.TestSet import *
from Controllers.Test import *
from Files.Constants import *
import Utilities.log as log
# addStepToTest('test7', 'PREPROD', 'kushal.aggarwal@capgemini.com', 'kusaggar')
# addTestToTestSet("test3", "PREPROD", "kushal.aggarwal@capgemini.com", "kusaggar")
# addTestToTestPlan("TS_T", "PREPROD", "kushal.aggarwal@capgemini.com", "kusaggar")
# addTestToTestExecution("TE_T", "PREPROD", "kushal.aggarwal@capgemini.com", "kusaggar")
# addTestToPrecondition("test2", "PREPROD", "kushal.aggarwal@capgemini.com", "kusaggar")
# logger = log.setup_custom_logger('root')
# logger.debug('sdvjjhvdjsvdh')
filename = sys.argv[1]
destination = sys.argv[2].upper()
issueType = sys.argv[3].upper()
issueTypeToBeAdded = sys.argv[4].upper()
userName = sys.argv[5]
password = sys.argv[6]

temp = get(f'{c.constants[destination]}rest/raven/1.0/api/settings/teststepstatuses', userName, password)
# temp = get(f'{c.constants["PREPROD"]}rest/raven/1.0/api/settings/teststepstatuses', "kushal.aggarwl@capgemini.com", "kusagga")
if temp == 401:
    print('please enter valid credentials')
    exit()
elif temp == 403 or temp == 500:
    print("Something went wrong")
    exit()
if issueType == "TEST":
    if issueTypeToBeAdded == "STEP":
        addStepToTest(filename, destination, userName, password)

if issueType == "PRECONDITION":
    if issueTypeToBeAdded == "TEST":
        addTestToPrecondition(filename, destination, userName, password)

if issueType == "TESTEXECUTION":
    if issueTypeToBeAdded == "TEST":
        addTestToTestExecution(filename, destination, userName, password)

if issueType == "TESTPLAN":
    if issueTypeToBeAdded == "TEST":
        addTestToTestPlan(filename, destination, userName, password)

if issueType == "TESTSET":
    if issueTypeToBeAdded == "TEST":
        addTestToTestSet(filename, destination, userName, password)

# readFile('test6')
# preCondition('test2','JIRA_PRE_PROD')
# testSet('test3','JIRA_PRE_PROD')
# testExecution('test4','JIRA_PRE_PROD')
# testPlan('test5','JIRA_PRE_PROD')
# addStepToTest('test7')
