#!/bin/sh

# This script requires the following tools:
#   - nmap: to execute ip/range scans (format 0-255.0-255.0-255.0-255) or domains.
#   - ndiff: for the comparison of the last two scans.

mkdir /nmapscans
nmap -F $1 -oX /nmapscans/scan.xml

if [ -f "/nmapscans/lastscan.xml" ]
then
    echo "=============== PRINTING DIFFERENCES BETWEEN LAST 2 SCANS ==============="
    ndiff -v /nmapscans/lastscan.xml /nmapscans/scan.xml
    cp /nmapscans/scan.xml /nmapscans/lastscan.xml
    echo "Completed"
else
    cp /nmapscans/scan.xml /nmapscans/lastscan.xml
    echo "Previous scans not available to be compared. Exiting."
fi