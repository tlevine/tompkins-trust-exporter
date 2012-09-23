Tompkins Trust History Exporter
============
The  Tompkins Trust History Exporter downloads your Tompkins Trust history in
OFX format and prints it to stdout.

## Dependencies

This needs Python 2 and Firefox.

## Configure

Put your account credentials in `~/.tompkins-trust.json`; see
`.tompkins-trust.json.sample` in this repository for the format.

## Run

Start selenium

    java -jar selenium-server-standalone-2.25.0.jar

Then run the exporter like so

    ./export.py

You'll need to click the save box manualy.
