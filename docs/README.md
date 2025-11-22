# CT EVV API Documentation

This is a comprehensive Mintlify documentation site for the Connecticut Electronic Visit Verification (EVV) Vendor API.

## What's Been Created

### ✅ Core Documentation
- **mint.json** - Complete Mintlify configuration with navigation structure
- **introduction.mdx** - Welcome page with overview and key features
- **quickstart.mdx** - Step-by-step guide to make first API calls
- **authentication.mdx** - Detailed authentication guide with code examples
- **environments.mdx** - UAT and Production environment details

### ✅ API Reference
- **api-reference/client/create.mdx** - Complete Client endpoint documentation with all 40+ fields, validation rules, and examples

### 📋 Still To Create

The following files need to be created to complete the documentation:

#### Core Concepts
- `concepts/overview.mdx` - Overview of EVV system architecture
- `concepts/data-types.mdx` - DateTime, Date, String, Integer, Decimal, Boolean formats
- `concepts/sequencing.mdx` - Sequence ID rules and best practices
- `concepts/error-handling.mdx` - Error codes, rejection handling, retry logic

#### API Reference - Client
- `api-reference/client/overview.mdx` - Client endpoint overview
- `api-reference/client/status.mdx` - GET status endpoint for clients

#### API Reference - Employee
- `api-reference/employee/overview.mdx` - Employee endpoint overview
- `api-reference/employee/create.mdx` - POST employee with all fields
- `api-reference/employee/status.mdx` - GET status endpoint for employees

#### API Reference - Visit
- `api-reference/visit/overview.mdx` - Visit endpoint overview
- `api-reference/visit/create.mdx` - POST visit with all fields (most complex - 50+ fields)
- `api-reference/visit/status.mdx` - GET status endpoint for visits

#### Business Rules
- `business-rules/overview.mdx` - Overview of validation rules
- `business-rules/client-rules.mdx` - Client-specific validation rules
- `business-rules/employee-rules.mdx` - Employee-specific validation rules
- `business-rules/visit-rules.mdx` - Visit-specific validation rules
- `business-rules/call-logic.mdx` - Call times vs Adjusted times logic
- `business-rules/adjusted-times.mdx` - Detailed adjusted time scenarios

#### Reference Data
- `reference/payers-programs.mdx` - All payer IDs and program codes
- `reference/procedure-codes.mdx` - Complete procedure code tables (9.1.1 - 9.1.9)
- `reference/tasks.mdx` - Task IDs by program (Home Health, ABP, CHP, PCP, AUP, MHP)
- `reference/reason-codes.mdx` - All 30 reason codes with descriptions
- `reference/exceptions.mdx` - Exception codes and handling
- `reference/timezones.mdx` - Supported timezone list

## Key Information from Specifications

### Three Main Endpoints

1. **Clients** - Member/beneficiary receiving care
2. **Employees** - Caregiver/worker providing service
3. **Visits** - EVV visit data with calls, tasks, and changes

### Supported Programs

- **CTHH/HHI** - Home Health Non-Waiver
- **CTDSS/ABI** - Acquired Brain Injury Waiver
- **CTDSS/AUI** - Autism Waiver
- **CTDSS/CHI** - CT Home Care Waiver
- **CTDSS/PCI** - Personal Care Waiver
- **CTDSS/ABP** - Acquired Brain Injury Non-Clinical
- **CTDSS/AUP** - Autism Professional
- **CTDSS/CHP** - CT Home Care Program
- **CTDSS/PCP** - Personal Care Assistant
- **CTMHW/MHP** - Mental Health Waiver Program

### Critical Business Logic

#### Call Times vs Adjusted Times
- **Scenario #1**: Calls captured correctly → No adjusted times needed
- **Scenario #2**: Caregiver logged in late/out early → Use adjusted times to correct
- **Scenario #3**: Calls before visit → ERROR, must use BillVisit=false and create new visit
- **Scenario #4**: Calls after visit → ERROR, must use BillVisit=false and create new visit

#### Sequence Rules
- First submission: SequenceID = 1
- Each update: Increment SequenceID
- Duplicate SequenceID = Rejected
- Lower SequenceID = Accepted as historical
- Can use timestamp format: YYYYMMDDHHMMSS

#### Visit Changes Segment
- Required when: CallType = Manual, Adjusted times exist, or any visit update
- Must include: SequenceID, ChangeMadeBy, ChangeDateTime, ReasonCode
- Optional: ChangeReasonMemo (required for some reason codes)

## Running the Documentation

### Install Mintlify

```bash
npm i -g mintlify
```

### Preview Locally

```bash
cd docs
mintlify dev
```

This will start a local server at `http://localhost:3000`

### Deploy to Mintlify

```bash
mintlify deploy
```

## Field Counts by Endpoint

### Client Endpoint
- **Provider Identification**: 2 fields
- **Client General**: 13 fields
- **Client Address**: 10 fields per address (repeatable)
- **Client Payer**: 12 fields per payer (repeatable)
- **Client Phone**: 2 fields per phone (repeatable)
- **Total**: ~40+ fields

### Employee Endpoint
- **Provider Identification**: 2 fields
- **Employee General**: 12 fields
- **Total**: ~14 fields

### Visit Endpoint (Most Complex)
- **Provider Identification**: 2 fields
- **Visit General**: 33 fields
- **Calls**: 14 fields per call (up to 2 calls)
- **Visit Changes**: 7 fields (required for updates)
- **Tasks**: 3 fields per task (repeatable)
- **Visit Exception Acknowledgement**: 2 fields per exception
- **Total**: 50+ fields

## Important Notes

### VPN Requirement
All API requests MUST originate from within the USA. International requests will be rejected.

### Transaction Limits
- Minimum: 1 record per transaction
- Maximum: 5,000 records per transaction
- Exceeding limit = entire transaction rejected

### Processing Time
- Typical: 30 seconds to 5 minutes
- Wait 5 minutes before checking status
- UUID available for 48 hours

### Data Dependencies
1. Create Employees first
2. Create Clients second
3. Submit Visits last (require both employee and client to exist)

## Contact

For implementation support:
- **Email**: support@sandata.com
- **Phone**: 516.484.4400 x4343
- **Implementation Manager**: Jason Feder (jfeder@sandata.com)

## Version

This documentation covers **API Version 1.5** (February 2024)
- Base Version: 7.14
- Specification: CT-(DSS-DMHAS)_EVV_Vendor_Specification v1.5
