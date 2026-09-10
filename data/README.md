# Bundled data

These are aggregate project inputs and explicitly identified reference outputs,
not individual farmer claim histories. `manifest.json` gives file names, schemas,
counts, provenance and checksums. Compression keeps every file below 25 MB.

Notebook 01 consumes `base_gold`, `weather_seasonal`, `vegetation_seasonal`.
Notebook 03 consumes `source_master`, `nasa_daily`, `modis_seasonal`.
`final_master` is the historical reference for inspection, not a shortcut target
used to train or score the models.

The master combines PMFBY/DES agricultural/insurance context and geographic
references. NASA POWER supplies weather. MODIS supplies satellite vegetation;
Google Earth Engine is an extraction platform, not the satellite data source.

These supplied third-party data snapshots retain their original source rights.
This repository does not assert ownership or apply a blanket new data licence.
Raw collection credentials and browser/account material are not included.
