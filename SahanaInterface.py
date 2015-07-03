__author__ = 'Hamza'

import getopt
import sys
import requests
from requests.auth import HTTPBasicAuth

# main function
def main(argv):
    r = ''
    username = 'hamzahussaini2@hotmail.com'
    password = 'pakistan'
    bundle = argv
    #bundle = bundle[:(len(bundle)-3)]
    print "this is bundle at PYTHON"
    print bundle
    print repr(bundle)
    bundle = bundle.split('%')
    print repr(bundle)
    bundle = bundle[0]
    print repr(bundle)
    host = "http://127.0.0.1:8000"
    #bundle = 'create_dvrcase|5355|Asad Kazmi|12-12-2009|male|030302020|htahir111@gmail.com|Qatar|Street 1|202000|High|Yes|Closed|My comments'
    #bundle = 'create_incident|Incident Type 1|Incident1|false|20|Qatar|Street 1|2020|My comments'
    #bundle = 'create_event|5355|Event2|Major Earthquake|false|12-12-2009|12-12-2015|My comments'
    bundle = bundle.split('|')
    #IncidentNumber, IncidentType, Name, Exercise, ZeroHour, Country, StreetAddress, Postcode, Comments
    #EventNumber, Name, EventType, Exercise, StartDate, EndDate, Comments

    if bundle[0] == 'create_dvrcase':
        print 'Dead Victim Case'
        if bundle[4] == 'male':
            bundle[4] = '3'
        elif bundle[4] == 'female':
            bundle[4] = '1'
        else:
            bundle[4] = '2'

            if bundle[10] == "High":
                bundle[10] = '2'
            elif bundle[10] == "Very High":
                bundle[10] = '1'
            elif bundle[10] == "Medium":
                bundle[10] = '3'
            elif bundle[10] == "Low":
                bundle[10] = '4'

            if bundle[11] == "Yes":
                bundle[11] = '1'
            else:
                bundle[11] = '0'


            if bundle[12] == "Open":
                bundle[12] = '1'
            elif bundle[12] == "Accepted":
                bundle[12] = '2'
            elif bundle[12] == "Rejected":
                bundle[12] = '3'            

        if bundle  [8] == '':
            bundle[8] = "gowalmandi"
        data = '{"$_dvr_case":[{'

        data += '"reference":"' + bundle[1] + '"'
        data += ',"$k_person_id":{"@resource":"pr_person","@tuid":"' + bundle[2] + '"}'
        data += ',"date_of_birth":"' + bundle[3] + '"'
        data += ',"mobile_phone":"' + bundle[5] + '"'
        data += ',"email":"' + bundle[6] + '"'
        #data += ',"reference":"' + bundle[7] + '"'
        data += ',"address":"' + bundle[8] + '"'
        data += ',"postcode":"' + bundle[9] + '"'
        data += ',"damage":"' + bundle[10] + '"'
        data += ',"insurance":"' + bundle[11] + '"'
        data += ',"status":"' + bundle[12] + '"'
        data += ',"comments":"' + bundle[13] + '"'
        data += ',"gender":"' + bundle[4] + '"}],'
        data += '"$_pr_person":[{"@tuid":"' + bundle[2] + '"'
        data += ',"first_name":"' + bundle[2] + '","gender":"' + bundle[4] + '"}]'
        data += '}'
        dvr_url = host + '/eden/dvr/case.s3json'

        print data

        r = requests.put(dvr_url, data, auth=HTTPBasicAuth(username,password))
        print r.text


    elif bundle[0] == 'create_event':
        print 'Create Event Case'
        data = '{"$_event_event":[{'

        #EventNumber, Name, EventType, Exercise, StartDate, EndDate, Comments
        #data += '"event_number":"' + bundle[1] + '"'
        data += '"name":"' + bundle[1] + '"'
        data += ',"$k_event_type_id":{"@resource":"event_event_type","@tuid":"' + bundle[3] + '"}'
        #data += ',"event_type_id":"' + bundle[2] + '"'
        data += ',"exercise":"' + bundle[3] + '"'
        data += ',"start_date":"' + bundle[4] + '"'
        data += ',"end_date":"' + bundle[5] + '"'
        data += ',"comments":"' + bundle[6] + '"}],'
        data += '"$_event_event_type":[{"@tuid":"' + bundle[2] + '"'
        data += ',"name":"' + bundle[2] + '","comments":"' + bundle[6] + '"}]'
        data += '}'
        event_url = host + '/eden/event/event.s3json'
        print data
        r = requests.put(event_url, data, auth=HTTPBasicAuth(username,password))
        print r.text

    elif bundle[0] == 'create_incident':
        print 'Create Incident Case'
        #IncidentNumber, IncidentType, Name, Exercise, ZeroHour, Country, StreetAddress, Postcode, Comments
        data = '{"$_event_incident":[{'

        #data += '"event_id":"' + bundle[1] + '"'
        data += '"name":"' + bundle[2] + '"'
        data += ',"$k_incident_type_id":{"@resource":"event_incident_type","@tuid":"' + bundle[1] + '"}'
        data += ',"exercise":"' + bundle[3] + '"'
        #data += ',"zero_hour":"' + bundle[4] + '"'
        #data += ',"country":"' + bundle[5] + '"'
        #data += ',"street_address":"' + bundle[6] + '"'
        #data += ',"postcode":"' + bundle[7] + '"'
        data += ',"comments":"' + bundle[8] + '"}],'
        data += '"$_event_incident_type":[{"@tuid":"' + bundle[1] + '"'
        data += ',"name":"' + bundle[1] + '","comments":"' + bundle[8] + '"}]'
        data += '}'
        incident_url = host + '/eden/event/incident.s3json'
        print data
        r = requests.put(incident_url, data, auth=HTTPBasicAuth(username,password))
        print r.text
    else:
        print "Acknowledgement Received!"
    

if __name__ == "__main__":
    main(sys.argv[1])