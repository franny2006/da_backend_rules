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



@then('es erscheint der Status {status} mit Meldung {meldung}')
def step_Response(context, status, meldung):
    context.status = status
    context.meldung = meldung

    url = 'http://localhost:5010/api/v1/resources/verifyKunde'
    payload = {
        'rolle': '' + context.rolle + '',
        'anrede': '' + context.anrede + '',
        'name': '111',
        'vorname': '111',
        'strasse': '111',
        'plz': '12345',
        'ort': '111'}
    jsonPayload = json.dumps(payload, default=str)
    jsonPayload = json.loads(jsonPayload)
    response = requests.post(url, json=jsonPayload)
    data = response.json()
 #   print("Response: ", data['status']['result'], data['status']['rc'])
    context.responseResult = data['status']['result']
    context.responseRc = data['status']['rc']
 #   print(context.status)


    assert context.status == data['status']['result']
    assert context.meldung == data['status']['rc']