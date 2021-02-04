# Tested with Python 3.5.3
# Python 2 does not have urllib.request (see https://docs.python.org/2/library/urllib2.html)
# so will not work with Python 2

# Linked to from Wikipedia talk page:
# https://en.wikipedia.org/wiki/Template_talk:Undisclosed_paid#Proposal_to_add_language_to_the_template_saying_that_the_payer_may_not_be_the_subject_of_the_article

import urllib.request
import json

#The list of titles are those found which were tagged
#by User:Blablubbs from this list of contributions:
#https://en.wikipedia.org/w/index.php?title=Special:Contributions/Blablubbs&offset=20201210151938&limit=500&target=Blablubbs
#which go from December 4, 2020 to December 10, 2020, and so
#searched for the string, "undisclosed paid" in the list.
titles=['J.Crew', 'Mike_Coupe', 'Alan_Joyce_(executive)', 'WhatsApp', 'Walton_Group', 'Advent_International', 'Frank_McCabe_(businessman)', 'Newbridge_Silverware', 'Self_Help_Africa', 'Tyrone_Yates', 'Goldman_Sachs', 'Leonard_Green_%26_Partners', 'Bob_Chapek', 'Craig_Miller_(CEO)', 'Ken_Whyte', 'Lochlann_Quinn', 'Eric_Fingerhut', 'Greg_Murphy_(politician)', 'Rico_Oller', 'Rockefeller_Foundation', 'Strive_Masiyiwa', 'Carrie_Hessler-Radelet', 'Maria_Elvira_Salazar', 'Wendy_Greuel', 'Steve_Blank', 'August_Capital', 'Julie_Smolyansky', 'Lisa_Falzone', 'Goldbelly', 'Efrat_Peled', 'Nordstrom', 'BHLDN', 'TechStyle_Fashion_Group', 'T._Rowe_Price', 'Adam_Hootnick', 'Adore_Me', 'Jonathan_Lavine', 'Winder_Farms', 'Watsi', 'Hasura', 'Affirm_(company)', 'Patagonia,_Inc.', 'Travis_Kalanick', 'Doximity', 'Gerard_Adams', 'Monzo', 'DoorDash', 'Ibotta', 'Hims,_Inc.', 'Phoenix_Technologies', 'Chris_Cox_(Facebook)', 'Partners_In_Health', 'Sarah_Gray_Miller', 'ColourPop_Cosmetics', 'Bustle_(magazine)', 'Uber_Eats', 'Edgewell_Personal_Care', 'Maxim_(magazine)', 'Tivity_Health', 'Sam_Nazarian', 'Everyday_Food', 'Rogers_Communications', "Today's_Parent", 'Health_(magazine)', "Women's_Health_(magazine)", 'Project_C.U.R.E.', 'Providence_St._Joseph_Health', 'Hospitals_of_Hope', 'CareFirst_BlueCross_BlueShield', 'Centene_Corporation', 'Haven_Healthcare', 'Encompass_Health', 'Yuma_Regional_Medical_Center', 'Jeff_Kindler', 'Michael_Neidorff', 'AmerisourceBergen', 'Orlando_Health', 'Northwest_MedStar', 'Apoth%C3%A9Cure_Inc.', 'McKesson_Corporation', 'Finastra', 'OraSure_Technologies', 'Medco_Health_Solutions', 'Bellin_Health', 'Mentor_(company)', 'Pharmacia_%26_Upjohn', 'Fidelis_Care']
titles_show=['J.Crew', 'Mike Coupe', 'Alan Joyce (executive)', 'WhatsApp', 'Walton Group', 'Advent International', 'Frank McCabe (businessman)', 'Newbridge Silverware', 'Self Help Africa', 'Tyrone Yates', 'Goldman Sachs', 'Leonard Green & Partners', 'Bob Chapek', 'Craig Miller (CEO)', 'Ken Whyte', 'Lochlann Quinn', 'Eric Fingerhut', 'Greg Murphy (politician)', 'Rico Oller', 'Rockefeller Foundation', 'Strive Masiyiwa', 'Carrie Hessler-Radelet', 'Maria Elvira Salazar', 'Wendy Greuel', 'Steve Blank', 'August Capital', 'Julie Smolyansky', 'Lisa Falzone', 'Goldbelly', 'Efrat Peled', 'Nordstrom', 'BHLDN', 'TechStyle Fashion Group', 'T. Rowe Price', 'Adam Hootnick', 'Adore Me', 'Jonathan Lavine', 'Winder Farms', 'Watsi', 'Hasura', 'Affirm (company)', 'Patagonia, Inc.', 'Travis Kalanick', 'Doximity', 'Gerard Adams', 'Monzo', 'DoorDash', 'Ibotta', 'Hims, Inc.', 'Phoenix Technologies', 'Chris Cox (Facebook)', 'Partners In Health', 'Sarah Gray Miller', 'ColourPop Cosmetics', 'Bustle (magazine)', 'Uber Eats', 'Edgewell Personal Care', 'Maxim (magazine)', 'Tivity Health', 'Sam Nazarian', 'Everyday Food', 'Rogers Communications', "Today's Parent", 'Health (magazine)', "Women's Health (magazine)", 'Project C.U.R.E.', 'Providence St. Joseph Health', 'Hospitals of Hope', 'CareFirst BlueCross BlueShield', 'Centene Corporation', 'Haven Healthcare', 'Encompass Health', 'Yuma Regional Medical Center', 'Jeff Kindler', 'Michael Neidorff', 'AmerisourceBergen', 'Orlando Health', 'Northwest MedStar', 'ApothéCure Inc.', 'McKesson Corporation', 'Finastra', 'OraSure Technologies', 'Medco Health Solutions', 'Bellin Health', 'Mentor (company)', 'Pharmacia & Upjohn', 'Fidelis Care']

tagged_titles=[]
untagged_titles=[]

print(u'Now iterating through list of fitles...')
for title in titles:

    req2 = urllib.request.Request(url='https://en.wikipedia.org/w/api.php?action=query&prop=revisions&titles='+title+'&rvslots=*&rvprop=content&format=json')

    s=""
    with urllib.request.urlopen(req2) as f:
            s = s+f.read().decode('utf-8')

    st = json.loads(s)
    pageid = list(st[u'query'][u'pages'])[0]
    assert(str(st[u'query'][u'pages'][pageid][u'pageid']) == pageid)
    wikitext = st[u'query'][u'pages'][pageid][u'revisions'][0][u'slots'][u'main'][u'*']
    # There are other cases...say if that is in <nowiki></nowiki>, or in comments say...<!-- -->
    #...but can just keep it simple for now.... User:Jjjjjjjjjj (David Kit Friedman) 2021-01-31
    if (wikitext.find(u'{{Undisclosed paid') != -1):
        print('{:40s}'.format(title) + '{:40s}'.format('found indication of undisclosed paid editing tag.'))
        tagged_titles.append(title)
    else:
        print('{:40s}'.format(title))
        untagged_titles.append(title)

print()
print(u'Total found without indication of tag: '+str(len(untagged_titles)))
print()

for i in range(len(untagged_titles)):
    print('{:02d}'.format(i+1)+'. '+untagged_titles[i])

print()
print(u'Total found with indication of tag: '+str(len(tagged_titles)))
print()

for i in range(len(tagged_titles)):
    print('{:02d}'.format(i+1)+'. '+tagged_titles[i])
