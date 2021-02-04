# Tested with Python 3.5.3 and Python 2.7.13

# Linked to from Wikipedia talk page:
# https://en.wikipedia.org/wiki/Template_talk:Undisclosed_paid#Proposal_to_add_language_to_the_template_saying_that_the_payer_may_not_be_the_subject_of_the_article

import webbrowser
import sys

not_confirmed = ['GuardLine9', 'PledgeGrant']
suspected_sock_puppets = ['VentureKit',\
                          'Quorum816',\
                          'JP Miller1',\
                          'QuibbleCod',\
                          'Accountmetric',\
                          'Boothit11',\
                          'Marginofinterest',\
                          'GroundFloor',\
                          'GuardLine9',\
                          'PledgeGrant',\
                          'Greente28',\
                          'L0calh0$t',\
                          'Balle010',\
                          'WonderfulWorld',\
                          'Deadbolt44']
confirmed_sock_puppets = [ i for i in suspected_sock_puppets if not (i in not_confirmed)]

for i in range(len(confirmed_sock_puppets)):
    s = 'https://xtools.wmflabs.org/ec/en.wikipedia.org/' + \
        confirmed_sock_puppets[i]        
    print('{:02d}'.format(i+1) + ". " + confirmed_sock_puppets[i])
    print('{:02d}'.format(i+1) + ".  Edit count information: " + confirmed_sock_puppets[i])
    webbrowser.open_new_tab(s)
    print("Press any key to continue...")
    if ( sys.version[0] == '3'):
        input()
    elif ( sys.version[0] == '2'):
        raw_input()

