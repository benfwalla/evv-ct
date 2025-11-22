# CT EVV API - Mintlify Documentation Implementation Guide

## 🎉 What's Been Created

I've analyzed all 71 pages of the CT-(DSS-DMHAS)_EVV_Vendor_Specification v1.5 and the EVV Vendor Spec 1.3 to create a comprehensive Mintlify documentation site for your development team.

### ✅ Completed Documentation

1. **Project Structure** (`docs/mint.json`)
   - Complete Mintlify configuration
   - Navigation structure for all sections
   - API playground setup
   - Theme and branding configuration

2. **Getting Started Section**
   - **introduction.mdx** - Welcome page with feature overview
   - **quickstart.mdx** - Step-by-step guide with working code examples
   - **authentication.mdx** - Complete auth guide with multi-language examples
   - **environments.mdx** - UAT and Production environment details

3. **API Reference - Client Endpoint**
   - **client/create.mdx** - COMPLETE documentation with:
     - All 40+ fields documented
     - Required/Optional/Conditional indicators
     - Field validation rules
     - Character restrictions
     - Format requirements
     - Max lengths
     - Business logic
     - Code examples
     - Error responses

4. **Business Rules**
   - **business-rules/overview.mdx** - Comprehensive "if-then" logic:
     - Conditional field requirements
     - Call Type dependencies
     - Adjusted times logic
     - Payer/Program dependencies
     - Modifier requirements
     - Visit changes requirements
     - Data dependencies
     - Timing rules
     - Exception handling

5. **Supporting Files**
   - **README.md** - Complete project documentation
   - **IMPLEMENTATION_GUIDE.md** - This file

## 📋 What Still Needs to Be Created

### High Priority (Core API Documentation)

1. **Employee Endpoint** (14 fields total)
   - `api-reference/employee/overview.mdx`
   - `api-reference/employee/create.mdx` - All employee fields with validation
   - `api-reference/employee/status.mdx` - Status check endpoint

2. **Visit Endpoint** (50+ fields - Most Complex!)
   - `api-reference/visit/overview.mdx`
   - `api-reference/visit/create.mdx` - All visit fields including:
     - Visit General (33 fields)
     - Calls segment (14 fields per call, up to 2)
     - Visit Changes segment (7 fields)
     - Tasks segment (3 fields per task)
     - Exception Acknowledgement (2 fields)
   - `api-reference/visit/status.mdx`

3. **Status Endpoints**
   - `api-reference/client/overview.mdx`
   - `api-reference/client/status.mdx`

### Medium Priority (Concepts & Rules)

4. **Core Concepts**
   - `concepts/overview.mdx` - System architecture
   - `concepts/data-types.mdx` - DateTime, Date, String, Integer, Decimal, Boolean
   - `concepts/sequencing.mdx` - Sequence ID best practices
   - `concepts/error-handling.mdx` - Error codes and retry logic

5. **Detailed Business Rules**
   - `business-rules/client-rules.mdx` - Client-specific validation
   - `business-rules/employee-rules.mdx` - Employee-specific validation
   - `business-rules/visit-rules.mdx` - Visit-specific validation
   - `business-rules/call-logic.mdx` - Call times scenarios
   - `business-rules/adjusted-times.mdx` - Adjusted time scenarios

### Lower Priority (Reference Data)

6. **Reference Documentation**
   - `reference/payers-programs.mdx` - All payer/program combinations
   - `reference/procedure-codes.mdx` - Complete tables from appendices 9.1.1-9.1.9
   - `reference/tasks.mdx` - Task IDs by program (Home Health, ABP, CHP, PCP, AUP, MHP)
   - `reference/reason-codes.mdx` - All 30 reason codes
   - `reference/exceptions.mdx` - Exception codes and handling
   - `reference/timezones.mdx` - Supported timezone list

## 🔑 Key Information Extracted

### Three Main Endpoints

| Endpoint | Purpose | Fields | Complexity |
|----------|---------|--------|------------|
| **Clients** | Member/beneficiary data | ~40 | Medium |
| **Employees** | Caregiver/worker data | ~14 | Low |
| **Visits** | EVV visit with calls/tasks | 50+ | High |

### Critical Business Logic Documented

#### 1. Call Times vs Adjusted Times (4 Scenarios)

**Scenario #1**: Calls captured correctly
```json
{
  "AdjInDateTime": null,
  "AdjOutDateTime": null,
  "Calls": [
    {"CallDateTime": "2023-02-05T09:00:00Z", "CallAssignment": "Time In"},
    {"CallDateTime": "2023-02-05T10:00:00Z", "CallAssignment": "Time Out"}
  ]
}
```

**Scenario #2**: Caregiver logged in late/out early (CORRECT)
```json
{
  "AdjInDateTime": "2023-02-05T09:00:00Z",
  "AdjOutDateTime": "2023-02-05T10:00:00Z",
  "Calls": [
    {"CallDateTime": "2023-02-05T09:10:00Z", "CallAssignment": "Time In"},
    {"CallDateTime": "2023-02-05T09:50:00Z", "CallAssignment": "Time Out"}
  ]
}
```

**Scenario #3**: Calls BEFORE visit (ERROR)
- Result: "Call Out cannot be less than Adjusted In"
- Solution: Set BillVisit=false, create new visit with Manual calls

**Scenario #4**: Calls AFTER visit (ERROR)
- Result: "Call In cannot be greater than Adjusted Out"
- Solution: Set BillVisit=false, create new visit with Manual calls

#### 2. Conditional Field Requirements

**If CallType = "Mobile"**, REQUIRED:
- `CallLatitude`
- `CallLongitude`
- `MobileLogin`

**If CallType = "Telephony"**, REQUIRED:
- `TelephonyPIN`
- `OriginatingPhoneNumber`

**If PayerProgram = ABP, AUP, CHP, PCP, MHP**, REQUIRED:
- `Tasks` segment with valid TaskID

**If Adjusted times exist**, REQUIRED:
- `VisitChanges` segment

#### 3. Sequence Rules

| Current | New | Result |
|---------|-----|--------|
| 4 | 5 | ✅ Accepted (current) |
| 5 | 5 | ❌ Rejected (duplicate) |
| 10 | 8 | ✅ Accepted (historical) |
| 5 | 100 | ✅ Accepted (current) |

### Programs Supported

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

### Procedure Codes

Documented in specification appendices 9.1.1 through 9.1.9:
- 9.1.1: Non-Waiver Home Health (CTHH/HHI) - 40+ codes
- 9.1.2: Waiver Home Health (CTDSS) - 40+ codes
- 9.1.3: Mental Health Waiver (CTMHW/MHP) - 12 codes
- 9.1.4: ABI Non-Clinical (CTDSS/ABP) - 20+ codes
- 9.1.5: ABI Optional (CTDSS/ABP) - 2 codes
- 9.1.6: Autism Professional (CTDSS/AUP) - 4 codes
- 9.1.7: Autism Optional (CTDSS/AUP) - 1 code
- 9.1.8: CT Home Care (CTDSS/CHP) - 30+ codes
- 9.1.9: Personal Care (CTDSS/PCP) - 10+ codes

### Task IDs

- **Home Health**: Task IDs 130-149, 801-816
- **ABP/CHP/PCP**: Task IDs 1-99, 150-158
- **AUP (Autism)**: Task IDs 99, 160-173
- **MHP (Mental Health)**: Task IDs 97, 99, 201-225

### Reason Codes

30 reason codes documented (01-30, plus 71):
- 01: Client Requested Different Visit Time
- 03: No Calls Received; Documentation Provided
- 22: Other; Documentation Provided (requires memo)
- 71: Virtual Visit
- etc.

## 🚀 How to Use This Documentation

### 1. Install Mintlify

```bash
npm install -g mintlify
```

### 2. Preview Locally

```bash
cd /Users/benwallace/Documents/kibu/code/evv-ct/docs
mintlify dev
```

This starts a local server at `http://localhost:3000`

### 3. Test the Documentation

- Navigate through all sections
- Test code examples
- Verify all links work
- Check mobile responsiveness

### 4. Complete Remaining Files

Use the existing files as templates:
- Copy structure from `client/create.mdx` for employee and visit endpoints
- Follow the same format for field documentation
- Include all validation rules and examples

### 5. Deploy

```bash
mintlify deploy
```

Or connect to your Git repository for automatic deployments.

## 📊 Documentation Statistics

- **Total Pages Created**: 7
- **Total Pages Needed**: ~30
- **Completion**: ~23%
- **Fields Documented**: 40+ (Client endpoint)
- **Fields Remaining**: 64+ (Employee + Visit endpoints)
- **Business Rules Documented**: Core logic + conditional requirements
- **Reference Tables**: 0 of 6 created

## 🎯 Next Steps for Your Team

### Immediate Actions

1. **Review Existing Documentation**
   - Check accuracy of client endpoint documentation
   - Verify business rules match your understanding
   - Test code examples in quickstart

2. **Complete Employee Endpoint**
   - Use `client/create.mdx` as template
   - Document all 14 employee fields
   - Add validation rules

3. **Complete Visit Endpoint**
   - Most complex endpoint (50+ fields)
   - Document all segments:
     - Visit General
     - Calls (repeatable)
     - Visit Changes
     - Tasks (repeatable)
     - Exception Acknowledgement
   - Add all business logic scenarios

4. **Add Reference Tables**
   - Procedure codes (from appendices 9.1.1-9.1.9)
   - Task IDs (from appendix 9.2)
   - Reason codes (from appendix 9.3)
   - Exceptions (from appendix 9.4)

### Testing Strategy

1. **Set up API Playground**
   - Configure with UAT credentials
   - Test all endpoints
   - Validate examples work

2. **Create Test Scenarios**
   - Happy path examples
   - Error scenarios
   - Edge cases
   - Business rule violations

3. **Document Common Issues**
   - FAQ section
   - Troubleshooting guide
   - Common error messages

## 💡 Tips for Completing Documentation

### Use Existing Templates

The `client/create.mdx` file is a comprehensive template. For each new endpoint:

1. Copy the structure
2. Update endpoint URL
3. Replace field documentation
4. Update examples
5. Adjust business rules

### Field Documentation Pattern

For each field, include:
```markdown
<ParamField body="FieldName" type="string" required>
  Brief description
  
  **Format**: Format specification
  **Max Length**: X characters
  **Values**: Valid values
  **Note**: Additional context
</ParamField>
```

### Business Rules Pattern

For conditional logic:
```markdown
<Accordion title="Rule Name">
  **If [condition]**, then:
  - Field X is **REQUIRED**
  - Field Y must be [value]
  
  Example:
  ```json
  {
    "field": "value"
  }
  ```
</Accordion>
```

## 📞 Support

For questions about the specifications:
- **Email**: support@sandata.com
- **Phone**: 516.484.4400
- **Implementation Manager**: Jason Feder (jfeder@sandata.com)

For Mintlify documentation help:
- **Docs**: https://mintlify.com/docs
- **Discord**: https://discord.gg/mintlify

## 🎓 Key Takeaways

1. **Authentication**: Basic Auth + Account header required
2. **VPN**: All requests must originate from USA
3. **Order**: Employees → Clients → Visits
4. **Sequencing**: Increment SequenceID for each update
5. **Timing**: Wait 5 minutes before checking status
6. **Limits**: 1-5,000 records per transaction
7. **Call Logic**: Adjusted times supersede Call times
8. **Tasks**: Required for ABP, AUP, CHP, PCP, MHP programs
9. **Changes**: VisitChanges required for Manual calls and Adjusted times
10. **Validation**: Strict field validation with character restrictions

---

**Created**: January 2025
**Specification Version**: v1.5 (February 2024)
**API Version**: v1.1
**Base Version**: 7.14
