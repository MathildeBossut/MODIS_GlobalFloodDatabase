# MODIS Global Flood Detection (Python 3 Fork)

This repository is a streamlined and updated fork of the original **MODIS Global Flood Database** codebase:
[https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase](https://github.com/cloudtostreet/MODIS_GlobalFloodDatabase)

The original work is described in:

> Tellman, B., Sullivan, J. A., Kuhn, C. et al. *Satellite imaging reveals increased proportion of population exposed to floods.* Nature (2021). [https://doi.org/10.1038/s41586-021-03695-w](https://doi.org/10.1038/s41586-021-03695-w)

---

## Overview

This fork focuses specifically on **flood detection using MODIS satellite imagery**, removing unrelated components and modernizing the codebase.

The goal is to provide a **clean, minimal, and Python 3–compatible implementation** of the flood detection workflow described in Tellman et al. (2021).

---

## Key Changes from Original Repository

### 1. Focus on Flood Detection Only

All non-essential components have been removed. This repository retains only code directly related to water detection, flood extent mapping and MODIS image processing relevant to flood identification

### 2. Python 3 Migration

The original repository was written in Python 2. This fork updates syntax to Python 3.

### 3. Updated Satellite Data References

References to satellite data repositories have been corrected and modernized, including updated MODIS data access endpoints and compatibility with current NASA/LP DAAC and Google Earth Engine workflows (where applicable)
