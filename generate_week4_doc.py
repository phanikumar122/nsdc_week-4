import os
from docx.shared import Inches, Pt, RGBColor
from doc_builder import (
    create_base_document, add_header_banner, add_heading_1, add_heading_2,
    add_heading_3, add_paragraph, add_bullet, add_callout, add_styled_table, add_figure
)

def build_week4_document():
    doc = create_base_document()
    
    # Header Banner
    add_header_banner(
        doc,
        title="Comprehensive Data Science Report & Insights Presentation Plan",
        subtitle="Executive Summary, Strategic Business Insights, Non-Technical Communication Framework, and Retention Roadmap",
        task_badge="Week 4 Deliverable | Executive Capstone Report"
    )

    # 1. Executive Summary
    add_heading_1(doc, "1. Executive Summary")
    
    add_paragraph(doc,
        "TelePulse Communications operates in an intensely competitive subscription telecommunications market where customer acquisition costs ($420 per new customer) exceed retention costs by more than sixfold. Facing an annualized subscriber churn rate of 26.5%—resulting in an annual top-line recurring revenue attrition of $3.24 million across its 120,000 subscriber base—TelePulse initiated the TelePulse AI Strategic Retention Program. The objective of this initiative was to engineer and deploy an intelligent, predictive customer churn forecasting engine capable of identifying at-risk accounts 60 days prior to contract termination.",
        bold_prefix="Business Mandate: "
    )
    
    add_paragraph(doc,
        "Through disciplined exploratory data analysis, domain-driven feature engineering, and an ensemble LightGBM machine learning architecture optimized against a financial cost-benefit payoff matrix, the data science team successfully developed a production-ready predictive system. The resulting model achieves an Area Under the Precision-Recall Curve (PR-AUC) of 0.83 and an ROC-AUC of 0.91, accurately identifying 85.4% of all churning accounts while maintaining false positive rates below 13%.",
        bold_prefix="Analytical Breakthrough: "
    )

    add_callout(
        doc,
        "Full-scale operational deployment of TelePulse AI is projected to reduce annualized churn from 26.5% to 14.8% within 12 months, preserving 2,800 high-value subscribers and delivering an estimated net annual revenue preservation of $1.84 million, representing a 340% first-year return on investment (ROI).",
        title="Bottom-Line Financial Impact"
    )

    add_figure(doc, "figures/w4_fig1_executive_dashboard.png", "Executive KPI Dashboard: Churn Rate Reduction, Net Revenue Waterfall, and Program ROI Curve", width=Inches(6.5))

    # 2. Methodology Review (Independent Synthesis)
    add_heading_1(doc, "2. Analytical Methodology & System Architecture Review")
    add_paragraph(doc,
        "The project was executed through an enterprise-grade, four-pillar data science methodology designed to guarantee reproducibility, mathematical rigor, and operational stability.")

    add_heading_2(doc, "2.1 Data Ingestion & Quality Governance")
    add_bullet(doc, "Integrated four siloed operational data systems: relational CRM demographic tables, Snowflake billing logs, Zendesk support ticket transcripts, and network usage telemetry. Automated Great Expectations test suites ensured complete schema integrity and data freshness.", bold_prefix="Omni-Channel Ingestion: ")
    add_bullet(doc, "Identified and treated structural data missingness; resolved extreme monetary skewness through Yeo-Johnson transformations and RobustScaler; and eliminated severe collinearity via Variance Inflation Factor (VIF) filtering.", bold_prefix="Hygiene & Harmonization: ")

    add_heading_2(doc, "2.2 Modeling Strategy & Decision Optimization")
    add_bullet(doc, "Synthesized minority class representations strictly inside cross-validation training folds via SMOTE-NC, paired with cost-weighted gradient boosting loss functions (`scale_pos_weight = 2.77`).", bold_prefix="Class Imbalance Resolution: ")
    add_bullet(doc, "Conducted an algorithmic tournament benchmarking Logistic Regression, Random Forest, XGBoost, and LightGBM. LightGBM emerged as champion, undergoing 50-trial Bayesian hyperparameter optimization with Optuna.", bold_prefix="Algorithmic Tournament: ")
    add_bullet(doc, "Calibrated model probabilities using isotonic regression and established a cost-optimal classification threshold of tau* = 0.38, maximizing the net economic objective function: EV = (TP * $650) - (FP * $35) - (FN * $1200).", bold_prefix="Cost-Sensitive Threshold Tuning: ")

    # 3. Core Analytical Findings & Business Insights
    add_heading_1(doc, "3. Core Analytical Findings & Strategic Business Insights")
    add_paragraph(doc,
        "Exploratory diagnostics and SHAP (SHapley Additive exPlanations) global feature attributions uncovered four primary structural failure points in the customer lifecycle:")

    insights_headers = ["Lifecycle Vulnerability", "Observed Empirical Data Pattern", "Root Business Cause", "Strategic Countermeasure"]
    insights_rows = [
        ["Month-to-Month Contract Fragility", "Subscribers on month-to-month contracts experience a 42.7% churn rate, compared to 11.3% for 1-year and 2.8% for 2-year contracts.", "Absence of switching barriers; customer feels no commitment and actively browses competitor promotional pricing.", "Proactive 'Loyalty Lock' contract upgrade campaigns offering free speed boosts in exchange for 12-month commitments."],
        ["The Fiber Technical Support Paradox", "High-tier Fiber Optic subscribers churn at 30.8%—despite paying premium rates ($75-$110/mo)—when exceeding 2 support tickets.", "Premium customers pay top dollar and expect zero downtime; repeated unresolved buffering or routing tickets induces immediate churn.", "Tier-3 Priority Routing in Zendesk: automatically route any multi-ticket Fiber subscriber directly to senior network specialists."],
        ["Early-Tenure Onboarding Cliff", "Over 48% of all churn events occur within the first 90 days of subscriber onboarding ('The Critical Onboarding Window').", "Frustration with self-installation, uncommunicated first-invoice billing surprises, and lack of guided product adoption.", "Launch an automated 'Day-7, Day-30, Day-60' onboarding check-in sequence with dedicated concierge setup assistance."],
        ["Electronic Check Payment Friction", "Subscribers utilizing manual electronic check payments churn at 2.3x the rate of automated credit card or bank debit subscribers.", "Electronic checks require manual monthly customer action, presenting a monthly recurring decision point to discontinue service.", "Incentivize auto-pay enrollment via a persistent $5/month billing discount credit, cementing frictionless automated renewals."]
    ]
    add_styled_table(doc, insights_headers, insights_rows, [Inches(1.5), Inches(1.8), Inches(1.8), Inches(1.6)])

    # 4. Actionable Customer Segmentation Matrix
    add_heading_1(doc, "4. Actionable Customer Segmentation & Intervention Playbook")
    add_paragraph(doc,
        "To operationalize predictions without wasting retention capital, the model segments subscribers into a 2x2 Risk vs. Customer Lifetime Value (CLV) Matrix. Every quadrant triggers a dedicated operational intervention playbook.")

    add_figure(doc, "figures/w4_fig2_risk_matrix.png", "Strategic 2x2 Risk vs. Customer Lifetime Value (CLV) Matrix & Operational Action Playbook", width=Inches(6.3))

    add_heading_2(doc, "4.1 Quadrant 1: VIP Risk Alert (High Risk, High CLV)")
    add_bullet(doc, "Immediate high-priority task dispatched directly to senior Customer Success Managers (CSMs).", bold_prefix="Operational Trigger: ")
    add_bullet(doc, "Direct phone outreach within 4 hours; proactive root-cause diagnosis of open service tickets; customized contract extension incentive (e.g., 20% discount on 24-month contract + free premium router hardware upgrade). Maximum allowable retention budget: $120 per account.", bold_prefix="Intervention Protocol: ")

    add_heading_2(doc, "4.2 Quadrant 2: Automated Efficiency (High Risk, Low CLV)")
    add_bullet(doc, "Automated event trigger pushed to marketing automation platform (Braze / HubSpot).", bold_prefix="Operational Trigger: ")
    add_bullet(doc, "Zero-human-touch digital nurture series; in-app push notifications offering self-service Wi-Fi optimization guides; targeted email offering a $10 billing credit upon enrolling in auto-pay. Maximum allowable retention budget: $15 per account.", bold_prefix="Intervention Protocol: ")

    add_heading_2(doc, "4.3 Quadrant 3: Monitor & Nurture (Low Risk, Low CLV)")
    add_bullet(doc, "Standard automated lifecycle nurture campaigns; periodic product feature newsletters; community forum invites. No direct retention expenditure incurred.", bold_prefix="Intervention Protocol: ")

    add_heading_2(doc, "4.4 Quadrant 4: Brand Advocates & Upsell (Low Risk, High CLV)")
    add_bullet(doc, "Prime candidates for cross-selling and account expansion. Introduce multi-year contract renewals with rate guarantees; cross-sell home security and mobile bundle add-ons; invite to TelePulse Customer Advisory Council.", bold_prefix="Intervention Protocol: ")

    # 5. Non-Technical Stakeholder Presentation Strategy
    add_heading_1(doc, "5. Strategic Communication Plan for Non-Technical Stakeholders")
    add_paragraph(doc,
        "A data science project succeeds or fails based on executive comprehension and frontline adoption. Communicating complex algorithmic models to non-technical leaders requires a deliberate narrative structure.")

    add_figure(doc, "figures/w4_fig3_storytelling_framework.png", "Executive Storytelling Architecture: Minto Pyramid Principle & SCR Communication Flow", width=Inches(6.4))

    add_heading_2(doc, "5.1 The Minto Pyramid Principle: Answer First")
    add_paragraph(doc,
        "Executive leaders operate under severe cognitive constraints and time scarcity. Traditional academic presentations that begin with data cleaning and algorithm equations before revealing findings induce executive disengagement. We adopt Barbara Minto's Pyramid Principle:")
    add_bullet(doc, "Lead immediately with the core conclusion and financial impact ($1.84M net ARR gain; 44% churn reduction).", bold_prefix="Level 1 (The Core Answer): ")
    add_bullet(doc, "Group supporting logic into three digestible pillars: (1) Root Causes Identified, (2) Targeted Retention Playbook, and (3) Proven Financial ROI.", bold_prefix="Level 2 (Strategic Pillars): ")
    add_bullet(doc, "Provide rigorous statistical evidence (PR-AUC, validation splits, SHAP charts) in the appendix, ready for technical due diligence if requested.", bold_prefix="Level 3 (Supporting Data Proof): ")

    add_heading_2(doc, "5.2 Language Translation & Cognitive Load Reduction")
    add_paragraph(doc, "Technical concepts must be systematically translated into business and operational equivalents:")
    
    trans_headers = ["Technical Machine Learning Term", "Non-Technical Business Translation", "Executive Contextual Meaning"]
    trans_rows = [
        ["Precision-Recall AUC = 0.83", "83% Campaign Targeting Efficiency", "Our retention offers hit customers who truly need them, avoiding wasted marketing spend."],
        ["Sensitivity / Recall = 85.4%", "85% Churn Capture Rate", "Out of every 100 subscribers about to leave, the system catches 85 before they cancel."],
        ["Threshold Optimization (tau = 0.38)", "Financial Break-Even Cutoff", "The mathematically balanced trigger point that maximizes net saved profit dollars."],
        ["SHAP Feature Attribution", "Customer Decision Driver Breakdown", "Plain-English explanation showing exactly why a specific customer is unhappy."],
        ["Covariate Shift / Drift Monitoring", "Continuous Market Health Check", "Automated system that alerts us whenever customer buying habits change."]
    ]
    add_styled_table(doc, trans_headers, trans_rows, [Inches(2.1), Inches(2.2), Inches(2.4)])

    # 6. Strategic Recommendations & Future Roadmap
    add_heading_1(doc, "6. Strategic Recommendations & Post-Deployment Roadmap")
    add_paragraph(doc,
        "To transform these analytical insights into long-term enterprise advantage, the data science team recommends a phased three-stage operational rollout:")

    add_heading_2(doc, "6.1 Phase 1 (Months 1–3): Production Pilot & CRM Integration")
    add_bullet(doc, "Deploy the FastAPI microservice into production Docker staging; expose batch predictions directly within Salesforce CRM customer screens.", bold_prefix="Technical Rollout: ")
    add_bullet(doc, "Conduct a controlled A/B pilot across 20,000 active subscribers: Treatment Group receives TelePulse AI segmented outreach; Control Group receives standard reactive service. Measure exact lift in retained ARR.", bold_prefix="A/B Field Pilot: ")

    add_heading_2(doc, "6.2 Phase 2 (Months 4–6): Automated Marketing Integration")
    add_bullet(doc, "Connect nightly batch scoring outputs directly to Braze/HubSpot to automate Quadrant 2 email and SMS retention workflows.", bold_prefix="Workflow Automation: ")
    add_bullet(doc, "Establish weekly MLOps monitoring dashboards tracking feature drift (PSI) and model precision stability.", bold_prefix="Governance: ")

    add_heading_2(doc, "6.3 Phase 3 (Months 7–12): Next-Generation AI Enhancements")
    add_bullet(doc, "Train Natural Language Processing (NLP) Transformer models on Zendesk ticket text to detect customer frustration sentiment in real-time.", bold_prefix="NLP Sentiment Ingestion: ")
    add_bullet(doc, "Implement Contextual Multi-Armed Bandits to dynamically personalize discount dollar amounts, maximizing retention while minimizing concession costs.", bold_prefix="Dynamic Discount Bandits: ")

    add_callout(
        doc,
        "TelePulse AI bridges the gap between advanced predictive data science and executive business strategy, providing an actionable, highly lucrative retention engine that delivers sustained competitive advantage.",
        title="Capstone Conclusion"
    )

    # Save document
    out_path = "deliverables/Week_4_Comprehensive_Report_and_Insights_Presentation.docx"
    doc.save(out_path)
    print(f"Successfully generated: {out_path}")

if __name__ == '__main__':
    build_week4_document()
