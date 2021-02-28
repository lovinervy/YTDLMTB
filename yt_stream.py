import requests


def get(m3u8_url: str, title: str, size: int) -> str:
    response = str(requests.get(m3u8_url).content)


    response = response.split('#')
    resolution = []
    for resp in response:
        if resp.rfind('RESOLUTION') != -1:
            resolution.append(resp)
    
    content = []
    for res in resolution:
        content.append(res.split('\\n'))
    
    for con in content:
        res = con[0].split(',')
        res = [x for x in res if x.rfind('RESOLUTION')!= -1]
        true_res = res[0].split('x')
        if true_res[1] == str(size):
            true_res = res[0]
            true_link = con[1]
            break
    
    m3u8_reply = '#EXTM3U\n'
    m3u8_reply += '#EXT-X-INDEPENDENT-SEGMENTS\n'
    for res in content:
        if str(res[0]).rfind(str(true_res)) != -1:
            m3u8_reply += f'#{str(res[0])}\n'
            m3u8_reply += f'{str(true_link)}'
    
    save_path = f'downloads/{title}.m3u8'
    m3u8_reply = bytes(m3u8_reply, 'utf-8')
    with open(save_path, 'wb') as f:
        f.write(m3u8_reply)
    return save_path