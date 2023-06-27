# python logger 
import logging
logger = logging.getLogger(__name__)


def azure_auth(clientid, clientsecret, tokenurl):
    import urllib.request
    import json
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'} 

    payload = {
        'grant_type': 'client_credentials', 
        'client_id': clientid,
        'client_secret': clientsecret,
        # 'scope': 'https://management.azure.com/.default'
        'scope': 'https://purview.azure.net/.default'
        }


    req = urllib.request.Request(url=tokenurl, data=urllib.parse.urlencode(payload).encode('utf-8'), headers=headers) 
    req.method = 'GET'
    response = urllib.request.urlopen(req)
    res = response.read()
    access_token = json.loads(res.decode('utf-8'))['access_token']

    return access_token


def search_catalog(
        keywords='Purchase History', 
        offset=0, 
        limit=100, 
        filter={}, 
        access_token=None,
        purview_url=None): 
    
    import urllib.request
    import json

    headers = {
    'Authorization': f'Bearer {access_token}',
    'Content-Type': 'application/json'
    }

    payload = {
        # "keywords": "Purchase History",
        "keywords": keywords,
        # "offset": -94587422,
        # "limit": -33306148,
        # "filter": {}
    }

    req = urllib.request.Request(url=purview_url, data=json.dumps(payload).encode('utf-8'), headers=headers)
    req.method = 'POST'

    res_json = None

    try: 
        res = urllib.request.urlopen(req)
        # pprint(res.read().decode('utf-8'))

        res_json = json.loads(res.read().decode('utf-8'))
        # logger.info(res_json)
    except urllib.error.HTTPError as e:
        logger.error(e.code)
        logger.error(e.read())

    return res_json


def get_asset_byguid(itemid=None,         
        access_token=None,
        purviewendpoint=None): 
    
    import urllib.request
    import json

    # {Endpoint}/catalog/api/atlas/v2/entity/guid/5cf8a9e5-c9fd-abe0-2e8c-d40024263dcb
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
        }


    req = urllib.request.Request(
        url=f"{purviewendpoint}/catalog/api/atlas/v2/entity/guid/{itemid}", 
        data=None, 
        headers=headers)
    req.method = 'GET'

    # pprint(req.data)

    res_json = None

    try: 
        res = urllib.request.urlopen(req)
        # pprint(res.read().decode('utf-8'))

        res_json = json.loads(res.read().decode('utf-8'))
        # pprint(res_json)
    except urllib.error.HTTPError as e:
        logger.error(e.code)
        logger.error(e.read())


    return res_json

