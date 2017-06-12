
import urllib.request

url = """
https://auto.ru/moskva/cars/vaz/2107/all/?beaten=1&customs_state=1&geo_id=
213&geo_radius=200&image=true&sort_offers=fresh_relevance_1-DESC&top_days=
off&currency=RUR&output_type=list&page_num_offers=1
"""

res = urllib.request.urlopen(url).read()
f = open('res.html', 'w+')
f.write(str(res))
f.close()