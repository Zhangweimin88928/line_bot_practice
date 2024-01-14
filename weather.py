import requests
#


def WeatherGet(user_location):
    try:
        import xml.etree.cElementTree as et
    except ImportError:
        import xml.etree.ElementTree as et

    user_key = "CWB-375A3979-1EC7-408F-99B1-2C36F8A5311B"
    doc_name = "F-C0032-001"

    api_link = "https://opendata.cwb.gov.tw/opendataapi?dataid=%s&authorizationkey=%s" % (
        doc_name, user_key)

    report = requests.get(api_link).text

    # print(report)

    xml_namespace = "{urn:cwb:gov:tw:cwbcommon:0.1}"
    root = et.fromstring(report)
    dataset = root.find(xml_namespace+'dataset')
    location_info = dataset.findall(xml_namespace+'location')
    #取得<location> Elements,每個location就表示一個縣市資料
    location = user_location
    target_idx = -1
    for idx, ele in enumerate(location_info):
        locationName = ele[0].text  # 取得縣市名
        if locationName == location:
            target_idx = idx
            break
    if target_idx != -1:
        show = ''
        tlist = ['天氣狀況', '最高溫', '最低溫', '舒適度', '降雨機率']
        for i in range(5):
            element = location_info[target_idx][i+1]  # 取得weather element
            timeblock = element[1]  # 取出目前時間點的資料
            data = timeblock[2][0].text
            show = show + tlist[i] + ':' + data + '\n'
    else:
        show = '無此縣市資料，注意xx縣xx市\n氣象局使用[臺]不是[台]'

    return show
