Feature: Formatprüfungen Kunde

  Scenario Outline: Prüfregeln für Kunde anlegen: <titel>
    Given Über die Schnittstelle kommt ein Auftrag zur Kundenanlage
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
    | rolle | anrede  | vorname | name  | strasse | plz    | ort      | geburtsdatum    | status     | meldung                           | titel                            |
    | 1     | 1       | vorname | name  | strasse | 12345  | ort      | 1973-11-17      | ok         | Prüfungen erfolgreich             | Glattläufer Natürliche Person    |
    | 2     | 1       | vorname | name  | strasse | 12345  | ort      | 1973-11-17      | ok         | Prüfungen erfolgreich             | Glattläufer Juristische Person   |
    | 3     | 1       | vorname | name  | strasse | 12345  | ort      | 1973-11-17      | ok         | Prüfungen erfolgreich             | Glattläufer Sonstige Person      |
    | A     | 1       | vorname | name  | strasse | 12345  | ort      | 1973-11-17      | nok        | Ungültiger Wert in Feld 'Rolle'   | Fehlerfall Rolle ungültig        |
    | 1     | 1       | vo      | name  | strasse | Test   | ort      | 1973-11-17      | nok        | PLZ nicht numerisch               | Fehlerfall PLZ nicht numerisch   |
    | 2     | 2       | vorname | na    | strasse | 12345  | ort      | 1973-11-17      | nok        | Ungültiger Wert in Feld 'Name'    | Fehlerfall Name zu kurz          |
    | 3     | 3       | vorname | name  | st      | 12345  | ort      | 1973-11-17      | nok        | Ungültiger Wert in Feld 'Strasse' | Fehlerfall Strasse zu kurz       |
    | 1     | 1       | vorname | name  | strasse | 12345  | or       | 1973-11-17      | nok        | Ungültiger Wert in Feld 'Ort'     | Fehlerfall Ort zu kurz           |
    | 2     | 1       | Horst   | Müller| Plätze 1| 12345  | München  | morgen - 18 y   | nok        | jünger als 18 Jahre               | Fehlerfall jünger als 18         |
    | 2     | 1       | Horst   | Müller| Plätze 1| 12345  | München  | heute - 18 y    | ok         | Prüfungen erfolgreich             | Alter genau 18                   |
    | 2     | 1       | Horst   | Müller| Plätze 1| 12345  | München  | gestern - 18 y  | ok         | Prüfungen erfolgreich             | Alter 18 + 1 Tag                 |
    | 2     | 1       | Ho      | Müller| Plätze 1| 12345  | München  | gestern - 18 y  | ok         | Prüfungen erfolgreich             | Glattläufer Name 2-stellig       |
    | 1     | 1       | vo      | name  | strasse | 12345  | ort      | 1973-11-17      | ok         | Ungültiger Wert in Feld 'Vorname' | Fehlerfall Vorname zu kurz       |
    | 1     | 1       | 1234    | name  | strasse | 12345  | ort      | 1973-11-17      | ok         | Ungültiger Wert in Feld 'Vorname' | Fehlerfall Vorname numerisch     |
    | 1     | 1       | Carla   | 1234  | strasse | 12345  | ort      | 1973-11-17      | ok         | Ungültiger Wert in Feld 'Name'    | Fehlerfall Name numerisch        |