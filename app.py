import streamlit as st
from prompts import (
    GENERAL_SUPPORT_PROMPT,
    BILLING_SUPPORT_PROMPT,
    TECH_SUPPORT_PROMPT
)
from azure_client import generate_response

st.set_page_config(page_title="Customer Support ChatBot")

st.title("Customer Support ChatBot")
st.write("Enterprise-grade Prompt-Based AI System (Azure OpenAI)")

company_name = st.text_input("Company Name", "PhonePe")
product_name = st.text_input("Product Name", "PhonePe App")

issue_type = st.selectbox(
    "Issue Type",
    ["General", "Billing", "Technical"]
)

customer_query = st.text_area(
    "Customer Query",
    placeholder="Enter customer issue here..."
)

if st.button("Generate Response"):
    if not customer_query.strip():
        st.warning("Please enter a customer query.")
    else:
        if issue_type == "Billing":
            prompt_template = BILLING_SUPPORT_PROMPT
            variables = {
                "company_name": company_name,
                "customer_query": customer_query
            }

        elif issue_type == "Technical":
            prompt_template = TECH_SUPPORT_PROMPT
            variables = {
                "product_name": product_name,
                "customer_query": customer_query
            }

        else:
            prompt_template = GENERAL_SUPPORT_PROMPT
            variables = {
                "company_name": company_name,
                "customer_query": customer_query
            }

        final_prompt = prompt_template.format(**variables)

        response = generate_response(final_prompt)

        st.subheader(" Generated Customer Support Response")
        st.success(response)
