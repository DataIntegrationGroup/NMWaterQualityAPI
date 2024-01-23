This API provides access to the Aquifer Mapping Program's Water Quality database. 
This is a collection of water chemistry data collected from wells and springs throughout New Mexico from
the USGS, NMBGMR, and other agencies.

# Data

## General
The data is stored in a MSSQL database. The database is updated on a semi-regular basis
with new manually measured depth to groundwater measurements.

Some of the data collected by NMBGMR is private and requires appropriate privileges and authentication for access. All endpoints that begin with **/authorization** requires authentication.
