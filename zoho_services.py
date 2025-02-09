import requests
from zoho_auth import get_access_token
from response_parser import response_parser

ZOHO_BASE_URL = "https://www.zohoapis.in/crm/v7"

def fetch_data_from_zoho(filters):
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json"
    }

    criteria = []

    if 'bedrooms' in filters:
        criteria.append(f"(Bedrooms:equals:{filters['bedrooms']})")
    if 'bathrooms' in filters:
        criteria.append(f"(Bathrooms:equals:{filters['bathrooms']})")
    if 'kitchen' in filters:
        criteria.append(f"(Kitchen:equals:{filters['kitchen']})")
    if 'hall' in filters:
        criteria.append(f"(Hall:equals:{filters['hall']})")
    if 'parking_available' in filters:
        criteria.append(f"(Parking_Available:equals:{filters['parking_available']})")
    if 'balcony' in filters:
        criteria.append(f"(Balcony:equals:{filters['balcony']})")
    if 'furnished' in filters:
        criteria.append(f"(Furnished:equals:{filters['furnished']})")
    if 'swimming_pool' in filters:
        criteria.append(f"(Swimming_Pool:equals:{filters['swimming_pool']})")
    if 'number_of_parking_spaces' in filters:
        criteria.append(f"(Number_of_Parking_Space:equals:{filters['number_of_parking_spaces']})")
    if 'garden' in filters:
        criteria.append(f"(Garden:equals:{filters['garden']})")
    if 'gym_facility' in filters:
        criteria.append(f"(Gym_Facility:equals:{filters['gym_facility']})")
    if 'year_built' in filters:
        criteria.append(f"(Year_Built:equals:{filters['year_built']})")

    if 'rent_min' in filters:
        criteria.append(f"(Rent_per_month_in_USD1:greater_equal:{filters['rent_min']})")
    if 'rent_max' in filters:
        criteria.append(f"(Rent_per_month_in_USD1:less_equal:{filters['rent_max']})")

    if 'street_address' in filters:
        criteria.append(f"(Street_Address:contains:{filters['street_address']})")
    if 'city' in filters:
        criteria.append(f"(City:equals:{filters['city']})")
    if 'province' in filters:
        criteria.append(f"(Province:equals:{filters['province']})")
    if 'country' in filters:
        criteria.append(f"(Country:equals:{filters['country']})")
    if 'moving_date' in filters:
        criteria.append(f"(Moving_Date:equals:{filters['moving_date']})")

    search_criteria = " and ".join(criteria) if criteria else ""

    print(f"Search Criteria: {search_criteria}")

    url = f"{ZOHO_BASE_URL}/Listings/search?criteria={search_criteria}"

    response = requests.get(url, headers=headers)
    print(response)
    print()
    if response.status_code == 204:
        return [{"message": "No relevant data found."}]
    if response.status_code == 200:
        data = response.json().get("data", [])
        if data:
            return response_parser(data)
            # return data
        else:
            return [{"message": "No relevant data found."}]
    else:
        return [{"message": f"Error fetching data: {response.text}"}]