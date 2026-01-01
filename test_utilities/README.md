# Test Utilities

This folder contains utility scripts for development and testing.

## Scripts

### `test_aws_connection.py`
Tests AWS connection and validates credentials are properly configured.

**Usage:**
```bash
python src/test_utilities/test_aws_connection.py
```

### `check_s3_bucket.py`
Checks S3 bucket status and verifies bucket exists and is accessible.

**Usage:**
```bash
python src/test_utilities/check_s3_bucket.py
```

### `check_s3_versions.py`
Lists S3 bucket versioning status and recent object versions.

**Usage:**
```bash
python src/test_utilities/check_s3_versions.py
```

## Purpose

These utilities are used to:
- Verify AWS configuration is correct
- Test S3 connectivity during development
- Debug AWS-related issues
- Validate credentials before running full pipeline
