import requests
API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjYzMTAxMDEzNywiYWFpIjoxMSwidWlkIjoxMDA4MTMwOTQsImlhZCI6IjIwMjYtMDMtMTBUMDY6MDY6NTAuMDAwWiIsInBlciI6Im1lOndyaXRlIiwiYWN0aWQiOjM0MTUzNDc2LCJyZ24iOiJhcHNlMiJ9.jdURCy9bk_TTB3gt8c9ka46jtObS-GM8icwD67v8d2M"
url = "https://api.monday.com/v2"
def fetch_boards():
    query = """
    {
      boards {
        id
        name
        items_page(limit: 100) {
          items {
            name
            column_values {
              text
              column {
                title
              }
            }
          }
        }
      }
    }
    """

    headers = {"Authorization": API_KEY}
    response = requests.post(url, json={"query": query}, headers=headers)
    return response.json()