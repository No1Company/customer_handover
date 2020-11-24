import json
import os
import requests
import sys
from urllib.parse import quote

class NetworkError(Exception):
    pass

baseUrl = 'https://rest.ehrscape.com/rest/v1'
queryUrl = baseUrl + '/query'


try:
    loginfile = open(os.path.join("..","..",'login.txt'))
    authorization = loginfile.read().split('\n')[0]
except FileNotFoundError:
    args = sys.argv
    if "--ehrpassword" in args:
        authorization = str("Basic " + args[args.index("--ehrpassword")+1])
    else:
        print("EHR authorization not found in either args or file. Add file in login.txt or by running the program with arg '--ehrpassword <EHRPASSWORD>'")

print(authorization)
authorization_header = {'Authorization': authorization}


def print_error(status_code, source):
    print('Recieved status code: ' + str(status_code) + ' from ' + source)


def generate_fake_user():
    partyData = {}

    person_source = 'https://fejka.nu/?json=1'
    req = requests.get(person_source)
    if req.status_code < 300:
        person = req.json()
        fname = person['fname']
        lname = person['lname']
        pnr = person['pnr_full']
        dob = pnr[0:4] + '-' + pnr[4:6] + '-' + pnr[6:8]
        partyData['firstNames'] = fname
        partyData['lastNames'] = lname
        partyData['dateOfBirth'] = dob
    else:
        raise NetworkError("fejka.nu unavailable")

    req = requests.post(baseUrl + '/ehr', headers=authorization_header)
    if req.status_code < 300:
        partyData['partyAdditionalInfo'] = [
            {
                'key': 'ehrId',
                'value': req.json()['ehrId']
            }
        ]
    else:
        raise NetworkError("Could not post to ehrscape")

    req = requests.post(baseUrl + '/demographics/party',
                        json=partyData, headers=authorization_header)
    if req.status_code < 300:
        if req.json()['action'] == 'CREATE':
            req = requests.get(
                req.json()['meta']['href'], headers=authorization_header)
            return req.json()
        else:
            print('Wrong action')
    else:
        raise NetworkError("Could not post to ehrscape")

def get_user(ehr_id):
    req = requests.get("{}/demographics/ehr/{}/party".format(baseUrl, ehr_id), headers = authorization_header)
    if req.status_code < 300:
        return req.json()["party"]
    else:
        raise NetworkError("Could not get from ehrscape. json: " + str(req.json()))

def params(dict):
    return_string = ''
    for i in dict:
        return_string = return_string + str(i) + '=' + str(dict[i]) + '&'
    return quote(return_string[0:len(return_string)-1], safe='/:=&')


def add_blood_pressure(ehr_id, systolic, diastolic, time):
    composition_data = {
        'ctx/time': time.isoformat(),
        'ctx/language': 'en',
        'ctx/territory': 'CA',
        'self_monitoring/blood_pressure/any_event/systolic': systolic,
        'self_monitoring/blood_pressure/any_event/diastolic': diastolic,
        'self_monitoring/blood_pressure/any_event/comment': 'inga kommentarer',
        'self_monitoring/blood_pressure/any_event/position': 'at1000'
    }

    query_params = {
        'ehrId': ehr_id,
        'templateId': 'sm_blood-pressure',
        'format': 'FLAT',
        'commiter': 'Patient'
    }
    url = baseUrl +\
        '/composition?' + params(query_params)
    req = requests.post(url, headers=authorization_header,
                        json=composition_data)
    if req.status_code < 300:
        return req.json()
    else:
        raise NetworkError("Could not post to ehrscape")



def make_aql_query(aql):
    req = requests.get(baseUrl + '/query?' +
                       params({"aql": aql}), headers=authorization_header)
    return req


def get_blood_pressure(ehr_id, simplify = True):
    aql = "SELECT c/context as context, " +\
        "g/data[at0001]/events[at0006]/data[at0003]/items[at0004]/value as systolic, " +\
        "g/data[at0001]/events[at0006]/data[at0003]/items[at0005]/value as diastolic, " +\
        "g/data[at0001]/events[at0006]/data[at0003]/items[at0033]/value as comment, " +\
        "g/data[at0001]/events[at0006]/state[at0007]/items[at0008]/value as position " +\
        "FROM EHR[ehr_id/value = '{}'] ".format(ehr_id) +\
        "CONTAINS COMPOSITION c " +\
        "CONTAINS OBSERVATION g[openEHR-EHR-OBSERVATION.blood_pressure.v2] " +\
        "OFFSET 0 LIMIT 10"
    req = make_aql_query(aql)
    if req.status_code < 300:    
        print(req)
        req_result_set = req.json()["resultSet"]
        if simplify:
            return [
                {
                    'systolic': i['systolic']['magnitude'],
                    'diastolic': i['diastolic']['magnitude'],
                    'comment': i['comment']['value'],
                    'position': i['position']['value'],
                    'time': i['context']['start_time']['value']
                } 
                for i in req_result_set
            ]
        else:
            return req_result_set
    else:
        raise NetworkError("Could not get from ehrscape")

