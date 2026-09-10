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

## AI-Assisted Investigation & Verification

Generative AI was used throughout the project as an analytical assistant to help examine network traffic, identify patterns, organize findings, and support the development of investigation-focused detection rules.

The AI-assisted approach helped reduce the time required to review large amounts of network traffic and provided additional perspectives for identifying areas that required deeper investigation.

### How AI Was Used

Generative AI assisted with:

- Reviewing structured network traffic data.
- Identifying frequently communicating IP addresses.
- Classifying internal and external communication.
- Examining repeated communication patterns.
- Investigating frequently used network ports.
- Highlighting potentially unusual traffic behavior.
- Reviewing DNS and HTTP activity.
- Interpreting statistical findings.
- Supporting detection rule development.
- Organizing investigation findings.
- Supporting incident response planning.
- Helping structure the final security assessment.

### AI and Analyst Verification

AI-generated observations were not treated as final security conclusions.

Important findings were checked against the underlying dataset, calculated statistics, protocol information, and traffic relationships.

This verification was especially important for observations involving:

- Repeated communication
- External destinations
- High-volume traffic
- Unusual ports
- Large frame sizes
- DNS activity
- Potential automated communication

### Limitations of AI-Assisted Analysis

Generative AI can help identify patterns quickly, but it cannot independently establish that a network behavior is malicious without sufficient supporting evidence.

For this investigation, unusual traffic patterns were therefore treated as investigation leads rather than automatically classified as:

- Confirmed malware
- Command and Control (C2)
- Data exfiltration
- DNS tunneling
- System compromise

### AI Investigation Principle

The project followed the principle:

**AI assists the investigation — the analyst validates the evidence and makes the final security decision.**

This approach combines the speed and analytical capabilities of Generative AI with evidence-based cybersecurity investigation.

## Tools & Technologies

The project used a combination of network analysis, command-line, data analysis, visualization, Generative AI, and documentation tools.

| Tool / Technology | Purpose |
|---|---|
| **Wireshark** | PCAP inspection, protocol validation, and network traffic analysis |
| **TShark** | Command-line PCAP processing and packet metadata extraction |
| **Python** | Traffic dataset preparation and segment combination |
| **Microsoft Excel** | Dataset validation, filtering, and statistical review |
| **Generative AI** | AI-assisted traffic investigation, pattern identification, and analysis support |
| **GitHub** | Project version control, documentation, and portfolio publication |
| **Markdown** | Project documentation and README creation |

### Technology Workflow

The main technologies were used at different stages of the investigation:

**Wireshark → TShark → CSV → Python/Pandas → Generative AI → Statistical Analysis → Visualization → Detection Rules → Incident Response**

### Important Note

Python was primarily used for data preparation and combining the three Milestone 2 traffic segments into the complete 3,588-record dataset.

The project also used statistical analysis and visualization techniques to support the interpretation of the network traffic.

## Repository Structure

The repository is organized by milestone to keep the investigation workflow, evidence, analysis outputs, and final deliverables clearly separated.

```text
PCAP-Threat-Detection-Using-Generative-AI/
│
├── Milestone_1_PCAP_Conversion/
│   ├── 01_Converted_Data/
│   ├── 02_PCAP_File/
│   ├── 03_Report_Documentation/
│   └── 04_Screenshots/
│
├── Milestone_2_AI-Assisted_Threat_Analysis/
│   ├── 01_AI_Analysis_Data/
│   ├── 02_AI_Prompts_and_Responses/
│   ├── 03_Attack_Timeline/
│   ├── 04_Report_Documentation/
│   └── 05_Screenshots/
│
├── Milestone_3_Detection_and_Visualization/
│   ├── 01_Detection_Rules/
│   ├── 02_Network_Traffic_Visualization_Report/
│   ├── 03_AI_Generated_Visuals/
│   ├── 04_Screenshots/
│   ├── 05_Source_Data/
│   ├── 06_Python_Script/
│   └── 07_Timeline_Analysis_Report/
│
├── Milestone_4_Incident_Response_and_Final_Presentation/
│   ├── 01_Incident_Response_Action_Plan/
│   ├── 02_Final_Presentation/
│   └── 03_Reflection_Summary/
│ 
│
└── README.md
```


### Repository Organization

Each milestone contains the documentation and supporting artifacts produced during that stage of the project.

This structure makes it possible to follow the investigation from the original PCAP conversion through AI-assisted analysis, detection and visualization, and finally incident response and project reflection.

### Milestone Folder Purpose

| Folder | Purpose |
|---|---|
| `Milestone_1_PCAP_Conversion` | PCAP validation, TShark extraction, and dataset preparation |
| `Milestone_2_AI-Assisted_Threat_Analysis` | Segmented traffic analysis and AI-assisted investigation |
| `Milestone_3_Detection_and_Visualization` | Detection rules, statistics, visualizations, and timeline analysis |
| `Milestone_4_Incident_Response_and_Final_Presentation` | Incident response, final presentation, reflection, and evidence |

## Project Deliverables

The project produced the following technical documentation, datasets, analysis reports, detection rules, visualizations, incident response documentation, and final presentation materials.

| Milestone | Deliverable | Purpose |
|---|---|---|
| Milestone 1 | PCAP Conversion Documentation | Documents the PCAP validation and TShark conversion process |
| Milestone 1 | Sample CSV Dataset | Provides structured network traffic data extracted from the PCAP |
| Milestone 1 | Validation Workbook | Supports validation and review of the extracted dataset |
| Milestone 2 | AI-Assisted Analysis Reports | Documents the AI-assisted investigation of the traffic segments |
| Milestone 2 | Traffic Segments | Contains the three segmented network traffic datasets |
| Milestone 3 | Detection Rules Report | Documents investigation-focused network detection rules |
| Milestone 3 | Network Traffic Visualization Report | Documents statistical analysis and network traffic visualizations |
| Milestone 3 | AI-Generated Visuals | Provides visual representations of investigation findings |
| Milestone 3 | Timeline Analysis Report | Documents traffic activity and timeline-based investigation |
| Milestone 3 | Combined Traffic Dataset | Contains the complete 3,588-record dataset |
| Milestone 3 | Python Data Combination Script | Combines the three Milestone 2 traffic segments |
| Milestone 4 | Incident Response Action Plan | Documents containment, remediation, recovery, and monitoring recommendations |
| Milestone 4 | Final Presentation | Summarizes the complete investigation and security findings |
| Milestone 4 | Reflection Summary | Documents lessons learned and the role of Generative AI |
| Milestone 4 | Evidence & Visuals | Provides supporting evidence collected throughout the project |

### Final Project Package

The repository brings together the complete project lifecycle:

**PCAP Data → Analysis → Detection → Visualization → Incident Response → Final Assessment**

All major project artifacts are organized within their respective milestone directories for easier review and reference.

## Security Concepts Demonstrated

This project demonstrates several practical cybersecurity and network security concepts through hands-on investigation.

- **PCAP Analysis** — Examining captured network traffic to understand host and protocol behavior.
- **Network Traffic Analysis** — Investigating communication patterns, ports, protocols, and traffic volume.
- **IP Address Classification** — Distinguishing internal, public, broadcast, and multicast addresses.
- **Protocol Analysis** — Identifying and categorizing TCP, TLS, HTTP, DNS, NBNS, SSDP, and ARP traffic.
- **Port Analysis** — Investigating frequently used TCP and UDP ports and their communication relationships.
- **External Communication Analysis** — Identifying communication between the internal workstation and public network destinations.
- **Anomaly Detection** — Using statistical and behavioral observations to identify traffic requiring further investigation.
- **Beaconing Analysis** — Reviewing repeated communication patterns for possible automated or periodic activity.
- **DNS Analysis** — Investigating DNS communication and unusual DNS-related frame sizes.
- **Traffic Timeline Analysis** — Examining how network activity changed throughout the capture period.
- **Detection Engineering** — Developing investigation-focused detection rules from observed network behaviors.
- **Security Visualization** — Using visual analysis to communicate network traffic patterns and findings.
- **Incident Response** — Applying containment, investigation, remediation, recovery, validation, and monitoring concepts.
- **Generative AI in Cybersecurity** — Using AI to accelerate traffic analysis and organize investigation findings.
- **Analyst Verification** — Validating AI-generated observations against the underlying evidence before making security decisions.
- **Evidence-Based Security Assessment** — Distinguishing investigation-relevant indicators from confirmed malicious activity.

## Learning Outcomes

This project provided practical experience in:

- Working with real network packet capture data.
- Using Wireshark to inspect and validate network traffic.
- Using TShark to extract structured packet metadata.
- Preparing and validating network traffic datasets.
- Using Python and Pandas for traffic data preparation.
- Applying Generative AI to assist with cybersecurity analysis.
- Investigating IP addresses, protocols, ports, and communication patterns.
- Using statistical analysis to identify unusual traffic characteristics.
- Creating security-focused visualizations.
- Developing investigation-oriented detection rules.
- Performing timeline-based network traffic analysis.
- Translating technical findings into incident response actions.
- Evaluating AI-generated findings through analyst verification.
- Understanding the difference between an investigation indicator and confirmed malicious activity.
- Communicating technical security findings through reports and presentations.
- Applying an evidence-based approach to cybersecurity investigations.

The project strengthened the ability to combine traditional network security analysis with modern Generative AI-assisted investigation techniques.

## Final Security Assessment

The investigation identified multiple network behaviors that warranted additional security review, including:

- High-volume communication involving the internal workstation `10.10.0.33`.
- Significant communication with `18.184.26.60`.
- Frequent TCP/80 traffic.
- Repeated communication through TCP destination port `53480`.
- External network communication.
- Unencrypted HTTP traffic.
- DNS activity requiring additional validation.
- Four unusually large DNS-related frame-size observations.
- A significant traffic burst during the capture timeline.
- Repeated communication patterns that were reviewed for possible automated activity.

These findings were treated as **investigation-relevant indicators** rather than confirmed malicious activity.

Based on the available PCAP metadata, the investigation did not provide sufficient evidence to confirm:

- Malware execution
- Command and Control (C2)
- Data exfiltration
- DNS tunneling
- System compromise

Additional endpoint, DNS, firewall, proxy, EDR, application, and authentication evidence would be required to make a definitive determination.

### Final Classification

**INVESTIGATION REQUIRED**

**Confirmed Compromise: No**

The appropriate security response is therefore to preserve the evidence, investigate the identified indicators, validate the activity using additional telemetry, and apply containment or remediation if further evidence confirms malicious behavior.

## Final Takeaway

This project demonstrated how a structured cybersecurity investigation can combine traditional network analysis techniques with Generative AI to investigate suspicious PCAP traffic efficiently.

The investigation showed that AI can help an analyst:

- Process and interpret large amounts of structured traffic data.
- Identify important communication patterns.
- Highlight ports, protocols, and destinations requiring investigation.
- Support statistical and timeline analysis.
- Assist with detection rule development.
- Organize technical findings into actionable security recommendations.

At the same time, the project demonstrated that AI-generated observations must be validated against the underlying evidence.

The investigation therefore followed an evidence-based approach in which unusual network behavior was treated as an investigation lead rather than automatically classified as malicious.

> **AI can accelerate cybersecurity investigation, but analyst verification and additional evidence are required before confirming compromise.**

**Final Takeaway: INVESTIGATION REQUIRED**

## Disclaimer

This project was completed for educational and cybersecurity learning purposes as part of a hands-on capstone project.

The network traffic analyzed in this project was used for security investigation and learning purposes. The findings should not be interpreted as definitive proof of malicious activity without additional supporting evidence.

Any security indicators identified in the analysis should be independently validated using appropriate endpoint, network, application, and security monitoring data before taking production security actions.

## Author

**Suraj Somkuwar**

Cybersecurity | Network Security | Threat Detection | Generative AI

GitHub: [surajs-sudo](https://github.com/surajs-sudo)

---

### Capstone Project 4

**AI-Powered PCAP Analysis & Threat Detection**
