from behave import *
import requests
import json
import sys
sys.path.insert(0, '../../')


@given('Ich erfasse einen neuen Kunden')
def step_impl(context):
    pass

@when('der Kunde hat die Rolle {rolle}')
def step_Rolle(context, rolle):
    context.rolle = rolle
 #   context.dictPayload['rolle'] = rolle

 #   assert context.rolle == "9"

@when('der Kunde hat die Anrede {anrede}')
def step_Anrede(context, anrede):
    context.anrede = anrede
 #   context.dictPayload['rolle'] = rolle

@when('der Kunde hat den Vornamen {vorname}')
def step_Vorname(context, vorname):
    context.vorname = vorname

@when('der Kunde hat den Namen {name}')
def step_Name(context, name):
    context.name = name

@when('der Kunde wohnt in Strasse {strasse}')
def step_strasse(context, strasse):
    context.strasse = strasse

@when('der Kunde wohnt in PLZ {plz}')
def step_plz(context, plz):
    context.plz = plz

@when('der Kunde wohnt in Ort {ort}')
def step_Ort(context, ort):
    context.ort = ort

@when('der Kunde ist geboren am {geburtsdatum}')
def step_Geburtsdatum(context, geburtsdatum):
    context.geburtsdatum = geburtsdatum


@then('es erscheint der Status {status} mit Meldung {meldung}')
def step_Response(context, status, meldung):
    context.status = status
    context.meldung = meldung

    url = 'http://localhost:5010/api/v1/resources/verifyKunde'
    payload = {
        'rolle': '' + context.rolle + '',
        'anrede': '' + context.anrede + '',
        'name': '' + context.name + '',
        'vorname': '' + context.vorname + '',
        'strasse': '' + context.strasse + '',
        'plz': '' + context.plz + '',
        'ort': '' + context.ort + '',
        'geburtsdatum': '' + context.geburtsdatum + ''}
    jsonPayload = json.dumps(payload, default=str)
    jsonPayload = json.loads(jsonPayload)
    response = requests.post(url, json=jsonPayload)
    data = response.json()
 #   print("Response: ", data['status']['result'], data['status']['rc'])
    context.responseResult = data['status']['result']
    context.responseRc = data['status']['rc']
 #   print(context.status)


    assert context.status == data['status']['result'], f"Soll: {context.status} - Ist: {data['status']['result']}"
    assert context.meldung == data['status']['rc'], f"Soll: {context.meldung} - Ist: {data['status']['rc']}"