import re
import pickle
import io
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload
from google.auth.transport.requests import Request
from bs4 import BeautifulSoup

PAGE_PATH = '/Users/sean/github/page'
"""
get pages from google and save to html

https://developers.google.com/drive/api/v3/quickstart/python
"""
def update_page(file_id, file_name, *, to_html=None, to_json=None):
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', ['https://www.googleapis.com/auth/drive'])
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    service = build('drive', 'v3', credentials=creds)

    request = service.files().export(fileId=file_id, mimeType=f'text/html')
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    fh.seek(0)

    if to_html:
        with open(f'{file_name}.html', 'wb') as f:
            f.write(fh.read())
            f.close()
    if to_json:
        data = {
            "id" : file_id,
            "name" : file_name
        }
        data["posts"] = html2json(fh.read())
        
        with open(f"{PAGE_PATH}/data/{file_name}.json", "w") as f:
            json.dump(data, f, ensure_ascii=False)

def html2json(html):
    bs = BeautifulSoup(html, "html.parser")
    doc = {}

    cur_h1, cur_h2, cur_h3, cur_li = None, None, None, None

    tags = bs.findAll(["h1", "h2", "h3", "p", "li"])
    i = 0
    while i < len(tags):
        tag = tags[i]
        if not tag.text:
            pass
        elif tag.name == "h1":
            cur_h1 = tag.text
            doc[cur_h1] = {}
        elif tag.name == "h2":
            cur_h2 = tag.text
            doc[cur_h1][cur_h2] = {}
        elif tag.name == "h3":
            cur_h3 = tag.text
            doc[cur_h1][cur_h2][cur_h3] = []
        elif tag.name == "li":
            cur_li = tag.text
            ps = []
            while tags[i + 1].name == "p":
                i += 1
                link = tags[i].find("a")
                if link:
                    ps.append(str(link))
                else:
                    ps.append(tags[i].text)
            try:
                doc[cur_h1][cur_h2][cur_h3].append({
                    "li" : cur_li,
                    "ps" : ps
                })
            except:
                pass
        i += 1
    return doc

def hide_unsolved(docs, solved):
    for h2 in docs.values():
        for h3 in h2.values():
            for post in h3:
                new_ps = []
                i = 0
                while i < len(post["ps"]):
                    id_match = re.match(r"<a.*(BJ|BJE|KT)_(\d+).*", post["ps"][i])
                    if "KT_" not in post["ps"][i]:
                        new_ps.append(post["ps"][i])
                    if id_match and id_match.group(1) not in solved:
                        while i + 1 < len(post["ps"]) and not re.match(r"<.*", post["ps"][i + 1]):
                            i+=1
                    i += 1
                post["ps"] = new_ps
    return docs

if __name__ == '__main__':
    update_page('1B8J_rQtCihzPVSN5wOf7SgEOQRlJFs5Rsf3wFH9_hwM', 'python', to_json=True)
    #html2json(open(f"{PAGE_PATH}/data/teaching_teacher.html", 'r'))
    #update_page('198UELcFM1OojGDVhEl5hk1vRXesDCa03vMldvA6HHGQ', 'machine_learning')
    #update_page('1xgPgq4xDpvCS8Y4rkIYf2Gm_xXr0pg7-aEysidfR3-I', 'terminal')