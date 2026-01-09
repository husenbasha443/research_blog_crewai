from prompts import GENERAL_SUPPORT_PROMPT
from azure_client import generate_response

customer_query = "My UPI ID is not working."

final_prompt = GENERAL_SUPPORT_PROMPT.format(
    company_name="PhonePe",
    customer_query=customer_query
)

response = generate_response(final_prompt)

print("\n CUSTOMER SUPPORT RESPONSE \n")
print(response)
