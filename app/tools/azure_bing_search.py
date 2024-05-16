import httpx 

from app.config import (
    API_KEY,
    ENDPOINT
)


def search_product_by_image(image_path):
    headers= {
    'Ocp-Apim-Subscription-Key': 'a26da85516f34ec6810578315151a554',
    'Content-Type': 'multipart/form-data'
    }
    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        response = httpx.post("https://api.bing.microsoft.com/v7.0/images/visualsearch", headers=headers, files=files)
    
    result = response.json()
    print(result)

    host_page_urls = []
    if 'tags' in result:
        for tag in result['tags']:
            if 'actions' in tag:
                for action in tag['actions']:
                    if 'data' in action and 'value' in action['data']:
                        for value in action['data']['value']:
                            if 'hostPageUrl' in value:
                                host_page_urls.append(value['hostPageUrl'])

    return host_page_urls