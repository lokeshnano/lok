import openai
import json 
openai.api_key = "xxx"
p = 'testing'
prompt = f"""
    Replace the values from this example json and remember, the first letter of names should be capitalized, 
    the citizenship should be a 3-letter country code, the date should be in the format mm.dd.yyyy and only contain 2 dots:
        {{
        "firstName": "",
        "lastName": ""
        "citizenship": "",
        "documentNumber": "",
        "dateOfBirth": ""
        }}
    with this data:
    {str(p)}
    """
completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
        ]
    )

completion = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": prompt},
        ]
    )
response = completion.get('choices', [{}])[0].get('message', {}).get('content', None)
    
response_dict = json.loads(response)