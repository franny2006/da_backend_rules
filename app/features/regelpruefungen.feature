Feature: Formatprüfungen

  Scenario Outline: Formatprüfungen Kunde anlegen
    Given Ich erfasse einen neuen Kunden
    When der Kunde hat die Rolle <rolle>
    When der Kunde hat die Anrede <anrede>
    When der Kunde hat den Vornamen <vorname>
    When der Kunde hat den Namen <name>
    When der Kunde wohnt in Strasse <strasse>
    When der Kunde wohnt in PLZ <plz>
    When der Kunde wohnt in Ort <ort>
    When der Kunde ist geboren am <geburtsdatum>
    Then es erscheint der Status <status> mit Meldung <meldung>

    Examples:
    | rolle | anrede  | vorname | name  | strasse | plz    | ort | geburtsdatum  | status     | meldung                           |
    | 1     | 1       | vorname | name  | strasse | 12345  | ort | 17-11-1973    | ok         | Prüfungen erfolgreich             |
    | 2     | 1       | vorname | name  | strasse | 12345  | ort | 17-11-1973    | ok         | Prüfungen erfolgreich             |
    | 3     | 1       | vorname | name  | strasse | 12345  | ort | 17-11-1973    | ok         | Prüfungen erfolgreich             |
    | A     | 1       | vorname | name  | strasse | 12345  | ort | 17-11-1973    | nok        | Ungültiger Wert in Feld 'Rolle'   |
    | 1     | 1       | vo      | name  | strasse | Test   | ort | 17-11-1973    | nok        | PLZ nicht numerisch               |
    | 2     | 2       | vorname | na    | strasse | 12345  | ort | 17-11-1973    | nok        | Ungültiger Wert in Feld 'Name'    |
    | 3     | 3       | vorname | name  | st      | 12345  | ort | 17-11-1973    | nok        | Ungültiger Wert in Feld 'Strasse' |
    | 1     | 1       | vorname | name  | strasse | 12345  | or  | 17-11-1973    | nok        | Ungültiger Wert in Feld 'Ort'     |