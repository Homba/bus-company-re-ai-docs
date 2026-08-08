# Constraints and Compliance

A constraint is not negotiable within this project. Where a stakeholder wish conflicts with a
constraint, the constraint wins and the wish becomes a change request to the constraint owner.

| ID | Constraint | Type | Owner | Consequence for the specification |
|---|---|---|---|---|
| CON-01 | Public procurement law applies; the specification must be vendor-neutral and describe outcomes, not products | legal | Procurement | No product names in FR/NFR; NFR targets must be objectively testable |
| CON-02 | The concession obliges RVB to deliver real-time data to the national platform; this channel cannot be deselected | legal | STK-09 | FR-012 exception; UC-002 flow 6a |
| CON-03 | Passenger information of public bodies must meet the applicable accessibility requirements | legal | STK-15 | NFR-011, NFR-012, FR-021 |
| CON-04 | The solution runs in the cantonal government cloud; only services from the approved catalogue may be used | technical / policy | Canton IT | NFR-019; rules out several managed translation services — see ADR-003 |
| CON-05 | The ITCS core is not replaced in this programme and its interface is the documented VDV 453 subscription only | technical | STK-12 | FR-003; ADR-002 |
| CON-06 | Swiss data protection law applies; a DPIA is required before go-live | legal | STK-11 | NFR-013, NFR-014 |
| CON-07 | Works agreement: vehicle data may not be used for individual performance assessment | organisational | STK-13 | BR-10, FR-029, NFR-014 |
| CON-08 | Budget ceiling CHF 4.2 M across three financial years, with annual cantonal approval | financial | STK-08 | Prioritisation in BR-05; phase 2 candidates in OPN list |
| CON-09 | Language of record for the specification is German; this repository's English version is a working translation | organisational | STK-03 | Terminology disputes resolved against the German glossary |
| CON-10 | Go-live may not fall between 15 December and 10 January (winter service peak) | operational | STK-01 | Release plan; pilot must complete by 30 November |
| CON-11 | Interfaces to the national platform must conform to the SIRI profile the platform mandates | technical | STK-10 | FR-024…FR-026, NFR-018 |
| CON-12 | Staff training must fit into existing shift structures — no more than 4 h per dispatcher | organisational | STK-01 | Drives NFR-002 and the UI simplicity target |

## Standards referenced

| Standard | Used for |
|---|---|
| ISO/IEC/IEEE 29148:2018 | Structure and quality criteria of this specification |
| ISO/IEC 25010 | Classification of quality requirements |
| SIRI (SX, ET) | IF-06 real-time exchange |
| NeTEx | IF-02 master data import |
| VDV 453 | IF-01 ITCS subscription |
| OIDC | IF-08 staff authentication |
| WCAG 2.1 AA | Accessibility target level for digital channels |

## Compliance evidence plan

| Requirement source | Evidence produced | When | Filed with |
|---|---|---|---|
| Concession / FOT finding | Conformance suite result, availability report | Before go-live, then monthly | STK-09 |
| Accessibility | External audit report, screen-reader test protocol | Before go-live | STK-15, canton |
| Data protection | DPIA, deletion job evidence, schema inspection | Before go-live, annually | STK-11 |
| Works agreement | Schema inspection sign-off | Before go-live | STK-13 |
| Procurement | Vendor-neutrality review of the tender specification | Before tender | Procurement |
