Feature: Formatprüfungen Antrag

  Scenario Outline: Formatprüfungen Antrag anlegen
    Given Ich erfasse einen neuen Antrag
    When der Antragsteller hat die ID <kundeId>
    When der Fuehrerschein wurde am <fueherscheindatum> erworben
    When das Fahrzeug hat die HSN / TSN <hsn> <tsn>
    When das Fahrzeug ist ein(e) <kategorie>
    When das Fahrzeug wurde am <ez> erstmals zugelassen
    When das Fahrzeug wird im Jahr <kilometer> km gefahren
    When das Fahrzeug wird <verwendung> genutzt
    When der gewünschte Versicherungsbeginn ist der <versicherungsbeginn>
    Then es erscheint der Antrags-Status <status> mit Meldung <meldung>

    Examples:
    | kundeId | fuehrerscheindatum  | hsn   | tsn  | kategorie                | ez          | kilometer | verwendung  | versicherungsbeginn     | status    | meldung                           |
    | 1       | 01-01-1978          | 001   | 1234 | Kombi                    | 01-01-2021  | 20.000    | privat      | 01-11-2022              | ok        | Prüfungen erfolgreich             |
    | 1       | 01-01-1978          | xxx   | 1234 | Kombi                    | 01-01-2021  | 20.000    | privat      | 01-11-2022              | nok       | Ungültige HSN angegeben           |
    | 1       | 01-01-1978          | 123   | 12   | Kombi                    | 01-01-2021  | 20.000    | privat      | 01-11-2022              | nok       | Ungültige TSN angegeben           |
    | 1       | 01-01-1978          | 123   | 12   | *** Bitte auswählen ***  | 01-01-2021  | 20.000    | privat      | 01-11-2022              | nok       | Ungültige Kategorie angegeben     |
