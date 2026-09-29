import os
import re
import certifi
import airportsdata
import pycountry
import requests

from dotenv import load_dotenv


load_dotenv()


os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()


API_KEY = os.getenv("AVIATIONSTACK_API_KEY")


# Default origin when user says only destination, e.g. "Japan Trip"
# Change this if your default if your location is not Sri Lanka/ Colomba.
DEFAULT_ORIGIN_IATA = os.getenv("DEFAULT_ORIGIN_IATA", "CMB")


BASE_URL = "https://api.aviationstack.com/v1/flights"


AIRPORTS = airportsdata.load("IATA")


COUNTRY_ALIASES = {
    "sri lanka": "LK",
    "sl": "LK",
    "lka": "LK",
    "ceylon": "LK",

    "united states": "US",
    "united states of america": "US",
    "usa": "US",
    "us": "US",
    "america": "US",

    "united kingdom": "GB",
    "uk": "GB",
    "gb": "GB",
    "great britain": "GB",
    "britain": "GB",
    "england": "GB",

    "italy": "IT",
    "italia": "IT",
    "it": "IT",

    "japan": "JP",
    "jp": "JP",

    "singapore": "SG",
    "sg": "SG",

    "australia": "AU",
    "au": "AU",

    "canada": "CA",
    "ca": "CA",

    "france": "FR",
    "fr": "FR",

    "germany": "DE",
    "de": "DE",
    "deutschland": "DE",

    "switzerland": "CH",
    "ch": "CH",

    "india": "IN",
    "in": "IN",

    "maldives": "MV",
    "mv": "MV",

    "united arab emirates": "AE",
    "uae": "AE",
    "ae": "AE",

    "south korea": "KR",
    "korea": "KR",
    "republic of korea": "KR",
    "kr": "KR",

    "china": "CN",
    "cn": "CN",

    "thailand": "TH",
    "th": "TH",

    "malaysia": "MY",
    "my": "MY",

    "indonesia": "ID",
    "id": "ID",

    "new zealand": "NZ",
    "nz": "NZ"
}


# Preferred main airport for country-level search
COUNTRY_MAIN_AIRPORT = {

    # Asia
    "LK": "CMB",  # Sri Lanka - Bandaranaike International Airport
    "IN": "DEL",  # India - Indira Gandhi International Airport
    "JP": "HND",  # Japan - Tokyo Haneda Airport
    "SG": "SIN",  # Singapore - Changi Airport
    "CN": "PEK",  # China - Beijing Capital International Airport
    "KR": "ICN",  # South Korea - Incheon International Airport
    "TH": "BKK",  # Thailand - Suvarnabhumi Airport
    "MY": "KUL",  # Malaysia - Kuala Lumpur International Airport
    "ID": "CGK",  # Indonesia - Soekarno-Hatta International Airport
    "PH": "MNL",  # Philippines - Ninoy Aquino International Airport
    "VN": "SGN",  # Vietnam - Tan Son Nhat International Airport
    "BD": "DAC",  # Bangladesh - Hazrat Shahjalal International Airport
    "NP": "KTM",  # Nepal - Tribhuvan International Airport
    "PK": "ISB",  # Pakistan - Islamabad International Airport
    "MV": "MLE",  # Maldives - Velana International Airport

    # Middle East
    "AE": "DXB",  # UAE - Dubai International Airport
    "QA": "DOH",  # Qatar - Hamad International Airport
    "SA": "JED",  # Saudi Arabia - King Abdulaziz International Airport
    "OM": "MCT",  # Oman - Muscat International Airport
    "BH": "BAH",  # Bahrain - Bahrain International Airport
    "KW": "KWI",  # Kuwait - Kuwait International Airport
    "JO": "AMM",  # Jordan - Queen Alia International Airport
    "IL": "TLV",  # Israel - Ben Gurion Airport
    "TR": "IST",  # Türkiye - Istanbul Airport

    # Europe
    "IT": "FCO",  # Italy - Rome Fiumicino Airport
    "GB": "LHR",  # United Kingdom - London Heathrow Airport
    "FR": "CDG",  # France - Paris Charles de Gaulle Airport
    "DE": "FRA",  # Germany - Frankfurt Airport
    "CH": "ZRH",  # Switzerland - Zurich Airport
    "ES": "MAD",  # Spain - Madrid-Barajas Airport
    "NL": "AMS",  # Netherlands - Amsterdam Schiphol Airport
    "BE": "BRU",  # Belgium - Brussels Airport
    "AT": "VIE",  # Austria - Vienna International Airport
    "PT": "LIS",  # Portugal - Lisbon Airport
    "IE": "DUB",  # Ireland - Dublin Airport
    "GR": "ATH",  # Greece - Athens International Airport
    "SE": "ARN",  # Sweden - Stockholm Arlanda Airport
    "NO": "OSL",  # Norway - Oslo Airport
    "DK": "CPH",  # Denmark - Copenhagen Airport
    "FI": "HEL",  # Finland - Helsinki Airport
    "PL": "WAW",  # Poland - Warsaw Chopin Airport
    "CZ": "PRG",  # Czechia - Václav Havel Airport Prague

    # North America
    "US": "JFK",  # USA - John F. Kennedy International Airport
    "CA": "YYZ",  # Canada - Toronto Pearson International Airport
    "MX": "MEX",  # Mexico - Mexico City International Airport

    # South America
    "BR": "GRU",  # Brazil - São Paulo/Guarulhos International Airport
    "AR": "EZE",  # Argentina - Ezeiza International Airport
    "CL": "SCL",  # Chile - Santiago International Airport
    "CO": "BOG",  # Colombia - El Dorado International Airport
    "PE": "LIM",  # Peru - Jorge Chávez International Airport

    # Oceania
    "AU": "SYD",  # Australia - Sydney Airport
    "NZ": "AKL",  # New Zealand - Auckland Airport

    # Africa
    "ZA": "JNB",  # South Africa - O.R. Tambo International Airport
    "EG": "CAI",  # Egypt - Cairo International Airport
    "KE": "NBO",  # Kenya - Jomo Kenyatta International Airport
    "ET": "ADD",  # Ethiopia - Addis Ababa Bole International Airport
    "MA": "CMN",  # Morocco - Mohammed V International Airport
    "NG": "LOS",  # Nigeria - Murtala Muhammed International Airport
}


CITY_DEFAULT_AIRPORT = {

    # Sri Lanka
    "colombo": "CMB",
    "negombo": "CMB",
    "katunayake": "CMB",
    "kandy": "CMB",
    "galle": "CMB",
    "jaffna": "JAF",

    # Italy
    "rome": "FCO",
    "milan": "MXP",
    "catania": "CTA",
    "palermo": "PMO",
    "naples": "NAP",
    "venice": "VCE",
    "bologna": "BLQ",
    "florence": "FLR",
    "pisa": "PSA",
    "turin": "TRN",
    "bari": "BRI",

    # United Kingdom
    "london": "LHR",
    "manchester": "MAN",
    "birmingham": "BHX",
    "edinburgh": "EDI",
    "glasgow": "GLA",
    "bristol": "BRS",

    # France
    "paris": "CDG",
    "nice": "NCE",
    "lyon": "LYS",
    "marseille": "MRS",
    "toulouse": "TLS",

    # Germany
    "frankfurt": "FRA",
    "munich": "MUC",
    "berlin": "BER",
    "dusseldorf": "DUS",
    "hamburg": "HAM",
    "cologne": "CGN",

    # Switzerland
    "zurich": "ZRH",
    "geneva": "GVA",
    "basel": "BSL",

    # Spain
    "madrid": "MAD",
    "barcelona": "BCN",
    "malaga": "AGP",
    "valencia": "VLC",
    "seville": "SVQ",

    # Netherlands
    "amsterdam": "AMS",
    "rotterdam": "RTM",
    "eindhoven": "EIN",

    # Austria
    "vienna": "VIE",
    "salzburg": "SZG",

    # Portugal
    "lisbon": "LIS",
    "porto": "OPO",

    # Ireland
    "dublin": "DUB",
    "cork": "ORK",

    # Greece
    "athens": "ATH",
    "thessaloniki": "SKG",

    # Sweden
    "stockholm": "ARN",
    "gothenburg": "GOT",

    # Norway
    "oslo": "OSL",
    "bergen": "BGO",

    # Denmark
    "copenhagen": "CPH",

    # Finland
    "helsinki": "HEL",

    # Poland
    "warsaw": "WAW",
    "krakow": "KRK",

    # Czechia
    "prague": "PRG",

    # Japan
    "tokyo": "HND",
    "osaka": "KIX",
    "kyoto": "KIX",
    "nagoya": "NGO",
    "fukuoka": "FUK",
    "sapporo": "CTS",
    "okinawa": "OKA",

    # Singapore
    "singapore": "SIN",

    # India
    "new delhi": "DEL",
    "delhi": "DEL",
    "mumbai": "BOM",
    "bangalore": "BLR",
    "bengaluru": "BLR",
    "chennai": "MAA",
    "hyderabad": "HYD",
    "kolkata": "CCU",
    "kochi": "COK",
    "goa": "GOI",

    # UAE
    "dubai": "DXB",
    "abu dhabi": "AUH",
    "sharjah": "SHJ",

    # Qatar
    "doha": "DOH",

    # Saudi Arabia
    "riyadh": "RUH",
    "jeddah": "JED",
    "medina": "MED",

    # Türkiye
    "istanbul": "IST",
    "ankara": "ESB",
    "antalya": "AYT",

    # Thailand
    "bangkok": "BKK",
    "phuket": "HKT",
    "chiang mai": "CNX",

    # Malaysia
    "kuala lumpur": "KUL",
    "penang": "PEN",

    # Indonesia
    "jakarta": "CGK",
    "bali": "DPS",
    "denpasar": "DPS",

    # South Korea
    "seoul": "ICN",
    "busan": "PUS",
    "jeju": "CJU",

    # China
    "beijing": "PEK",
    "shanghai": "PVG",
    "guangzhou": "CAN",
    "shenzhen": "SZX",
    "chengdu": "TFU",

    # Hong Kong
    "hong kong": "HKG",

    # Maldives
    "male": "MLE",
    "malé": "MLE",

    # Australia
    "sydney": "SYD",
    "melbourne": "MEL",
    "brisbane": "BNE",
    "perth": "PER",
    "adelaide": "ADL",
    "gold coast": "OOL",

    # New Zealand
    "auckland": "AKL",
    "wellington": "WLG",
    "christchurch": "CHC",

    # United States
    "new york": "JFK",
    "los angeles": "LAX",
    "san francisco": "SFO",
    "chicago": "ORD",
    "dallas": "DFW",
    "houston": "IAH",
    "miami": "MIA",
    "boston": "BOS",
    "seattle": "SEA",
    "atlanta": "ATL",
    "washington": "IAD",
    "washington dc": "IAD",
    "las vegas": "LAS",
    "orlando": "MCO",
    "denver": "DEN",
    "austin": "AUS",

    # Canada
    "toronto": "YYZ",
    "vancouver": "YVR",
    "montreal": "YUL",
    "calgary": "YYC",
    "ottawa": "YOW",

    # Brazil
    "sao paulo": "GRU",
    "são paulo": "GRU",
    "rio de janeiro": "GIG",
    "brasilia": "BSB",

    # Argentina
    "buenos aires": "EZE",

    # South Africa
    "johannesburg": "JNB",
    "cape town": "CPT",
    "durban": "DUR",

    # Egypt
    "cairo": "CAI",
    "alexandria": "HBE",

    # Kenya
    "nairobi": "NBO",

    # Morocco
    "casablanca": "CMN",
    "marrakech": "RAK",
}


def clean_text(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    stop_words = [
        "flight", "flights", "ticket", "tickets", "trip", "travel",
        "plan", "complete", "days", "day", "including", "hotel",
        "hotels", "sightseeing", "under", "budget", "info", "information"
    ]

    words = [w for w in text.split() if w not in stop_words]

    return " ".join(words).strip()


def country_name_to_code(text: str):
    text = clean_text(text)

    if text in COUNTRY_ALIASES:
        return COUNTRY_ALIASES[text]

    try:
        country = pycountry.countries.lookup(text)
        return country.alpha_2

    except LookupError:
        pass

    # Detect country name inside longer text
    for country in pycountry.countries:
        country_name = country.name.lower()

        if country_name in text:
            return country.alpha_2

    for alias, code in COUNTRY_ALIASES.items():
        if re.search(rf"\b{re.escape(alias)}\b", text):
            return code

    return None


def airport_country_matches(airport: dict, country_code: str) -> bool:
    airport_country = str(
        airport.get("country", "")
    ).upper().strip()

    if airport_country == country_code:
        return True

    try:
        country = pycountry.countries.get(alpha_2=country_code)

        if country and airport_country.lower() == country.name.lower():
            return True

    except Exception:
        pass

    return False


def get_best_airport_for_country(country_code: str):
    preferred = COUNTRY_MAIN_AIRPORT.get(country_code)

    if preferred and preferred in AIRPORTS:
        return preferred

    candidates = []

    for iata, airport in AIRPORTS.items():
        if not iata:
            continue

        if airport_country_matches(airport, country_code):
            name = str(airport.get("name", "")).lower()
            city = str(airport.get("city", "")).lower()

            score = 0

            if "international" in name:
                score += 50

            if "intl" in name:
                score += 40

            if "capital" in name:
                score += 20

            if city:
                score += 5

            candidates.append((score, iata))

    if not candidates:
        return None

    candidates.sort(reverse=True)

    return candidates[0][1]


def resolve_location_to_iata(location: str):
    """
    Converts country/city/airport/IATA into IATA code.

    Examples:
    Sri Lanka -> CMB
    Japan -> NRT
    Dhaka -> DAC
    Tokyo -> NRT
    CMB -> CMB
    """

    if not location:
        return None

    raw_location = location.strip()

    # Direct IATA code
    if re.fullmatch(r"[A-Za-z]{3}", raw_location):
        code = raw_location.upper()

        if code in AIRPORTS:
            return code

    location_clean = clean_text(raw_location)

    if not location_clean:
        return None

    # City preferred airport
    if location_clean in CITY_DEFAULT_AIRPORT:
        return CITY_DEFAULT_AIRPORT[location_clean]

    # Country preferred airport
    country_code = country_name_to_code(location_clean)

    if country_code:
        airport = get_best_airport_for_country(country_code)

        if airport:
            return airport

    # Exact city match from airport database
    city_matches = []

    for iata, airport in AIRPORTS.items():
        city = str(
            airport.get("city", "")
        ).lower().strip()

        name = str(
            airport.get("name", "")
        ).lower().strip()

        score = 0

        if city == location_clean:
            score += 100

        elif location_clean in city:
            score += 70

        if location_clean in name:
            score += 50

        if "international" in name:
            score += 10

        if score > 0:
            city_matches.append((score, iata))

    if city_matches:
        city_matches.sort(reverse=True)

        return city_matches[0][1]

    return None


def find_location_mentions(query: str):
    """
    Finds country or city names inside a natural language query.
    """

    q = query.lower()
    mentions = []

    # Country aliases
    for alias in COUNTRY_ALIASES:
        if re.search(
            rf"\b{re.escape(alias)}\b",
            q
        ):
            mentions.append(alias)

    # Country names from pycountry
    for country in pycountry.countries:
        name = country.name.lower()

        if (
            len(name) >= 4
            and re.search(
                rf"\b{re.escape(name)}\b",
                q
            )
        ):
            mentions.append(name)

    # City names from our preferred city map
    for city in CITY_DEFAULT_AIRPORT:
        if re.search(
            rf"\b{re.escape(city)}\b",
            q
        ):
            mentions.append(city)

    # Remove duplicate while keeping order
    unique_mentions = []

    for item in mentions:
        if item not in unique_mentions:
            unique_mentions.append(item)

    return unique_mentions


def parse_route(query: str):
    """
    Returns:
    dep_iata, arr_iata

    Can return:
    None, None -> global live flights
    DAC, NRT -> filtered route
    DAC, None -> all flights from DAC
    None, NRT -> all flights to NRT
    """

    q = query.strip()
    q_lower = q.lower()

    # Global / all-country query
    global_keywords = [
        "all country",
        "all countries",
        "global flight",
        "global flights",
        "all flight",
        "all flights",
        "worldwide flight",
        "worldwide flights",
    ]

    if any(keyword in q_lower for keyword in global_keywords):
        return None, None

    # Direct IATA code route: DAC to NRT
    codes = re.findall(r"\b[A-Za-z]{3}\b", q)

    valid_codes = [
        code.upper()
        for code in codes
        if code.upper() in AIRPORTS
    ]

    if len(valid_codes) >= 2:
        dep = valid_codes[0]
        arr = valid_codes[1]

        return dep, arr

    # Pattern: from X to Y
    match = re.search(
        r"\bfrom\s+(.+?)\s+\bto\s+(.+?)(?:\s+(?:on|for|under|including|with|in|at)\b|[.!?]|$)",
        q_lower,
    )

    if match:
        origin_text = match.group(1)
        dest_text = match.group(2)

        dep_iata = resolve_location_to_iata(origin_text)
        arr_iata = resolve_location_to_iata(dest_text)

        return dep_iata, arr_iata

    # Pattern: to Y from X
    match = re.search(
        r"\bto\s+(.+?)\s+\bfrom\s+(.+?)(?:\s+(?:on|for|under|including|with|in|at)\b|[.!?]|$)",
        q_lower,
    )

    if match:
        dest_text = match.group(1)
        origin_text = match.group(2)

        dep_iata = resolve_location_to_iata(origin_text)
        arr_iata = resolve_location_to_iata(dest_text)

        return dep_iata, arr_iata

    # Pattern: flights from X
    match = re.search(
        r"\bfrom\s+(.+?)(?:[.!?]|$)",
        q_lower
    )

    if match:
        origin_text = match.group(1)

        dep_iata = resolve_location_to_iata(origin_text)

        return dep_iata, None

    # Pattern: flights to X
    match = re.search(
        r"\bto\s+(.+?)(?:[.!?]|$)",
        q_lower
    )

    if match:
        dest_text = match.group(1)

        arr_iata = resolve_location_to_iata(dest_text)

        return None, arr_iata

    # Fallback: find country/city mentions
    mentions = find_location_mentions(q)

    if len(mentions) >= 2:
        dep_iata = resolve_location_to_iata(
            mentions[0]
        )

        arr_iata = resolve_location_to_iata(
            mentions[1]
        )

        return dep_iata, arr_iata

    if len(mentions) == 1:
        arr_iata = resolve_location_to_iata(
            mentions[0]
        )

        return DEFAULT_ORIGIN_IATA, arr_iata

    return None, None


def format_flight(flight: dict):
    airline = (
        flight.get("airline", {}).get("name")
        or "Unknown airline"
    )

    flight_number = (
        flight.get("flight", {}).get("iata")
        or "Unknown flight number"
    )

    status = (
        flight.get("flight_status")
        or "Unknown"
    )

    dep = flight.get("departure", {}) or {}
    arr = flight.get("arrival", {}) or {}

    dep_airport = (
        dep.get("airport")
        or "Unknown departure airport"
    )

    dep_iata = (
        dep.get("iata")
        or "Unknown"
    )

    dep_terminal = (
        dep.get("terminal")
        or "N/A"
    )

    dep_gate = (
        dep.get("gate")
        or "N/A"
    )

    dep_scheduled = (
        dep.get("scheduled")
        or "Unknown"
    )

    dep_delay = dep.get("delay")

    dep_delay_text = (
        f"{dep_delay} minutes"
        if dep_delay is not None
        else "N/A"
    )

    arr_airport = (
        arr.get("airport")
        or "Unknown arrival airport"
    )

    arr_iata = (
        arr.get("iata")
        or "Unknown"
    )

    arr_terminal = (
        arr.get("terminal")
        or "N/A"
    )

    arr_gate = (
        arr.get("gate")
        or "N/A"
    )

    arr_scheduled = (
        arr.get("scheduled")
        or "Unknown"
    )

    arr_delay = arr.get("delay")

    arr_delay_text = (
        f"{arr_delay} minutes"
        if arr_delay is not None
        else "N/A"
    )

    return f"""
Airline: {airline}
Flight: {flight_number}
Status: {status}

Departure:
- Airport: {dep_airport}
- IATA: {dep_iata}
- Terminal: {dep_terminal}
- Gate: {dep_gate}
- Scheduled: {dep_scheduled}
- Delay: {dep_delay_text}

Arrival:
- Airport: {arr_airport}
- IATA: {arr_iata}
- Terminal: {arr_terminal}
- Gate: {arr_gate}
- Scheduled: {arr_scheduled}
- Delay: {arr_delay_text}
""".strip()


def search_flights(query: str, limit: int = 10):
    if not API_KEY:
        return (
            "Flight API error: AVIATIONSTACK_API_KEY is missing.\n"
            "Please add this in your .env file:\n"
            "AVIATIONSTACK_API_KEY=your_api_key_here"
        )

    dep_iata, arr_iata = parse_route(query)

    params = {
        "access_key": API_KEY,
        "limit": min(limit, 100),
    }

    if dep_iata:
        params["dep_iata"] = dep_iata

    if arr_iata:
        params["arr_iata"] = arr_iata

    try:
        response = requests.get(
            BASE_URL,
            params=params,
            timeout=30
        )

        data = response.json()

    except requests.exceptions.RequestException as e:
        return f"Flight API request failed: {e}"

    except ValueError:
        return "Flight API returned invalid JSON."

    if "error" in data:
        error = data["error"]

        return (
            "Flight API error:\n"
            f"Code: {error.get('code', 'Unknown')}\n"
            f"Message: {error.get('message', 'Unknown error')}"
        )

    flight_data = data.get("data", [])

    if not flight_data:
        route_text = ""

        if dep_iata and arr_iata:
            route_text = (
                f" for route {dep_iata} to {arr_iata}"
            )

        elif dep_iata:
            route_text = (
                f" from {dep_iata}"
            )

        elif arr_iata:
            route_text = (
                f" to {arr_iata}"
            )

        return (
            f"No live flight data found{route_text}.\n\n"
            "Note: AviationStack provides live/status flight data, not ticket prices. "
            "For actual fare prices, use a flight-pricing API such as Amadeus."
        )

    route_info = "Global live flights"

    if dep_iata and arr_iata:
        route_info = (
            f"Live flights from {dep_iata} to {arr_iata}"
        )

    elif dep_iata:
        route_info = (
            f"Live flights from {dep_iata}"
        )

    elif arr_iata:
        route_info = (
            f"Live flights to {arr_iata}"
        )

    formatted_flights = [
        format_flight(flight)
        for flight in flight_data[:limit]
    ]

    return (
        f"{route_info}\n\n"
        + "\n\n---\n\n".join(formatted_flights)
    )


if __name__ == "__main__":
    print(
        search_flights(
            "Plan a 7 days Japan trip from Bangladesh"
        )
    )

    print("\n" + "=" * 80 + "\n")

    print(
        search_flights(
            "all country flight info"
        )
    )
