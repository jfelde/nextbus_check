#!/usr/bin/env python

import smtplib
import urllib2

agency = 'umd'
route = '104'
dest = 'stamsu'
stop = 'cpmetro_d'

url = 'http://webservices.nextbus.com/service/publicXMLFeed?command=predictions&a='+agency+'&r='+route+'&d='+dest+'&s='+stop

req = urllib2.Request(url)

response = urllib2.urlopen(req)

the_page = response.read()

if 'dirTitleBecauseNoPredictions' in the_page:
        sender = 'noreply@icecube.umd.edu'
        with open('email_addresses.txt','r') as f:
            receivers = f.readlines()

        message =  "From: noreply <noreply@icecube.umd.edu>\n"
        message += "To: "
        for receiver in receivers[:-1]:
            message += "<{0}>, ".format(receiver.strip())
        message += "<{0}>\n".format(receivers[-1].strip())
        message += "Subject: UMD Shuttle 104\n\n"
        message += "It looks like the shuttle is not running. "
        message += "You should check.\n\n"
        message += "http://www.transportation.umd.edu/service_cal.html"
	
        try:
                smtpObj = smtplib.SMTP('localhost')
                smtpObj.sendmail(sender, receivers, message)
                #print "Email Sent"
        except:
                pass
                #print "Error: Could not send mail!"
else:
        pass
        #print 'Bus '+route+' is running!'

