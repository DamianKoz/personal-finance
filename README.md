# Personal Finance Analyzer

### Funktionen

- Alle Transaktionen anzeigen
- Nach Zeitraum filtern (Monat, Tag etc.)
- Dashboards anzeigen (Ausgaben pro Monat, Ausgaben pro Kategorie)
- Analysen per ML (Vorhersage des nächsten Monats)

### Technical Flow

- Upload Finance data (CSV, Excel, mayber fetch per API from bank)
- Relevante Spalten erkennen
- Transaktions-Model bauen

### Datenmodell

- Transaktion (Name, Datum, Beschreibung, Eigene Beschreibung, Kategorie, Zufriedenheit, Notwendigkeit)

## Setup

#`docker-compose up --build`

or for production:

`docker-compose -f docker-compose.prod.yml up --build`
