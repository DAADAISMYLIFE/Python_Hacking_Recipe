# web_path_scanner_ex.py
# html 문서 내의 태그를 분석하여 경로를 탐색
# 더 향상된 기능 추가

import requests
import copy
from bs4 import BeautifulSoup, SoupStrainer

target_domain = "https://shop.hakhub.net/"
results = set()

def check_target_domain(domain):
    # 주소 마지막의 `/` 제거
    if domain[-1] == "/":
        return domain[:-1]
    else:
        return domain

def discover_directory(domain):
    hrefs = set()
    try:
        content = requests.get(domain).content
    except requests.exceptions.ConnectionError:
        pass
    except Exception as e:
        print(f"requests error : {e}")
    
    for link in BeautifulSoup(content, features="html.parser", parse_only=SoupStrainer("a")):
        if hasattr(link, "href"):
            try:
                path = link["href"]
                # 프래그먼트(#)나 단순 리소스 무시
                if (
                    path.startswith("#")
                    or path.startswith("javascript")
                    or path.endswith(".jpg")
                    or path.endswith(".png")
                    or path.endswith(".css")
                    or path.endswith(".js")
                ):
                    continue
                elif path.startswith("/") or path.startswith("?"):
                    hrefs.add(f"{target_domain}{path}")
                elif target_domain not in path and path[:4]!="http":
                    hrefs.add(f"{target_domain}{path}")
                else:
                    hrefs.add(path)
            except KeyError:
                pass
            except Exception as e:
                print(f"Error when parsing: {e}")
    
    for href in hrefs:
        if href.startswith(target_domain):
            results.add(href)
            
            
if __name__ == "__main__":
    target_domain = check_target_domain(target_domain)
    discover_directory(target_domain)
    links = copy.deepcopy(results)  # 깊은 복사
    print(f"Start Scanning on {len(links)} links..")
    
    for link in links:
        print(f"Searching on... {link}")
        links.add(link)
        discover_directory(link)
    
    print(f"{results}")
    print(f"Found {len(results)} Links!!")