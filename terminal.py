from prompts import GENERAL_SUPPORT_PROMPT
from azure_client import generate_response

# Sample input
customer_query = "My UPI ID is not working."

# Inject variables into existing prompt
final_prompt = GENERAL_SUPPORT_PROMPT.format(
    company_name="PhonePe",
    customer_query=customer_query
)

# Generate response using existing Azure client
response = generate_response(final_prompt)

# Print response in terminal
print("\n========== CUSTOMER SUPPORT RESPONSE ==========\n")
print(response)
print("\n==============================================\n")
