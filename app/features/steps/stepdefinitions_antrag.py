from behave import *
import requests
import json
import sys
sys.path.insert(0, '../../')


@given('Ich erfasse einen neuen Antrag')
def step_impl(context):
    pass

@when('der Antragsteller hat die ID {kundeId}')
def step_Kunde(context, kundeId):
    context.kundeId = kundeId

@when('der Fuehrerschein wurde am {fuehrerscheindatum} erworben')
def step_Fuehrerscheindatum(context, fuehrerscheindatum):
    context.fuehrerscheindatum = fuehrerscheindatum

@when('das Fahrzeug hat die HSN / TSN {hsn} {tsn}')
def step_Hsn_Tsn(context, hsn, tsn):
    context.hsn = hsn
    context.tsn = tsn

@when('das Fahrzeug ist ein(e) {kategorie}')
def step_Kategorie(context, kategorie):
    context.kategorie = kategorie

@when('das Fahrzeug wurde am {ez} erstmals zugelassen')
def step_Ez(context, ez):
    context.ez = ez

@when('das Fahrzeug wird im Jahr {kilometer} km gefahren')
def step_Kilometer(context, kilometer):
    context.kilometer = kilometer

@when('das Fahrzeug wird {verwendung} genutzt')
def step_Verwendung(context, verwendung):
    context.verwendung = verwendung

@when('der gewünschte Versicherungsbeginn ist der {versicherungsbeginn}')
def step_Versicherungsbeginn(context, versicherungsbeginn):
    context.versicherungsbeginn = versicherungsbeginn


@then('es erscheint der Antrags-Status {status} mit Meldung {meldung}')
def step_Response(context, status, meldung):
    context.status = status
    context.meldung = meldung

    url = 'http://localhost:5010/api/v1/resources/verifyOffer'
    payload = {
        'kunde_id': '' + context.kundeId + '',
        'fuehrerschein': '' + context.fuehrerscheindatum + '',
        'hsn': '' + context.hsn + '',
        'tsn': '' + context.tsn + '',
        'kategorie': '' + context.kategorie + '',
        'ez': '' + context.ez + '',
        'fahrleistung': '' + context.kilometer + '',
        'verwendung': '' + context.verwendung + '',
        'versicherungsbeginn': '' + context.versicherungsbeginn + ''}
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