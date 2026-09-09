# AI-Powered PCAP Analysis & Threat Detection

[![Project Status](https://img.shields.io/badge/Project-Completed-brightgreen)](https://github.com/surajs-sudo/PCAP-Threat-Detection-Using-Generative-AI)
[![Cybersecurity](https://img.shields.io/badge/Domain-Cybersecurity-red)](https://github.com/surajs-sudo/PCAP-Threat-Detection-Using-Generative-AI)
[![Network Security](https://img.shields.io/badge/Focus-Network%20Security-blue)](https://github.com/surajs-sudo/PCAP-Threat-Detection-Using-Generative-AI)
[![Generative AI](https://img.shields.io/badge/AI-Generative%20AI-purple)](https://github.com/surajs-sudo/PCAP-Threat-Detection-Using-Generative-AI)
[![Wireshark](https://img.shields.io/badge/Tool-Wireshark-blue)](https://www.wireshark.org/)
[![TShark](https://img.shields.io/badge/Tool-TShark-lightgrey)](https://www.wireshark.org/docs/man-pages/tshark.html)
[![Python](https://img.shields.io/badge/Language-Python-yellow)](https://www.python.org/)
[![GitHub](https://img.shields.io/badge/Platform-GitHub-black)](https://github.com/)

Hands-on cybersecurity capstone project focused on PCAP analysis, network traffic investigation, threat detection, visualization, incident response, and AI-assisted security analysis.

## Project Overview

This project demonstrates a hands-on Security Operations Center (SOC) workflow for investigating suspicious network traffic captured in a PCAP file.

The investigation uses Wireshark, TShark, CSV-based analysis, Python-assisted data preparation, visualization, detection rules, and Generative AI to examine network activity and identify traffic patterns that require further security investigation.

The project follows a complete investigation lifecycle:

**PCAP Capture → Data Extraction → AI-Assisted Analysis → Detection → Visualization → Incident Response → Security Assessment**

The analysis was performed on the `2021-08-16-formbook.pcap` network capture and resulted in a structured investigation of **3,588 network traffic records**.

The investigation focused on identifying:

- Frequently communicating hosts
- Internal, public, broadcast, and multicast addresses
- Repeated communication patterns
- Frequently used network ports
- External network communication
- Unencrypted HTTP traffic
- DNS traffic anomalies
- Unusual frame sizes
- Traffic bursts and timeline patterns
- Indicators requiring further investigation
- Appropriate incident response actions

The project emphasizes an important cybersecurity principle:

> **Unusual network activity does not automatically mean confirmed malicious activity.**

Therefore, the findings were treated as **investigation-relevant indicators** rather than automatically classified as confirmed malware, Command and Control (C2), data exfiltration, or system compromise.

## Project Objectives

The main objectives of this project were to:

- Convert PCAP network capture data into a structured CSV dataset using TShark.
- Validate the extracted network traffic data using Wireshark and spreadsheet-based analysis.
- Analyze network traffic using Generative AI to identify potentially suspicious patterns.
- Identify the most frequently communicating source and destination IP addresses.
- Classify internal, public, broadcast, and multicast IP addresses.
- Investigate frequently used TCP and UDP ports.
- Identify repeated communication patterns and traffic bursts.
- Examine external network communication involving the internal workstation.
- Detect unencrypted HTTP communication that may require security review.
- Investigate unusual frame-size observations using statistical analysis.
- Develop detection rules based on investigation-relevant network behaviors.
- Create visualizations to make traffic patterns and security findings easier to understand.
- Develop an incident response strategy covering containment, eradication, recovery, validation, and monitoring.
- Evaluate the usefulness and limitations of Generative AI in cybersecurity investigations.
- Apply analyst verification before treating AI-generated observations as security conclusions.
- Produce a complete evidence-based security assessment and final project documentation.

## Investigation Workflow

The project followed a structured network security investigation workflow from raw PCAP data to incident response recommendations.

```text
PCAP Capture
     ↓
Wireshark Validation
     ↓
TShark Data Extraction
     ↓
CSV Dataset Preparation
     ↓
AI-Assisted Traffic Analysis
     ↓
Traffic Segmentation & Combination
     ↓
Detection Rules
     ↓
Statistical Analysis
     ↓
Network Traffic Visualization
     ↓
Timeline Analysis
     ↓
Incident Response Planning
     ↓
Final Security Assessment
```

### Phase 1 — PCAP Conversion

The original PCAP capture was examined and validated using Wireshark.

TShark was then used to extract relevant packet metadata into a structured CSV format for further analysis.

The resulting dataset provided a structured representation of the network traffic that could be analyzed using spreadsheet tools, Python, and Generative AI.

### Phase 2 — AI-Assisted Threat Analysis

The extracted network traffic was divided into manageable segments and analyzed using Generative AI.

The analysis focused on:

- Communication frequency
- Source and destination IP addresses
- Internal and external communication
- Network ports
- Repeated communication patterns
- Potential automated activity
- DNS traffic
- HTTP traffic
- Unusual traffic characteristics

The AI-assisted analysis helped identify traffic patterns and investigation areas that required deeper validation.

### Phase 3 — Detection & Visualization

The traffic segments were combined into a complete dataset containing 3,588 network traffic records.

Detection rules were developed based on investigation-relevant network behaviors.

Statistical analysis and visualizations were used to examine:

- Protocol distribution
- Top communicating hosts
- Destination port usage
- External communication
- Frame-size characteristics
- Traffic bursts
- Timeline patterns

The visualizations helped present complex network traffic findings in a clearer and more understandable format.

### Phase 4 — Incident Response

The investigation findings were translated into an incident response strategy covering the following lifecycle:

**ISOLATE → INVESTIGATE → REMEDIATE → VALIDATE → RECONNECT → MONITOR**

The response plan included:

- Immediate containment actions
- Investigation and validation
- Containment and eradication
- Recovery activities
- Validation before reconnecting the affected system
- Post-recovery monitoring
- Lessons learned

The response strategy was designed around the available evidence rather than assuming that unusual traffic represented confirmed compromise.

### Phase 5 — Final Security Assessment

The final assessment classified the observed activity as:

**INVESTIGATION REQUIRED**

The analysis identified several investigation-relevant network behaviors, including external communication, frequently used ports, HTTP traffic, DNS activity, traffic bursts, and unusual frame-size observations.

However, the available PCAP metadata alone did not provide sufficient evidence to confirm:

- Malware execution
- Command and Control (C2)
- Data exfiltration
- DNS tunneling
- System compromise

Additional endpoint, application, DNS, proxy, firewall, and security monitoring evidence would be required to confirm malicious activity.

**Final Assessment: Investigation Required — No Confirmed Compromise**

## Milestone 1 — PCAP Conversion & Data Preparation

Milestone 1 focused on converting the raw PCAP network capture into a structured dataset suitable for security analysis.

The original network capture was validated using Wireshark and then processed using TShark to extract packet-level metadata into CSV format.

The extracted data was subsequently validated using spreadsheet-based analysis to ensure that the conversion produced a usable and consistent dataset.

### Key Activities

- Examined the original PCAP capture using Wireshark.
- Validated the captured network traffic and protocol information.
- Used TShark to extract packet metadata.
- Converted the PCAP data into CSV format.
- Reviewed the extracted dataset using spreadsheet analysis.
- Verified the structure and consistency of the extracted traffic data.
- Prepared the dataset for AI-assisted investigation in Milestone 2.

### Dataset Summary

| Metric | Result |
|---|---:|
| Total Records | 3,588 |
| Capture Duration | 610.400 seconds |
| Approximate Duration | 10 minutes 10 seconds |
| Primary Dataset | `formbook_traffic.csv` |
| Validation Workbook | `formbook_traffic_validation.xlsx` |
| Primary Extraction Tool | TShark |
| Validation Tool | Wireshark |

### Milestone 1 Outcome

The raw PCAP capture was successfully converted into a structured CSV dataset containing 3,588 network traffic records.

This structured dataset became the foundation for the subsequent AI-assisted threat analysis, detection, visualization, and incident response activities.

## Milestone 2 — AI-Assisted Threat Analysis

Milestone 2 focused on using Generative AI to assist with the investigation of the structured network traffic dataset.

The complete traffic data was divided into three manageable segments and analyzed separately. The AI-assisted analysis was used to identify communication patterns, frequently communicating hosts, external connections, unusual ports, repeated traffic, and other behaviors requiring further investigation.

### Traffic Segmentation

The 3,588-record dataset was divided into three traffic segments for analysis:

| Segment | Records |
|---|---:|
| Segment 1 | 1,200 |
| Segment 2 | 1,200 |
| Segment 3 | 1,188 |
| **Total** | **3,588** |

The three segments were analyzed independently and later combined for complete dataset analysis in Milestone 3.

### AI-Assisted Investigation Areas

The AI-assisted analysis focused on:

- Identifying the most frequently communicating source and destination IP addresses.
- Classifying internal and external IP addresses.
- Identifying repeated communication patterns.
- Examining potential automated or periodic communication.
- Investigating frequently used network ports.
- Examining external network communication.
- Identifying potentially unusual traffic behavior.
- Reviewing DNS and HTTP communication.
- Highlighting traffic patterns that required deeper validation.

### Important Investigation Finding

The analysis identified `10.10.0.33` as the primary internal workstation involved in the observed network communication.

A dominant communication relationship was observed between:

`10.10.0.33` and `18.184.26.60`

The two-way communication between these addresses accounted for 1,725 records, representing approximately 48.08% of the complete 3,588-record dataset.

### AI Verification

Generative AI was used as an analytical aid rather than as the final authority for security conclusions.

AI-generated observations were reviewed against the underlying network traffic data and supporting statistical analysis.

This verification step was important because repeated communication, large frames, unusual ports, or external connections do not automatically indicate malicious activity.

The final security assessment therefore remained evidence-based and analyst-verified.

### Milestone 2 Outcome

The AI-assisted investigation identified several network behaviors and communication patterns that required deeper analysis.

The findings from the three traffic segments provided the basis for the complete dataset analysis, detection rules, statistical analysis, visualizations, and timeline investigation performed during Milestone 3.

## Milestone 3 — Detection & Visualization

Milestone 3 focused on transforming the results of the AI-assisted traffic investigation into structured detection rules, statistical analysis, visualizations, and timeline-based investigation.

The three Milestone 2 traffic segments were combined into a complete dataset containing 3,588 records. The resulting dataset was then analyzed to identify communication patterns, protocol distribution, port usage, external communication, frame-size characteristics, and traffic activity over time.

### Dataset Combination

The three traffic segments from Milestone 2 were combined using Python into a single dataset.

| Dataset | Records |
|---|---:|
| `traffic_segment_1.csv` | 1,200 |
| `traffic_segment_2.csv` | 1,200 |
| `traffic_segment_3.csv` | 1,188 |
| **Combined Dataset** | **3,588** |

The combined dataset was used as the primary source for the Milestone 3 statistical analysis and visualizations.

### Detection Rules

Five investigation-focused detection rules were developed:

1. **Possible Automated External Communication Detection**
2. **Unencrypted HTTP Communication Monitoring**
3. **Unusual Data Transfer Volume Detection**
4. **DNS Traffic Anomaly Detection**
5. **New External Communication Monitoring**

These rules were designed to identify behaviors that may require investigation.

The rules were not treated as proof of malicious activity. Appropriate validation and additional evidence would be required before confirming a security incident.

### Network Traffic Analysis

The Milestone 3 analysis examined several important characteristics of the network traffic:

- Protocol distribution
- Source and destination communication
- Top communicating hosts
- Destination port usage
- Internal and external communication
- DNS activity
- HTTP communication
- Frame-size distribution
- Traffic bursts
- Timeline activity

The analysis combined numerical statistics with visual representations to make the network behavior easier to interpret.

### Milestone 3 Outcome

Milestone 3 produced a structured set of detection rules, statistical findings, network traffic visualizations, and timeline analysis.

The results provided the evidence base used for the incident response planning and final security assessment completed during Milestone 4.

## Milestone 4 — Incident Response & Final Presentation

Milestone 4 focused on translating the network investigation findings into an incident response strategy and presenting the complete investigation in a structured final format.

The milestone included an Incident Response Action Plan, Final Presentation, Reflection Summary, and supporting evidence and visual materials.

### Incident Response Action Plan

The Incident Response Action Plan documented the recommended response to the investigation-relevant network activity.

The response lifecycle followed:

**ISOLATE → INVESTIGATE → REMEDIATE → VALIDATE → RECONNECT → MONITOR**

The plan covered:

- Immediate containment actions
- External communication validation
- Investigation and evidence collection
- Containment and eradication
- System recovery
- Validation before reconnection
- Post-recovery monitoring
- Lessons learned
- Recommendations for improving future investigations

### Final Presentation

The final presentation summarized the complete project and communicated the major investigation findings.

The presentation covered:

- Investigation overview
- Investigation workflow
- Key network traffic findings
- Investigation-relevant indicators
- Detection rules
- AI-assisted analysis
- Incident response strategy
- Final security assessment
- Lessons learned and conclusion

### Reflection Summary

The Reflection Summary documented the key lessons learned throughout the project.

The project demonstrated that:

- PCAP data can initially be difficult to interpret without a structured workflow.
- Data validation is critical before drawing security conclusions.
- Generative AI can accelerate network traffic analysis.
- AI-generated findings must be verified against the underlying evidence.
- Repeated or unusual traffic does not automatically indicate malicious activity.
- Visualization can make complex network behavior easier to understand.
- Network metadata alone may not be sufficient to confirm compromise.

### Final Assessment

The investigation identified multiple network behaviors that require further security investigation.

However, the available PCAP metadata did not provide sufficient evidence to confirm malware execution, Command and Control (C2), data exfiltration, DNS tunneling, or system compromise.

**Final Classification: Investigation Required**

**Confirmed Compromise: No**

### Milestone 4 Outcome

Milestone 4 completed the project lifecycle by connecting technical network analysis with incident response, security recommendations, presentation, and reflection.

The final project therefore demonstrates an end-to-end approach to AI-assisted PCAP investigation and threat detection.

## Key Investigation Findings

The complete analysis of the 3,588-record network traffic dataset identified several significant communication patterns and investigation-relevant indicators.

The findings below summarize the main observations from the network traffic, statistical analysis, and timeline investigation.

### Dataset & Communication Overview

| Finding | Result |
|---|---:|
| Total Network Records | 3,588 |
| IP-Bearing Records | 3,549 |
| Non-IP / ARP Records | 39 |
| Capture Duration | 610.400 seconds |
| Primary Internal Host | `10.10.0.33` |
| Dominant External IP | `18.184.26.60` |

### Dominant Communication Relationship

The most significant communication relationship observed in the dataset was:

`10.10.0.33 ↔ 18.184.26.60`

The traffic consisted of:

- `10.10.0.33 → 18.184.26.60` — 877 records
- `18.184.26.60 → 10.10.0.33` — 848 records
- Combined communication — 1,725 records

This represented approximately **48.08% of all 3,588 network records**.

This dominant relationship was therefore identified as a primary area for further investigation.

### Internal & External Communication

The analysis identified the following communication categories:

- Internal-to-public-unicast communication: **1,785 records**
- Public-unicast-to-internal communication: **1,740 records**
- Combined internal-to-public-unicast communication: **3,525 records**

This represented approximately **98.24% of all network records**.

Among IP-bearing records, internal-to-public-unicast communication represented approximately **99.32%** of the traffic.

### Special Network Addresses

Two non-unicast communication patterns were also identified:

- `10.10.0.255` — local broadcast address associated with NBNS traffic.
- `239.255.255.250` — multicast address associated with SSDP traffic.

These were treated as normal broadcast/multicast categories rather than public Internet destinations.

### Key Investigation Areas

The following areas were identified as requiring additional security review:

- Communication involving `10.10.0.33`.
- High-volume communication with `18.184.26.60`.
- TCP destination port `53480`.
- Unencrypted HTTP communication.
- DNS traffic and unusually large DNS-related frames.
- Traffic bursts within the capture timeline.
- Statistical frame-size outliers.
- Repeated external communication patterns.

These observations were considered **investigation-relevant indicators**, not confirmed evidence of malicious activity.

### Important Security Interpretation

The observed traffic patterns provide useful investigation leads, but network metadata alone is not sufficient to confirm malicious activity.

In particular, the investigation did not confirm:

- Malware execution
- Command and Control (C2)
- Data exfiltration
- DNS tunneling
- System compromise

Additional endpoint and security telemetry would be required to establish a confirmed security incident.

## Detailed Network Traffic Analysis

The complete 3,588-record dataset was examined using protocol classification, port analysis, IP communication analysis, and statistical investigation.

The following observations represent the main technical findings from the Milestone 3 analysis.

### Protocol Distribution

The traffic was classified using the following protocol precedence:

**HTTP → TLS → DNS → NBNS → SSDP → ARP → Remaining TCP**

The resulting protocol distribution was:

| Protocol | Records | Percentage |
|---|---:|---:|
| TCP | 3,093 | 86.20% |
| TLS | 201 | 5.60% |
| HTTP | 119 | 3.32% |
| DNS | 112 | 3.12% |
| ARP | 39 | 1.09% |
| NBNS | 16 | 0.45% |
| SSDP | 8 | 0.22% |
| **Total** | **3,588** | **100%** |

### Destination Port Usage

The most frequently observed destination ports were:

| Destination Port | Records | Percentage |
|---|---:|---:|
| TCP/80 | 1,221 | 34.03% |
| TCP/53480 | 804 | 22.41% |
| TCP/443 | 506 | 14.10% |
| TCP/53483 | 181 | 5.04% |
| UDP/53 | 58 | 1.62% |

The high frequency of TCP/80 and TCP/53480 communication was identified as an important investigation area.

### TCP/53480 Investigation

TCP destination port `53480` was one of the most frequently observed destination ports.

All **804 of 804** destination-port-53480 records followed the same communication pattern:

`18.184.26.60:80 → 10.10.0.33:53480`

This means the traffic consistently represented communication from source port `80` on `18.184.26.60` to destination port `53480` on the internal workstation.

The consistency of this communication pattern made TCP/53480 an important indicator for further investigation.

### HTTP Traffic Observation

The analysis identified **119 records classified as HTTP**.

It is important to distinguish this value from the total TCP/80 count:

- TCP/80 traffic: **1,221 records**
- HTTP-decoded traffic: **119 records**

Therefore, TCP destination port 80 was not treated as equivalent to confirmed HTTP application-layer traffic.

The unencrypted HTTP records were included as an investigation-relevant security observation.

### DNS Traffic Observation

The analysis identified **112 DNS records**.

Four records contained `frame.protocols = "53"` while also using UDP destination port 53 and were therefore classified as DNS based on the traffic characteristics.

The DNS analysis also identified unusually large captured frames associated with:

`10.10.0.33 → 8.8.8.8`

These observations required validation rather than being automatically classified as DNS tunneling or data exfiltration.

### Frame Size Analysis

Statistical analysis of captured frame lengths produced the following results:

| Metric | Value |
|---|---:|
| Minimum | 42 bytes |
| Q1 | 60 bytes |
| Median | 66 bytes |
| Mean | 672.06 bytes |
| Q3 | 1,514 bytes |
| IQR | 1,454 bytes |
| Maximum | 58,337 bytes |
| Upper IQR Threshold | 3,695 bytes |

Four statistical outliers exceeded the upper IQR threshold.

All four were DNS-related frames from:

`10.10.0.33 → 8.8.8.8`

with UDP/53 communication.

The outliers were treated as **statistical anomalies requiring further validation**. They were not classified as confirmed exfiltration, DNS tunneling, or malicious traffic based solely on frame size.

## Timeline Analysis & Traffic Activity

Timeline analysis was performed to understand how network activity was distributed throughout the PCAP capture.

The capture lasted approximately **10 minutes and 10 seconds**, with significant variation in traffic volume across the one-minute intervals.

### Capture Timeline

| Metric | Result |
|---|---:|
| Start | `2021-08-17 01:58:06.017228 +0530` |
| End | `2021-08-17 02:08:16.417023 +0530` |
| Duration | `610.399795 seconds` |
| Approximate Duration | `10 minutes 10.40 seconds` |
| Total Records | `3,588` |
| Average Capture Rate | `352.69 records/minute` |

### Traffic Distribution Over Time

The one-minute traffic distribution was:

| Time Interval | Records |
|---|---:|
| 01:58–01:59 | 696 |
| 01:59–02:00 | 2,097 |
| 02:00–02:01 | 54 |
| 02:01–02:02 | 82 |
| 02:02–02:03 | 113 |
| 02:03–02:04 | 68 |
| 02:04–02:05 | 104 |
| 02:05–02:06 | 81 |
| 02:06–02:07 | 103 |
| 02:07–02:08 | 150 |
| 02:08–02:09 | 40 |
| **Total** | **3,588** |

### Peak Traffic Period

The highest traffic volume occurred during the **01:59–02:00** interval.

During this one-minute period:

- **2,097 records** were observed.
- This represented approximately **58.44% of the complete dataset**.

The large concentration of traffic within this period was identified as an investigation-relevant traffic burst.

### Beaconing Assessment

Repeated communication patterns were reviewed to determine whether the traffic demonstrated characteristics of automated or periodic communication.

The observed traffic contained repeated external communication and activity bursts; however, the available analysis did not provide sufficient evidence to confirm a consistent beaconing pattern.

Therefore:

**Beaconing: Low Confidence / Not Confirmed**

Additional packet timing analysis, endpoint telemetry, process information, and longer-duration traffic captures would be useful for confirming or rejecting a potential beaconing behavior.

### Timeline Investigation Conclusion

The timeline analysis demonstrated that network activity was highly concentrated during a short period of the capture.

The traffic burst was considered relevant for further investigation, but traffic volume and concentration alone were not treated as proof of malicious activity.

The timeline findings were therefore incorporated into the detection rules and incident response recommendations.

## Detection Rules & Security Monitoring

Based on the network traffic investigation, five detection rules were developed to help identify behaviors that may require additional security investigation.

The rules are designed as investigation and monitoring controls rather than automatic proof of malicious activity.

### Rule 1 — Possible Automated External Communication Detection

**Purpose:** Identify repeated communication between an internal workstation and an external destination that may indicate automated network activity.

**Investigation Focus:**

- Repeated external connections
- High-frequency communication
- Consistent source and destination relationships
- Potential periodic communication

**Validation:** Review connection timing, destination reputation, endpoint processes, and longer-duration traffic.

**Assessment:** Investigation-relevant; automated activity was not confirmed.

### Rule 2 — Unencrypted HTTP Communication Monitoring

**Purpose:** Identify unencrypted HTTP communication that may expose traffic to interception or indicate legacy or insecure application behavior.

**Investigation Focus:**

- TCP/80 communication
- HTTP-decoded traffic
- External HTTP destinations

**Validation:** Examine HTTP requests, hosts, URLs, payloads, and the application or process generating the traffic.

**Assessment:** Investigation-relevant; HTTP traffic alone does not confirm malicious activity.

### Rule 3 — Unusual Data Transfer Volume Detection

**Purpose:** Identify unusually large captured frames or traffic volumes that may require additional investigation.

**Investigation Focus:**

- Large frame sizes
- Traffic bursts
- Unusual transfer patterns
- Statistical outliers

**Validation:** Determine whether the observed frame size represents legitimate application traffic, protocol behavior, or an actual data transfer.

**Assessment:** Statistical anomalies were identified, but data exfiltration was not confirmed.

### Rule 4 — DNS Traffic Anomaly Detection

**Purpose:** Identify unusual DNS traffic that may require further analysis.

**Investigation Focus:**

- DNS traffic volume
- Large DNS-related frames
- Repeated DNS communication
- Unusual DNS destinations

**Validation:** Examine DNS queries and responses, domain characteristics, query frequency, and endpoint context.

**Assessment:** Four unusually large DNS-related frames were identified, but DNS tunneling or malicious DNS activity was not confirmed.

### Rule 5 — New External Communication Monitoring

**Purpose:** Identify internal systems communicating with external destinations that may not normally be expected.

**Investigation Focus:**

- Internal-to-public communication
- New external destinations
- High-frequency external relationships
- Destination reputation and ownership

**Validation:** Compare against known business services, approved destinations, DNS records, proxy logs, firewall logs, and endpoint telemetry.

**Assessment:** External communication was extensive in the capture and therefore represents an important investigation area.

### Detection Rule Philosophy

The detection rules were intentionally designed to generate investigation leads rather than automatically classify traffic as malicious.

This approach reduces the risk of false positives and supports an analyst-driven investigation process.

**Detection → Investigation → Validation → Security Decision**

## Incident Response Strategy

The network investigation findings were translated into an incident response strategy designed to provide a structured approach for handling the investigation-relevant activity.

The response process follows six stages:

**ISOLATE → INVESTIGATE → REMEDIATE → VALIDATE → RECONNECT → MONITOR**

### Immediate Containment

The recommended immediate actions include:

- Isolate the affected workstation from the network.
- Preserve relevant network and endpoint evidence.
- Record active network connections and system state.
- Prevent unnecessary communication with suspicious or investigation-relevant destinations.
- Avoid destroying or modifying evidence before collection.
- Escalate the investigation to the appropriate security team.

### Investigation & Validation

After containment, the investigation should validate the observed network indicators using additional evidence.

Recommended sources include:

- Endpoint process and application information
- DNS logs
- Firewall logs
- Proxy logs
- Authentication logs
- EDR or security monitoring telemetry
- Network connection history
- Destination reputation and ownership information

The purpose is to determine whether the observed network behavior was legitimate, automated, suspicious, or malicious.

### Eradication & Recovery

If additional evidence confirms malicious activity, appropriate remediation should be performed.

Potential actions include:

- Remove identified malicious artifacts.
- Remediate affected applications or configurations.
- Reset compromised credentials where necessary.
- Apply required security patches.
- Verify system integrity.
- Restore the workstation to a trusted state.
- Revalidate security controls before reconnecting the system.

### Reconnection & Monitoring

The affected system should only be reconnected after validation confirms that the required remediation activities have been completed.

Post-recovery monitoring should focus on:

- Repeated external communication
- Unexpected destinations
- Unusual ports
- DNS anomalies
- HTTP activity
- Traffic bursts
- Endpoint processes associated with network connections

The incident response plan recommends continued monitoring for at least **30 days** after recovery.

### Incident Response Decision

Based on the available PCAP evidence, the recommended classification is:

**INVESTIGATION REQUIRED**

There was not sufficient evidence from the network metadata alone to declare a confirmed compromise.

Therefore, the appropriate response is to preserve evidence, investigate further, validate the indicators, and avoid making an unsupported conclusion.

