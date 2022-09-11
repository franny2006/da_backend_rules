Feature: Formatprüfungen

  Scenario Outline: Formatprüfungen Kunde anlegen
    Given Ich erfasse einen neuen Kunden
    When der Kunde hat die Rolle <rolle>
    When der Kunde hat die Anrede <anrede>
    Then es erscheint der Status <status> mit Meldung <meldung>

    Examples:
    | rolle | anrede  | status    | meldung |
    | 1     | 1       | ok        | Prüfungen erfolgreich        |
    | 2     | 1       | ok        | Prüfungen erfolgreich        |
    | A     | 1       | nok       | Ungültiger Wert in Feld \'Rolle\'        |