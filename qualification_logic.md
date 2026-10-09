# AI Qualification Logic, System Prompt & Scoring Rules

## 1. System Prompt

```text
You are an enterprise AI Lead Qualification Analyst. Your role is to evaluate inbound and outbound prospects against our Ideal Customer Profile (ICP), diagnose pain points, determine buying intent, and recommend next actions.

STRICT INSTRUCTIONS:
1. Always evaluate context based on target profile: SaaS decision-makers in India, 10–200 employees, experiencing lead qualification bottlenecks.
2. Read the entire conversation history to detect sentiment shifts and buyer interest.
3. Return output strictly in pure JSON format conforming to the required schema.
```

## 2. Structured Output JSON Schema

```json
{
  "qualification_status": "Qualified | Potential | Not Qualified",
  "score": 85,
  "buying_intent": "High | Medium | Low",
  "pain_points": ["manual lead qualification", "slow follow-up delay"],
  "requirements": ["sales automation", "inbound pipeline scoring"],
  "reason": "Matches the target industry and decision-maker profile with 50 employees.",
  "summary": "The prospect is a SaaS founder looking for sales automation to reduce rep workload.",
  "next_action": "Schedule meeting"
}
```

## 3. Transparent 100-Point Scoring Rules

| Criteria | Maximum Points | Scoring Rule |
| :--- | :--- | :--- |
| **Industry Match** | 25 pts | 25 pts for exact SaaS / Software match; 15 pts for adjacent tech; 0 pts for non-tech. |
| **Job Title Match** | 20 pts | 20 pts for Founder, CEO, VP Sales, Head of Growth; 10 pts for Mid-tier managers; 0 pts for non-decision makers. |
| **Location Match** | 15 pts | 15 pts for target geography (India); 10 pts for Global/Remote; 0 pts for non-target region. |
| **Company Size** | 15 pts | 15 pts for sweet spot (10–200 employees); 8 pts for 201–400; 0 pts outside range. |
| **Requirement Match** | 15 pts | 15 pts for >=2 automation keywords; 10 pts for 1 keyword; 0 pts for unrelated needs. |
| **Pain Point Urgency**| 10 pts | 10 pts for high-urgency keywords ('manual', 'slow', 'delay'); 0 pts otherwise. |
| **Total** | **100 pts** | **80–100: Highly Relevant \| 60–79: Potential \| <60: Not Qualified** |

## 4. Buying Intent Logic

- **High Intent**:
  - Prospect mentions volume (>500 leads/mo), requests demo, agrees to schedule, or asks about pricing/implementation.
- **Medium Intent**:
  - Prospect acknowledges pain points and asks how the solution works, but has not yet confirmed readiness.
- **Low Intent**:
  - Prospect shows skepticism, small team (<5 people), no budget, or non-responsive.

## 5. Human Escalation Rules

Automation is automatically paused (`lead_status = "Human Review"`) under the following conditions:
1. **Explicit Request**: Prospect says *"I want to talk to a human"*, *"Can I speak to someone?"*, or *"agent"*.
2. **Out of Scope Inquiries**: Complex contract negotiations, custom legal/security audits.
3. **Hostility/Negative Sentiment**: Prospect requests removal or expresses strong frustration. Outreach stops immediately to protect domain reputation.
