import streamlit as st
st.image("logo.png", width=200)
st.set_page_config(
    page_title="MintMyWealth Retirement Calculator",
    page_icon="logo.png",
    layout="wide"
)

st.title(" MintMyWealth Retirement Calculator")

st.markdown("### Plan your retirement corpus")

# Inputs

col1, col2 = st.columns(2)

with col1:

    current_age = st.number_input(
        "Current Age",
        min_value=18,
        max_value=80,
        value=35
    )

    retirement_age = st.number_input(
        "Retirement Age",
        min_value=current_age + 1,
        max_value=90,
        value=60
    )

    current_corpus = st.number_input(
        "Current Retirement Corpus (₹)",
        value=1000000
    )

    monthly_sip = st.number_input(
        "Monthly SIP (₹)",
        value=25000
    )

with col2:

    expected_return = st.number_input(
        "Expected Return Before Retirement (%)",
        value=12.0
    )

    inflation = st.number_input(
        "Inflation (%)",
        value=6.0
    )

    monthly_expense_today = st.number_input(
        "Current Monthly Expense (₹)",
        value=50000
    )

    life_expectancy = st.number_input(
        "Life Expectancy",
        min_value=retirement_age + 1,
        max_value=100,
        value=85
    )

# Calculations

years_to_retirement = retirement_age - current_age

future_monthly_expense = (
    monthly_expense_today *
    ((1 + inflation/100) ** years_to_retirement)
)

annual_expense_retirement = future_monthly_expense * 12

retirement_years = life_expectancy - retirement_age

required_corpus = (
    annual_expense_retirement *
    retirement_years
)

future_corpus = (
    current_corpus *
    ((1 + expected_return/100) ** years_to_retirement)
)

monthly_rate = expected_return / 100 / 12

months = years_to_retirement * 12

sip_future_value = (
    monthly_sip *
    (((1 + monthly_rate) ** months - 1) / monthly_rate)
)

projected_corpus = future_corpus + sip_future_value

goal_achievement = (
    projected_corpus / required_corpus
) * 100

surplus_deficit = projected_corpus - required_corpus

st.divider()

st.subheader("Retirement Results")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric(
        "Required Corpus",
        f"₹ {required_corpus:,.0f}"
    )

with c2:
    st.metric(
        "Projected Corpus",
        f"₹ {projected_corpus:,.0f}"
    )

with c3:
    st.metric(
        "Goal Achievement",
        f"{goal_achievement:.1f}%"
    )

if surplus_deficit >= 0:
    st.success(
        f"Surplus: ₹ {surplus_deficit:,.0f}"
    )
else:
    st.error(
        f"Shortfall: ₹ {abs(surplus_deficit):,.0f}"
    )

st.divider()

st.subheader("Summary")

st.write(
    f"Years to Retirement: {years_to_retirement}"
)

st.write(
    f"Future Monthly Expense at Retirement: ₹ {future_monthly_expense:,.0f}"
)

st.write(
    f"Retirement Duration: {retirement_years} years"
)

st.write(
    f"Current Corpus: ₹ {current_corpus:,.0f}"
)

st.write(
    f"Monthly SIP: ₹ {monthly_sip:,.0f}"
)

st.caption(
    "For educational purposes only. Returns are assumed and not guaranteed."
)